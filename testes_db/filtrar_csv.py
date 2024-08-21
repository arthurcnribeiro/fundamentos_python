import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('db/tabela_1.csv', delimiter=";")

# Passar a coluna 'nome' para maiúscula
df['modelo'] = df['modelo'].str.upper()
df['nome_cliente'] = df['nome_cliente'].str.lower()

# Filtrar onde a coluna 'nome' é igual a 'JOÃO'
filtro = df[df['modelo'].str.contains("CIVIC")]
print(filtro)

# Salvar os dados filtrados em um arquivo CSV já existente
filtro.to_csv('db/tabela_3.csv', mode='w', index=False, header=True)