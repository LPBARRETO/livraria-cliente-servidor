import requests

# URL do seu Back-end rodando na nuvem
URL_PRODUCAO = "https://engsoft-cap8-lucas.azurewebsites.net/catalogo"


def testar_backend_online():
    print(f"Testando conexão com: {URL_PRODUCAO}")
    print("-" * 40)

    try:
        # Faz uma requisição GET para o servidor na nuvem
        resposta = requests.get(URL_PRODUCAO)

        # O código 200 significa "OK" na internet
        if resposta.status_code == 200:
            print("✅ SUCESSO! O Back-end está online e respondendo.")
            print("\nDados recebidos (Catálogo):")
            livros = resposta.json()
            for livro in livros:
                print(f" - {livro['titulo']} (R$ {livro['preco']})")
        else:
            print(f"❌ ERRO! O servidor retornou o status: {resposta.status_code}")

    except requests.exceptions.ConnectionError:
        print("❌ FALHA CRÍTICA! Não foi possível acessar o servidor. Verifique se o link está online.")


if __name__ == "__main__":
    testar_backend_online()