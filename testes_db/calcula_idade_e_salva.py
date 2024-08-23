from datetime import datetime


def calcular_idades(arquivo_entrada, arquivo_saida, data_atual):
    # Lendo o arquivo de entrada
    with open(arquivo_entrada, 'r', encoding='utf-8') as entrada:
        linhas = entrada.readlines()

    # Processando cada linha para calcular a idade
    with open(arquivo_saida, 'w', encoding='utf-8') as saida:
        for linha in linhas:
            nome, dia, mes, ano = linha.strip().split()
            dia, mes, ano = int(dia), int(mes), int(ano)

            # Convertendo data de nascimento em objeto datetime
            data_nascimento = datetime(ano, mes, dia)

            # Calculando a idade
            idade = data_atual.year - data_nascimento.year
            if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1

            # Escrevendo o nome e a idade no arquivo de saída
            saida.write(f"{nome}: {idade} anos\n")


def main():
    # Solicitando ao usuário o nome do arquivo de entrada
    arquivo_entrada = input("Digite o nome do arquivo de entrada: ")

    # Solicitando a data atual
    data_atual_input = input("Digite a data de hoje (DD MM AAAA): ")
    dia_atual, mes_atual, ano_atual = map(int, data_atual_input.split())
    data_atual = datetime(ano_atual, mes_atual, dia_atual)

    # Nome do arquivo de saída
    arquivo_saida = 'db/nome_idade.txt'

    # Calculando idades e gerando o arquivo de saída
    calcular_idades(arquivo_entrada, arquivo_saida, data_atual)
    print(f"Arquivo '{arquivo_saida}' foi criado com sucesso.")


# Executando o programa
main()
