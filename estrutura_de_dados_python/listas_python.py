"""frutas = ["laranja", "Limão", "Abacaxi", "Uva"] #[0] - [1] - [2]
frutas2 = [] #lista vazia
letras = list("abcdefgh")
numeros = list(range(10))
diversos = ["Ferrari", "F8", 42000000, 2020, 290, "São Paulo", True]
print(numeros)
print(frutas[1])
print(frutas[-1])
print(frutas[-3])"""
#*****************************************************************
"""matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0]) # traz a primeira linha completa, linha "0 zero"
print(matriz[0][0]) # primeira linha e primeira coluna
print(matriz[0][-1]) #primeira linha e última coluna
print(matriz[-1][-1]) # última linha e última coluna
print(matriz[1][1]) # segunda linha (1) e segunda coluna (1)"""
#******************************************************************
lista = ["p", "y", "t", "h", "o", "n"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])
#*****************************************************************
"""carros = ["Gol", "Celta", "Palio", "BMW"]
for carro in carros:
    print(carro)"""
""""carros = ["Gol", "Celta", "Palio", "BMW"]
for indice, carro in enumerate(carros): #indice é o contador
    print(f"{indice+1} : {carro}")"""
#****************************************************************
"""numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(sorted(pares), end=" ")
print()
print(sorted(impares), end=" ")"""
#******************************************
"""numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0] # FOR com parametros dentro da lista
impares = [numero for numero in numeros if numero % 2 == 1]
quadrado = [numero ** 2 for numero in numeros]
print(pares)
print(impares)
print(quadrado)"""
#********************************************
"""lista = []
lista.append(1) #armazenando o número 1 na lista
lista.append("Python") #armazenando string
lista.append([40, 30, 20]) # armazenando outra lista dentro da lista
lista2 = lista.copy()
print(lista)
lista.pop(0)
print(lista)
lista.clear()
print(lista)
print(lista2)"""
"""lista = [1, 2, 3, 1, 4, 1, 5, 6]
print(lista)
lista[7] = 1 #alterando o promeiro item da lista, item ZERO 0
print(lista)
contar = lista.count(1)
print(f"o número 1 aparece {contar} vezes")
lista.extend([99, 199, 299])
print(lista)
print(lista.index(199))# Acha o indce do número 199 na lista, na primeira ocorrenca caso tenha mais do que um
lista.pop(0) # POP EXCLUI DA LISTA PELO INDICE
print(lista)
lista.remove(299) #EXCLUI DA LISTA PELO NOME do objeto
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)"""




