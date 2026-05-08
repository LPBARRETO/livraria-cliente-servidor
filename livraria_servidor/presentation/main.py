from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.use_cases import LivrariaUseCases
from infrastructure.txt_repository import TXTLivroRepository

app = FastAPI()

# --- A MÁGICA DO CLIENTE-SERVIDOR (CORS) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite que qualquer Cliente (Front-end) acesse
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -------------------------------------------

repositorio_txt = TXTLivroRepository()
casos_de_uso = LivrariaUseCases(repositorio_txt)

@app.get("/catalogo")
async def ver_catalogo():
    return casos_de_uso.obter_catalogo()

@app.post("/checkout/{id_livro}")
async def comprar(id_livro: int):
    sucesso, mensagem = casos_de_uso.realizar_checkout(id_livro)
    return {"status": sucesso, "mensagem": mensagem}