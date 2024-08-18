import pandas as pd

# Nome do arquivo CSV existente
csv_file = 'db/tabela_2.csv'

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv(csv_file, delimiter=";")

# Exibir as colunas disponíveis para ordenar
print("Colunas disponíveis para ordenação:", df.columns.tolist())

# Solicitar ao usuário para escolher a coluna para ordenação
column_name = input("Digite o nome da coluna pela qual deseja ordenar: ")

# Ordenar o DataFrame pela coluna escolhida
df_sorted = df.sort_values(by=column_name)

# Nome do novo arquivo CSV a ser criado (opcional)
new_csv_file = input("Digite o nome do novo arquivo (com extensão .csv) para salvar os dados ordenados: ")

# Salvar o DataFrame ordenado em um novo arquivo CSV
df_sorted.to_csv(new_csv_file, index=False)

print(f"Dados ordenados pela coluna '{column_name}' e salvos em '{new_csv_file}' com sucesso!")
