from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from fastapi.responses import FileResponse

from core.use_cases import LivrariaUseCases
from infrastructure.txt_repository import TXTLivroRepository

app = FastAPI()

# --- CONFIGURAÇÃO INTELIGENTE DE CAMINHOS ---
# 1. Descobre a pasta exata onde este arquivo (main.py) está: .../presentation
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# 2. Volta uma pasta para trás para chegar na raiz do servidor: .../livraria_servidor
DIRETORIO_RAIZ = os.path.dirname(DIRETORIO_ATUAL)

# 3. Aponta para a pasta static: .../livraria_servidor/static
CAMINHO_STATIC = os.path.join(DIRETORIO_RAIZ, "static")

# --- MONTANDO O FRONT-END ---
# Usa o caminho absoluto calculado acima
app.mount("/static", StaticFiles(directory=CAMINHO_STATIC), name="static")

@app.get("/")
async def read_index():
    # Entrega o index.html usando o mesmo caminho seguro
    return FileResponse(os.path.join(CAMINHO_STATIC, 'index.html'))

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