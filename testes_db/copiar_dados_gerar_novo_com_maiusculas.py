def juntar_arquivos(arquivo_1, arquivo_2, arquivo_3):

    try:
        with open(arquivo_1, 'r') as dados_1:
            conteudo_1 = dados_1.read()  # Lê o conteúdo do arquivo de entrada

        with open(arquivo_2, 'r') as dados_2:
            conteudo_2 = dados_2.read()

        with open(arquivo_3, 'w') as saida:
            saida.write(conteudo_1)  # Escreve o conteúdo modificado no arquivo de saída

        with open(arquivo_3, 'a') as saida:
            saida.write(conteudo_2)

        print(f"O arquivo 3 foi criado com sucesso!")

    except FileNotFoundError:
        print("Arquivo de entrada não encontrado. Por favor, verifique o nome e tente novamente.")


# Solicita o nome do arquivo de entrada e o nome do arquivo de saída ao usuário
arquivo_1 = input("Digite o nome do arquivo 1 (com a extensão): ")
arquivo_2 = input("Digite o nome do arquivo 2 (com a extensão): ")
arquivo_3 = input("Digite o nome do arquivo 3 (com a extensão): ")
juntar_arquivos(arquivo_1, arquivo_2, arquivo_3)