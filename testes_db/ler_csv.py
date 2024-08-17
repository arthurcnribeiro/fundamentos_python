import pandas as pd

# Especificando o caminho para o arquivo CSV
tabela_1 = "db/tabela_1.csv"# Lendo o arquivo CSV
dados = pd.read_csv(tabela_1) #ler toda a tabela
#dados = pd.read_csv(tabela_1, usecols=['nome_cliente', 'modelo'])#Ler apenas as colunas que você der o nome

print(dados)
# Mostrando as primeiras linhas do DataFrame