# Importando a classe necessárias
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chaves

# Criando uma instância da classe FastAPI
app = FastAPI()

# Adicionando um middleware à aplicação. Neste caso, é o CORSMiddleware que permite requisições cross-origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitindo qualquer origem
    allow_credentials=True,  # Permitindo cookies de sessão de qualquer origem
    allow_methods=["*"],  # Permitindo todos os métodos HTTP
    allow_headers=["*"],  # Permitindo todos os cabeçalhos HTTP
)

# Incluindo as rotas definidas no módulo chaves à aplicação
app.include_router(chaves.router)
