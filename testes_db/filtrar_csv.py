import pandas as pd

# Especificando o caminho para o arquivo CSV
tabela_1 = "db/tabela_1.csv"# Lendo o arquivo CSV
dados = pd.read_csv(tabela_1, delimiter=';') #ler toda a tabela
#dados = pd.read_csv(tabela_1, usecols=['nome_cliente', 'modelo'])#Ler apenas as colunas que você der o nome
#print(dados)
#***********************************************************
#print()
#colunas_especificas = dados[['nome_cliente', 'fabricante']]
#print(colunas_especificas)
#*************************************************************
#***************************************************************
linhas_filtradas = dados[dados['quilometragem'] <= 3000]
print(linhas_filtradas)

#print()
