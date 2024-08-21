def contar_vogais(arquivo):
    vogais = 'aeiouAEIOU'
    total_vogais = 0  # Variável para armazenar o total de vogais

    try:
        with open(arquivo, 'r') as file:
            conteudo = file.read()  # Lê o conteúdo inteiro do arquivo

            for caractere in conteudo:
                if caractere in vogais:  # Verifica se o caractere é uma vogal
                    total_vogais += 1  # Incrementa a contagem total de vogais

        print(f"O total de vogais no arquivo '{arquivo}' é {total_vogais}.")

    except FileNotFoundError:
        print("Arquivo não encontrado. Por favor, verifique o nome e tente novamente.")


# Solicita o nome do arquivo ao usuário
arquivo_usuario = input("Digite o nome do arquivo (com a extensão): ")
contar_vogais(arquivo_usuario)
