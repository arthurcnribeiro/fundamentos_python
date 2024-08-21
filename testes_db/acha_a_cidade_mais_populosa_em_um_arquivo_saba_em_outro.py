def cidade_mais_populosa(arquivo_entrada, arquivo_saida):
    cidade_mais_populosa = ""
    maior_populacao = 0

    try:
        with open(arquivo_entrada, 'r') as entrada:
            for linha in entrada:
                # Extrai o nome da cidade e o número de habitantes
                cidade = linha[:40].strip()  # Nome da cidade (40 caracteres)
                populacao = int(linha[40:].strip())  # Número de habitantes

                # Verifica se essa cidade tem a maior população até agora
                if populacao > maior_populacao:
                    cidade_mais_populosa = cidade
                    maior_populacao = populacao

        # Escreve a cidade mais populosa no arquivo de saída
        with open(arquivo_saida, 'w') as saida:
            saida.write(f"{cidade_mais_populosa} {maior_populacao}\n")

        print(f"O arquivo '{arquivo_saida}' foi criado com a cidade mais populosa.")

    except FileNotFoundError:
        print("Arquivo de entrada não encontrado. Por favor, verifique o nome e tente novamente.")
    except ValueError:
        print("Erro ao processar os dados. Verifique se o formato do arquivo de entrada está correto.")


# Solicita o nome do arquivo de entrada e do arquivo de saída ao usuário
arquivo_entrada = input("Digite o nome do arquivo de entrada (com a extensão): ")
arquivo_saida = input("Digite o nome do arquivo de saída (com a extensão): ")

cidade_mais_populosa(arquivo_entrada, arquivo_saida)
