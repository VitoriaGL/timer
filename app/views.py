import asyncio
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from .models import Contador


# View assíncrona simples usando função
async def index(request):
    """View assíncrona básica."""
    await asyncio.sleep(0.1)  # Simula operação assíncrona
    return JsonResponse({
        'mensagem': 'Bem-vindo ao projeto Django com views assíncronas!',
        'status': 'sucesso'
    })


# View assíncrona que retorna HTML
async def home(request):
    """View assíncrona que renderiza template."""
    await asyncio.sleep(0.1)
    context = {
        'titulo': 'Projeto Django Assíncrono',
        'descricao': 'Este é um exemplo de views assíncronas no Django'
    }
    return render(request, 'app/home.html', context)


# View assíncrona com operações de banco de dados
async def listar_contadores(request):
    """Lista todos os contadores de forma assíncrona."""
    # Em Django 5.0+, você pode usar async ORM
    contadores_list = []
    async for contador in Contador.objects.all():
        contadores_list.append({
            'id': contador.id,
            'nome': contador.nome,
            'valor': contador.valor,
            'criado_em': contador.criado_em.isoformat(),
        })
    
    return JsonResponse({
        'contadores': contadores_list,
        'total': len(contadores_list)
    })


# View assíncrona para criar contador
@csrf_exempt
async def criar_contador(request):
    """Cria um novo contador de forma assíncrona."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nome = data.get('nome', 'Contador')
            valor = data.get('valor', 0)
            
            # Criar contador de forma assíncrona
            contador = await Contador.objects.acreate(
                nome=nome,
                valor=valor
            )
            
            return JsonResponse({
                'id': contador.id,
                'nome': contador.nome,
                'valor': contador.valor,
                'mensagem': 'Contador criado com sucesso!'
            }, status=201)
        except Exception as e:
            return JsonResponse({
                'erro': str(e)
            }, status=400)
    
    return JsonResponse({
        'erro': 'Método não permitido'
    }, status=405)


# View assíncrona para incrementar contador
@csrf_exempt
async def incrementar_contador(request, contador_id):
    """Incrementa o valor de um contador de forma assíncrona."""
    if request.method == 'POST':
        try:
            contador = await Contador.objects.aget(id=contador_id)
            contador.valor += 1
            await contador.asave()
            
            return JsonResponse({
                'id': contador.id,
                'nome': contador.nome,
                'valor': contador.valor,
                'mensagem': 'Contador incrementado!'
            })
        except Contador.DoesNotExist:
            return JsonResponse({
                'erro': 'Contador não encontrado'
            }, status=404)
        except Exception as e:
            return JsonResponse({
                'erro': str(e)
            }, status=400)
    
    return JsonResponse({
        'erro': 'Método não permitido'
    }, status=405)


# View assíncrona com múltiplas operações
async def estatisticas(request):
    """Retorna estatísticas dos contadores de forma assíncrona."""
    # Executar múltiplas queries assíncronas em paralelo
    total_contadores = await Contador.objects.acount()
    soma_valores = await Contador.objects.aaggregate(
        total=Sum('valor')
    )
    
    # Buscar contador com maior valor
    try:
        maior_contador = await Contador.objects.order_by('-valor').afirst()
        maior_info = {
            'nome': maior_contador.nome,
            'valor': maior_contador.valor
        } if maior_contador else None
    except:
        maior_info = None
    
    return JsonResponse({
        'total_contadores': total_contadores,
        'soma_valores': soma_valores.get('total', 0) or 0,
        'maior_contador': maior_info
    })


# View assíncrona com simulação de operação demorada
async def operacao_demorada(request):
    """Simula uma operação que demora alguns segundos."""
    await asyncio.sleep(2)  # Simula operação que demora 2 segundos
    
    return JsonResponse({
        'mensagem': 'Operação concluída!',
        'tempo_estimado': '2 segundos'
    })


# View assíncrona usando classe (Class-Based View)
class ContadorView(View):
    """Class-based view assíncrona."""
    
    async def get(self, request, contador_id):
        """Busca um contador específico."""
        try:
            contador = await Contador.objects.aget(id=contador_id)
            return JsonResponse({
                'id': contador.id,
                'nome': contador.nome,
                'valor': contador.valor,
                'criado_em': contador.criado_em.isoformat(),
                'atualizado_em': contador.atualizado_em.isoformat(),
            })
        except Contador.DoesNotExist:
            return JsonResponse({
                'erro': 'Contador não encontrado'
            }, status=404)
    
    async def delete(self, request, contador_id):
        """Deleta um contador."""
        try:
            contador = await Contador.objects.aget(id=contador_id)
            await contador.adelete()
            return JsonResponse({
                'mensagem': 'Contador deletado com sucesso!'
            })
        except Contador.DoesNotExist:
            return JsonResponse({
                'erro': 'Contador não encontrado'
            }, status=404)

