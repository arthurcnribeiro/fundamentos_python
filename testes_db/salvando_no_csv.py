import pandas as pd

# Especificando o caminho para o arquivo CSV
tabela_1 = "db/tabela_1.csv"# Lendo o arquivo CSV
dados = pd.read_csv(tabela_1, delimiter=";") #ler toda a tabela e mostrando o delimitador
print(dados)

#linhas_filtradas = dados[dados['fabricante'] == 'Honda']
#print(linhas_filtradas)
#linhas_filtradas.to_csv("db/tabela2.csv", index=False)