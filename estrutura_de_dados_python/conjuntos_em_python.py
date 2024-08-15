"""conjunto1 = set([1, 2, 3, 1, 3, 4]) # SET ELIMINA REGISTRO DUPLICADOS
print(conjunto1)
conjunto2 = set("abacaxi") # SET ELIMINA REGISTRO DUPLICADOS
print(conjunto2)
for letras in conjunto2:
    print(letras, end=" ")"""
#**************************
"""conjunto_a = {1, 2}
conjunto_b = {3, 4}
conjunto_c = conjunto_a.union(conjunto_b) #Juntar os dois SETs
print(conjunto_c)"""
# ***************************
"""conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_c = conjunto_a.intersection(conjunto_b) # junta apenas os itens iguais dos SETS
print(conjunto_c)"""
#****************************
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_c = conjunto_a.difference(conjunto_b)
conjunto_d = conjunto_b.difference(conjunto_a)
conjunto_e = conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_c, conjunto_d, conjunto_e)