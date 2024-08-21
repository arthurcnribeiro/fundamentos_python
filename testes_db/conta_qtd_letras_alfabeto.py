def substituir_vogais(arquivo_entrada, arquivo_saida):
    vogais = 'aeiouAEIOU'  # Define as vogais, tanto maiúsculas quanto minúsculas

    try:
        with open(arquivo_entrada, 'r') as entrada:
            conteudo = entrada.read()  # Lê o conteúdo do arquivo de entrada

            # Substitui cada vogal por '*'
            conteudo_substituido = ''.join('*' if caractere in vogais else caractere for caractere in conteudo)

        with open(arquivo_saida, 'w') as saida:
            saida.write(conteudo_substituido)  # Escreve o conteúdo modificado no arquivo de saída

        print(f"O arquivo '{arquivo_saida}' foi criado com as vogais substituídas por '*'.")

    except FileNotFoundError:
        print("Arquivo de entrada não encontrado. Por favor, verifique o nome e tente novamente.")


# Solicita o nome do arquivo de entrada e o nome do arquivo de saída ao usuário
arquivo_entrada = input("Digite o nome do arquivo de entrada (com a extensão): ")
arquivo_saida = input("Digite o nome do arquivo de saída (com a extensão): ")
substituir_vogais(arquivo_entrada, arquivo_saida)
