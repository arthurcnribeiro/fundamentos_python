def converter_maiusculas(arquivo_entrada, arquivo_saida):

    try:
        with open(arquivo_entrada, 'r') as entrada:
            conteudo = entrada.read()  # Lê o conteúdo do arquivo de entrada

            # Substitui por maiúscula
            conteudo_convertido = conteudo.upper()

        with open(arquivo_saida, 'w') as saida:
            saida.write(conteudo_convertido)  # Escreve o conteúdo modificado no arquivo de saída

        print(f"O arquivo '{arquivo_saida}' foi criado com letras maiúsculas")

    except FileNotFoundError:
        print("Arquivo de entrada não encontrado. Por favor, verifique o nome e tente novamente.")


# Solicita o nome do arquivo de entrada e o nome do arquivo de saída ao usuário
arquivo_entrada = input("Digite o nome do arquivo de entrada (com a extensão): ")
arquivo_saida = input("Digite o nome do arquivo de saída (com a extensão): ")
converter_maiusculas(arquivo_entrada, arquivo_saida)