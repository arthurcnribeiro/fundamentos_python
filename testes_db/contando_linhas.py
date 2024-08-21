def contar_linhas(arquivo):
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
            print(f"O arquivo '{arquivo}' possui {len(linhas)} linhas.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Por favor, verifique o nome e tente novamente.")

# Solicita o nome do arquivo ao usuário
arquivo_usuario = input("Digite o nome do arquivo (com a extensão): ")
contar_linhas(arquivo_usuario)
