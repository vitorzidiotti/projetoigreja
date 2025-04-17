from fastapi import APIRouter, HTTPException
import bcrypt
from supabase import create_client, Client
from usuario_model import UsuarioCreate, UsuarioLogin

url = "https://qswnqzmikzxlvupvwxra.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFzd25xem1pa3p4bHZ1cHZ3eHJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ2NDIyOTEsImV4cCI6MjA2MDIxODI5MX0.3cB6bVGMDa5DyvRhTzNb9uBisLim-jtnCft4dkfQW9A"
supabase: Client = create_client(url, key)

router = APIRouter()

@router.post("/cadastrar")
async def cadastrar_usuario(usuario: UsuarioCreate):
    senha_criptografada = bcrypt.hashpw(usuario.senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    dados = {
        "nome": usuario.nome,
        "cpf": usuario.cpf,
        "email": usuario.email,
        "senha": senha_criptografada
    }
    try:
        res = supabase.table("tb_usuario").insert(dados).execute()
        return {"message": "Usuário cadastrado com sucesso!", "data": res.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao cadastrar usuário: {str(e)}")
@router.post("/login")
async def login_usuario(credenciais: UsuarioLogin):
    res = supabase.table("tb_usuario").select("*").eq("email", credenciais.email).execute()

    if not res.data:
        raise HTTPException(status_code=404, detail="Email não encontrado.")

    usuario = res.data[0]
    senha_valida = bcrypt.checkpw(credenciais.senha.encode('utf-8'), usuario['senha'].encode('utf-8'))

    if senha_valida:
        return {"message": f"Login bem-sucedido. Bem-vindo(a), {usuario['nome']}!"}
    else:
        raise HTTPException(status_code=400, detail="Senha incorreta.")
