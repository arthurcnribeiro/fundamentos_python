def conta_caracter(arquivo):
    caracter = input("Digite o carater que deseja contar: ")

    try:
        with open(arquivo, 'r') as file:
            conteudo = file.read()  # Lê o conteúdo inteiro do arquivo
            total_caracter = 0

            for letra in conteudo:
                if letra in caracter: # Verifica se o caractere esta no arquivo
                    total_caracter += 1 # Incrementa a contagem total de caracter

        print(f"O total de letras '{caracter}' é {total_caracter}.")

    except FileNotFoundError:
        print("Arquivo não encontrado. Por favor, verifique o nome e tente novamente.")

# Solicita o nome do arquivo ao usuário
arquivo_usuario = input("Digite o nome do arquivo (com a extensão): ")
conta_caracter(arquivo_usuario)