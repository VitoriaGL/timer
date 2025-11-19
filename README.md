# Projeto Django com Views Assíncronas

Este é um projeto Django que demonstra o uso de views assíncronas (async views) introduzidas no Django 3.1+ e melhoradas nas versões mais recentes.

## Características

- **Views Assíncronas**: Exemplos de funções e class-based views assíncronas
- **ORM Assíncrono**: Uso do Django ORM assíncrono (Django 4.1+)
- **Operações de Banco de Dados**: CRUD completo com operações assíncronas
- **API REST**: Endpoints JSON para gerenciamento de contadores

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone ou navegue até o diretório do projeto:
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

6. Crie um superusuário (opcional):
```bash
python manage.py createsuperuser
```

## Executando o Projeto

Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

O servidor estará disponível em: `http://127.0.0.1:8000/`

## 📡 Endpoints da API

### GET `/`
Retorna uma mensagem de boas-vindas em JSON.

### GET `/home/`
Página inicial com informações sobre os endpoints disponíveis.

### GET `/contadores/`
Lista todos os contadores cadastrados.

**Resposta:**
```json
{
  "contadores": [
    {
      "id": 1,
      "nome": "Contador 1",
      "valor": 5,
      "criado_em": "2024-01-01T12:00:00Z"
    }
  ],
  "total": 1
}
```

### POST `/contadores/criar/`
Cria um novo contador.

**Body (JSON):**
```json
{
  "nome": "Meu Contador",
  "valor": 0
}
```

**Resposta:**
```json
{
  "id": 1,
  "nome": "Meu Contador",
  "valor": 0,
  "mensagem": "Contador criado com sucesso!"
}
```

### GET `/contadores/<id>/`
Retorna os detalhes de um contador específico.

### POST `/contadores/<id>/incrementar/`
Incrementa o valor de um contador em 1.

### DELETE `/contadores/<id>/`
Deleta um contador.

### GET `/estatisticas/`
Retorna estatísticas sobre os contadores (total, soma dos valores, maior contador).

### GET `/operacao-demorada/`
Simula uma operação assíncrona que demora 2 segundos.

##  Testando os Endpoints

### Usando curl:

```bash
# Listar contadores
curl http://127.0.0.1:8000/contadores/

# Criar contador
curl -X POST http://127.0.0.1:8000/contadores/criar/ \
  -H "Content-Type: application/json" \
  -d '{"nome": "Teste", "valor": 0}'

# Incrementar contador
curl -X POST http://127.0.0.1:8000/contadores/1/incrementar/

# Buscar contador
curl http://127.0.0.1:8000/contadores/1/

# Estatísticas
curl http://127.0.0.1:8000/estatisticas/
```

### Usando Python (requests):

```python
import requests

# Criar contador
response = requests.post(
    'http://127.0.0.1:8000/contadores/criar/',
    json={'nome': 'Meu Contador', 'valor': 0}
)
print(response.json())

# Listar contadores
response = requests.get('http://127.0.0.1:8000/contadores/')
print(response.json())
```

##  Conceitos de Views Assíncronas

### Views Assíncronas com Funções

```python
async def minha_view(request):
    await asyncio.sleep(0.1)  # Operação assíncrona
    return JsonResponse({'status': 'ok'})
```

### Views Assíncronas com Classes

```python
class MinhaView(View):
    async def get(self, request):
        # Lógica assíncrona
        return JsonResponse({'status': 'ok'})
```

### ORM Assíncrono

```python
# Buscar objeto
contador = await Contador.objects.aget(id=1)

# Criar objeto
contador = await Contador.objects.acreate(nome='Teste', valor=0)

# Salvar objeto
await contador.asave()

# Deletar objeto
await contador.adelete()

# Contar objetos
total = await Contador.objects.acount()

# Iterar sobre objetos
async for contador in Contador.objects.all():
    print(contador.nome)
```

## Modelo de Dados

O projeto inclui um modelo `Contador` com os seguintes campos:
- `nome`: Nome do contador (CharField)
- `valor`: Valor numérico (IntegerField)
- `criado_em`: Data de criação (DateTimeField, auto)
- `atualizado_em`: Data de atualização (DateTimeField, auto)

## Admin do Django

Acesse o painel administrativo em: `http://127.0.0.1:8000/admin/`

Use as credenciais do superusuário criado anteriormente.

##  Notas Importantes

- Views assíncronas funcionam melhor com servidores ASGI (como Daphne ou Uvicorn)
- Para produção, considere usar um servidor ASGI em vez do servidor de desenvolvimento padrão
- O ORM assíncrono está disponível desde o Django 4.1
- Algumas operações do ORM ainda não são totalmente assíncronas

## nTecnologias Utilizadas

- Django 5.0+
- Python 3.8+
- SQLite (banco de dados padrão)

