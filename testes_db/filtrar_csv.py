import pandas as pd

# Especificando o caminho para o arquivo CSV
tabela_2 = "db/tabela_2.csv" # Lendo o arquivo CSV
dados = pd.read_csv(tabela_2) #ler toda a tabela
#dados = pd.read_csv(tabela_1, usecols=['nome_cliente', 'modelo'])#Ler apenas as colunas que você der o nome
#print(dados)
#***********************************************************
#print()
#colunas_especificas = dados[['nome_cliente', 'fabricante']]
#print(colunas_especificas)
#*************************************************************
#***************************************************************
linhas_filtradas = dados[dados['Idade'] >= 10]
print(linhas_filtradas)

#print()
