# Importando a classe BaseModel do módulo pydantic
from pydantic import BaseModel

# Definindo uma classe Chave que herda de BaseModel
class Chave(BaseModel):
    nome: str  # Definindo um atributo nome do tipo string
    situacao: str  # Definindo um atributo situacao do tipo string
    status: str  # Definindo um atributo status do tipo string
