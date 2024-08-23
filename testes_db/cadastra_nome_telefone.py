def cadastrar_contatos():
    # Abrindo o arquivo para escrita (append mode, para não sobrescrever o arquivo se já existir)
    with open('db/contatos.txt', 'a', encoding='utf-8') as arquivo:
        while True:
            # Solicitando o nome ao usuário
            nome = input("Digite o nome (ou deixe em branco para sair): ")
            if nome == "":
                print("Cadastro finalizado.")
                break

            # Solicitando o telefone ao usuário
            telefone = input("Digite o telefone (ou '0' para finalizar): ")
            if telefone == '0':
                print("Cadastro finalizado.")
                break

            # Escrevendo os dados no arquivo
            arquivo.write(f"{nome}: {telefone}\n")
            print(f"Contato '{nome}' com telefone '{telefone}' cadastrado com sucesso.\n")


# Chamando a função para iniciar o cadastro
cadastrar_contatos()
