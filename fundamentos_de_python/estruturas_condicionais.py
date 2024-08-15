n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print(f"o número {n1} é maior que o número {n2}")
elif n1 == n2:
    print(f"o número {n1} é igual número {n2}")
else:
    print(f"o número {n2} é maior que o número {n1}")

"""saldo = 100
saque = 10
status = "Sucesso!" if saldo >= saque else "Sem Saldo" # SE saldo MAIOR IGUAL saque, Sucesso!!! Se não Sem saldo.
print(f"{status}, seu novo saldo é {saldo-saque}") #Imprime o resultado e o novo saldo"""

