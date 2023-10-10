from pydantic import BaseModel

class Chave(BaseModel):
    nome: str
    situacao: str
    status: str