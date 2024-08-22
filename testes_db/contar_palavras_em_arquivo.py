def conta_palavra(arquivo):
    caracter = input("Digite o carater que deseja contar: ")

    try:
        with open(arquivo, 'r') as file:
            conteudo = file.read()  # Lê o conteúdo inteiro do arquivo
            total_palavra = 0

            for palavra in conteudo:
                if palavra in caracter: # Verifica se o caractere esta no arquivo
                    total_palavra += 1 # Incrementa a contagem total de caracter

        print(f"O total de palavras '{palavra}' é {total_palavra}.")

    except FileNotFoundError:
        print("Arquivo não encontrado. Por favor, verifique o nome e tente novamente.")

# Solicita o nome do arquivo ao usuário
arquivo_usuario = input("Digite o nome do arquivo (com a extensão): ")
conta_palavra(arquivo_usuario)