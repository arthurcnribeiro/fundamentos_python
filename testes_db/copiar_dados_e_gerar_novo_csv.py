import csv

# Nome do arquivo CSV existente
existing_csv = 'db/tabela_1.csv'

# Nome do novo arquivo CSV a ser criado
new_csv = input("Digite o nome do novo arquivo (com extensão .csv): ")

# Abrir o arquivo existente no modo 'r' (read)
with open(existing_csv, 'r') as existing_file:
    reader = csv.reader(existing_file)

    # Abrir o novo arquivo no modo 'w' (write)
    with open(new_csv, 'w', newline='') as new_file:
        writer = csv.writer(new_file)

        # Copiar cada linha do arquivo existente para o novo arquivo
        for row in reader:
            writer.writerow(row)

print(f"Dados copiados com sucesso para {new_csv}")
