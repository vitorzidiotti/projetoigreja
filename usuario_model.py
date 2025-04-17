from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    cpf: str
    email: str
    senha: str

class UsuarioLogin(BaseModel):
    email: str
    senha: str