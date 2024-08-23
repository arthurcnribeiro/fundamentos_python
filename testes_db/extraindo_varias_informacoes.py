from collections import Counter
import string


# Função para processar o arquivo
def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()

        # Número de caracteres
        num_caracteres = len(texto)

        # Número de linhas
        num_linhas = texto.count('\n') + 1

        # Número de palavras
        palavras = texto.split()
        num_palavras = len(palavras)

        # Frequência de cada letra (ignora diferenças entre maiúsculas e minúsculas)
        texto_limpo = texto.lower()
        letras = [char for char in texto_limpo if char in string.ascii_lowercase]
        frequencia_letras = Counter(letras)

        # Escreve os resultados
        with open('db/resultado.txt', 'w', encoding='utf-8') as resultado:
            resultado.write(f"Número de caracteres: {num_caracteres}\n")
            resultado.write(f"Número de linhas: {num_linhas}\n")
            resultado.write(f"Número de palavras: {num_palavras}\n")
            resultado.write("Frequência de cada letra:\n")
            for letra, frequencia in sorted(frequencia_letras.items()):
                resultado.write(f"{letra}: {frequencia}\n")


# Exemplo de uso
caminho_arquivo = 'db/texto_2.txt'  # Substitua pelo caminho do seu arquivo
processar_arquivo(caminho_arquivo)
