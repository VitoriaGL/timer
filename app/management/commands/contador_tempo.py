import asyncio
import time
import os
import threading
from django.core.management.base import BaseCommand
from django.core.management import call_command
from app.views import contador_tempo


class Command(BaseCommand):
    help = 'Inicia servidor Django e contador de 10 a 0'

    def handle(self, *args, **options):
        # Limpar tela
        os.system('cls' if os.name == 'nt' else 'clear')
        
        self.stdout.write('=' * 50)
        self.stdout.write('Servidor Django + Contador')
        self.stdout.write('=' * 50)
        self.stdout.write('\nServidor rodando em: http://127.0.0.1:8000/timer/')
        self.stdout.write('Contador sincronizado abaixo:\n')
        self.stdout.write('-' * 50)
        self.stdout.write('\n')
        
        # Iniciar servidor em thread separada
        server_thread = threading.Thread(target=self.iniciar_servidor, daemon=True)
        server_thread.start()
        
        # Aguardar um pouco para o servidor iniciar
        time.sleep(2)
        
        # Mostrar contador inicial
        self.stdout.write('10')
        self.stdout.flush()
        
        # Rodar contador
        try:
            asyncio.run(self.monitorar())
        except KeyboardInterrupt:
            self.stdout.write('\n\nEncerrando...\n')

    def iniciar_servidor(self):
        """Inicia o servidor Django em thread separada."""
        call_command('runserver', '--noreload', verbosity=0)

    async def monitorar(self):
        """Monitora o contador e atualiza o display."""
        ultimo = None
        
        while True:
            agora = time.time()
            
            if contador_tempo['iniciado']:
                decorrido = agora - contador_tempo['tempo_inicial']
                restante = 10 - decorrido
                
                if restante <= 0:
                    restante = 0
                    contador_tempo['iniciado'] = False
                    contador_tempo['tempo_restante'] = 0
                else:
                    contador_tempo['tempo_restante'] = restante
            else:
                restante = contador_tempo['tempo_restante']
            
            num = int(restante)
            
            if num != ultimo:
                self.stdout.write(f'\rContador: {num}   ')
                self.stdout.flush()
                ultimo = num
            
            await asyncio.sleep(0.1)
