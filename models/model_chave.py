from pydantic import BaseModel

class Chave(BaseModel):
    id: int
    nome: str
    situacao: str
    status: str