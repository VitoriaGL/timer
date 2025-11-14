import time
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Estado global do contador simples (10 a 0)
contador_tempo = {
    'iniciado': False,
    'tempo_inicial': None,
    'tempo_restante': 10
}


async def contador_tempo_page(request):
    """Página HTML do contador de tempo."""
    return render(request, 'app/contador_tempo.html')


async def contador_tempo_status(request):
    """Retorna o status atual do contador (10 a 0)."""
    agora = time.time()
    
    if contador_tempo['iniciado']:
        tempo_decorrido = agora - contador_tempo['tempo_inicial']
        tempo_restante = 10 - tempo_decorrido
        
        if tempo_restante <= 0:
            tempo_restante = 0
            contador_tempo['iniciado'] = False
            contador_tempo['tempo_restante'] = 0
        else:
            contador_tempo['tempo_restante'] = tempo_restante
    else:
        tempo_restante = contador_tempo['tempo_restante']
    
    segundos = int(tempo_restante)
    
    return JsonResponse({
        'segundos': segundos,
        'finalizado': tempo_restante <= 0
    })


@csrf_exempt
async def contador_tempo_iniciar(request):
    """Inicia o contador de 10 a 0."""
    if request.method == 'POST':
        if not contador_tempo['iniciado']:
            contador_tempo['iniciado'] = True
            contador_tempo['tempo_inicial'] = time.time()
            contador_tempo['tempo_restante'] = 10
            return JsonResponse({'mensagem': 'Contador iniciado'})
        else:
            return JsonResponse({'mensagem': 'Já está rodando'})
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)


@csrf_exempt
async def contador_tempo_resetar(request):
    """Reseta o contador para 10."""
    if request.method == 'POST':
        contador_tempo['iniciado'] = False
        contador_tempo['tempo_inicial'] = None
        contador_tempo['tempo_restante'] = 10
        return JsonResponse({'mensagem': 'Resetado'})
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)
