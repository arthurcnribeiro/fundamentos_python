def contar_letras(arquivo):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    contagem = {letra: 0 for letra in alfabeto}  # Inicializa o dicionário com contagem 0 para cada letra

    try:
        with open(arquivo, 'r') as file:
            conteudo = file.read().lower()  # Lê o conteúdo e converte tudo para minúsculas

            for caractere in conteudo:
                if caractere in contagem:  # Verifica se o caractere é uma letra do alfabeto
                    contagem[caractere] += 1  # Incrementa a contagem da letra correspondente

        # Exibe a contagem de cada letra
        for letra, qtd in contagem.items():
            print(f"A letra '{letra}' aparece {qtd} vezes.")

    except FileNotFoundError:
        print("Arquivo não encontrado. Por favor, verifique o nome e tente novamente.")


# Solicita o nome do arquivo ao usuário
arquivo_usuario = input("Digite o nome do arquivo (com a extensão): ")
contar_letras(arquivo_usuario)
