import pandas as pd

# Ler o arquivo CSV
df1 = pd.read_csv('db/tabela_1.csv', delimiter=";")
df2 = pd.read_csv('db/tabela_2.csv', delimiter=";")

# Passar a coluna 'nome' para MAIÚSCULA
#df1['modelo'] = df1['modelo'].str.upper()
# Passar a coluna 'nome' para minúscula
#df1['nome_cliente'] = df1['nome_cliente'].str.lower()

# Filtrar onde a coluna 'nome' é igual a 'JOÃO'
filtro_df1 = df1[df1['sexo'] == 'feminino']
print(filtro_df1)
filtro_df2 = df2[df2['sexo'] == 'masculino']
print(filtro_df2)

# Salvar os dados filtrados em um arquivo CSV já existente
filtro_df1.to_csv('db/tabela_4.csv', mode='w', index=False, header=True)
filtro_df2.to_csv('db/tabela_4.csv', mode='a', index=False, header=False)
