import os
import uvicorn

if __name__ == "__main__":
    print("Iniciando o servidor da Livraria...")

    # 1. O Python entra na pasta do servidor automaticamente por baixo dos panos
    os.chdir("livraria_servidor")

    # 2. Ele roda o uvicorn direto pelo código, sem precisar do terminal
    uvicorn.run("presentation.main:app", host="127.0.0.1", port=8000, reload=True)