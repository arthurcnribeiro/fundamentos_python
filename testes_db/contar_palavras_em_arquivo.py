def contar_palavra(arquivo_entrada, palavra_procurada):
    contagem = 0

    try:
        with open(arquivo_entrada, 'r') as arquivo:
            for linha in arquivo:
                # Divide a linha em palavras e conta quantas vezes a palavra_procurada aparece
                palavras = linha.split()
                contagem += palavras.count(palavra_procurada)

        print(f"A palavra '{palavra_procurada}' aparece {contagem} vezes no arquivo '{arquivo_entrada}'.")

    except FileNotFoundError:
        print("Arquivo não encontrado. Por favor, verifique o nome e tente novamente.")


# Solicita o nome do arquivo e a palavra a ser contada ao usuário
arquivo_entrada = input("Digite o nome do arquivo de entrada (com a extensão): ")
palavra_procurada = input("Digite a palavra que deseja contar: ")

contar_palavra(arquivo_entrada, palavra_procurada)