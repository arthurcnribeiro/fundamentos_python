texto = input("")
VOGAIS = "AEIOUaeiou"
conta = 0
for letra in texto:
    if letra in VOGAIS:
        conta = conta + 1
print(f"""O número de vogais na string '{texto}' é: {conta}""")