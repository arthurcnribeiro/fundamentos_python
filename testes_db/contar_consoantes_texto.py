def contar_vogais_consoantes(arquivo):
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vogais = 'aeiouAEIOU'
    total_consoantes = 0  # Variável para armazenar o total de vogais
    total_vogais = 0

    try:
        with open(arquivo, 'r') as file:
            conteudo = file.read()  # Lê o conteúdo inteiro do arquivo

            for caractere in conteudo:
                if caractere in consoantes:  # Verifica se o caractere é uma vogal
                    total_consoantes += 1  # Incrementa a contagem total de vogais
                if caractere in vogais:
                    total_vogais += 1

        print(f"O total de vogais no arquivo '{arquivo}' é {total_vogais}.")
        print(f"O total de consoantes no arquivo '{arquivo}' é {total_consoantes}.")


    except FileNotFoundError:
        print("Arquivo não encontrado. Por favor, verifique o nome e tente novamente.")


# Solicita o nome do arquivo ao usuário
arquivo_usuario = input("Digite o nome do arquivo (com a extensão): ")
contar_vogais_consoantes(arquivo_usuario)