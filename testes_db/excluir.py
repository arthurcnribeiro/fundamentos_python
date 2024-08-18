import csv

# Nome do arquivo CSV
nome_arquivo = "db/tabela_2.csv"

# Ler os dados existentes do arquivo CSV
with open(nome_arquivo, mode='r', newline='') as arquivo:
    leitor_csv = csv.reader(arquivo)
    dados = list(leitor_csv)  # Lê todos os dados como uma lista

# Exibir os dados lidos
print("Dados atuais:")
for i, linha in enumerate(dados, start=1):
    print(f"{i}: {linha}")

# Solicitar ao usuário qual linha deseja excluir
numero_linha = int(input("Digite o número da linha que deseja excluir: ")) - 1

# Verificar se o número da linha é válido e excluir a linha
if 0 <= numero_linha < len(dados):
    dados.pop(numero_linha)
    print(f"Linha {numero_linha + 1} excluída com sucesso.")
else:
    print("Número da linha inválido.")

# Reescrever o arquivo CSV com os dados restantes
with open(nome_arquivo, mode='w', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerows(dados)  # Escreve os dados restantes

print(f"Arquivo {nome_arquivo} atualizado.")
