from pydantic import BaseModel

class EventoCreate(BaseModel):
    nome: str
    local: str

class EventoEdit(BaseModel):
    email: str
    senha: str