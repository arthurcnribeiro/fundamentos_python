import csv

# Solicita os dados do usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Nome do arquivo CSV
nome_arquivo = "db/tabela_2.csv"

# Abre o arquivo em modo de escrita (write mode)
with open(nome_arquivo, mode='a', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)

    # Escreve o cabeçalho (opcional)
    # escritor_csv.writerow(["Nome", "Idade"])

    # Escreve os dados do usuário
    escritor_csv.writerow([nome, idade])

print(f"Dados salvos no arquivo {nome_arquivo}.")
