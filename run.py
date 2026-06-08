import os
import sys
import uvicorn

if __name__ == "__main__":
    print("Iniciando o servidor da Livraria...")

    # 1. Descobre o caminho exato e absoluto da pasta do servidor
    caminho_servidor = os.path.abspath("livraria_servidor")

    # 2. Força o Python a colocar essa pasta na lista prioritária de leitura
    sys.path.insert(0, caminho_servidor)
    os.chdir(caminho_servidor)

    # 3. Usa o host 0.0.0.0 para garantir que o Azure consiga expor o site para a internet
    uvicorn.run(
        "presentation.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=[caminho_servidor]  # Ajuda o clone do Uvicorn a não se perder
    )