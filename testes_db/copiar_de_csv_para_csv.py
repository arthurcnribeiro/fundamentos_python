import csv

# Nome do arquivo CSV existente
existing_csv = 'db/tabela_1.csv'

# Nome do arquivo CSV com os dados a serem copiados
new_csv = 'db/tabela2.csv'

# Abrir o arquivo existente no modo 'a' (append)
with open(existing_csv, 'a', newline='') as existing_file:
    writer = csv.writer(existing_file)

    # Abrir o arquivo com os novos dados no modo 'r' (read)
    with open(new_csv, 'r') as new_file:
        reader = csv.reader(new_file)

        # Iterar sobre as linhas e escrevê-las no arquivo existente
        for row in reader:
            writer.writerow(row)

