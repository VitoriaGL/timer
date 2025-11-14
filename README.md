# Contador Assíncrono Django

Projeto Django simples com contador assíncrono de 10 a 0 segundos que funciona na página web e no terminal simultaneamente.

## 🚀 Características

- **Contador Assíncrono**: Contador regressivo de 10 a 0 segundos
- **Sincronização**: Página web e terminal sincronizados em tempo real
- **Views Assíncronas**: Implementado com async/await do Django
- **Interface Minimalista**: Design simples e limpo

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Navegue até o diretório do projeto:
```bash
cd contador
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
   - **Windows (PowerShell):**
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD):**
     ```bash
     venv\Scripts\activate.bat
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute as migrações:
```bash
python manage.py migrate
```

## 🏃 Executando o Projeto

**Execute apenas um comando:**
```bash
python manage.py contador_tempo
```

Este comando irá:
- Iniciar o servidor Django automaticamente
- Mostrar o contador no terminal
- Sincronizar com a página web

**Acesse no navegador:**
```
http://127.0.0.1:8000/timer/
```

## 📡 Endpoints da API

### GET `/timer/`
Página HTML do contador.

### GET `/timer/status/`
Retorna o status atual do contador em JSON.

**Resposta:**
```json
{
  "segundos": 10,
  "finalizado": false
}
```

### POST `/timer/iniciar/`
Inicia o contador de 10 a 0.

### POST `/timer/resetar/`
Reseta o contador para 10.

## 🎮 Como Usar

1. Execute `python manage.py contador_tempo`
2. Acesse `http://127.0.0.1:8000/timer/` no navegador
3. Clique em "Iniciar" na página
4. O contador começará a contar de 10 a 0 simultaneamente na página e no terminal

## 📚 Estrutura do Projeto

```
contador/
├── app/
│   ├── management/
│   │   └── commands/
│   │       └── contador_tempo.py  # Comando do terminal
│   ├── templates/
│   │   └── app/
│   │       └── contador_tempo.html  # Página HTML
│   ├── urls.py  # Rotas
│   └── views.py  # Views assíncronas
├── contador/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## 🛠️ Tecnologias Utilizadas

- Django 5.0+
- Python 3.8+
- JavaScript (para atualização em tempo real na página)

## 📝 Notas

- O contador usa estado compartilhado entre a página web e o terminal
- Views assíncronas utilizam `async/await` do Django
- Logs do servidor Django estão desabilitados para manter o terminal limpo

##  Licença

Este projeto é um exemplo educacional.
