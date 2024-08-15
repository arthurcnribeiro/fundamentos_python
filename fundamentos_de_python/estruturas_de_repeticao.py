"""texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()"""
#print(list(range(4)))
"""for numero in range(0, 51, 5):# start, range -1, de 5 em 5
    print(numero, end=" ")"""
"""opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n>>>: ))

    if opcao == 1:
        print("Sacando...")
    if opcao == 2:
        print("Exibindo Extrado...")"""

"""while True:
    opcao = int(input("Digite um número: "))

    if opcao == 10:
        break
    print(opcao)"""
#********************************
"""for numero in range(101):
    if numero % 2 == 1:
        continue
    print(numero, end=" ")"""
#********************************
"""carros = ["Gol", "Celta", "Palio", "BMW"]
for carro in carros:
    print(carro)"""
carros = ["Gol", "Celta", "Palio", "BMW"]
for indice, carro in enumerate(carros): #indice é o contador
    print(f"{indice+1} : {carro}")

