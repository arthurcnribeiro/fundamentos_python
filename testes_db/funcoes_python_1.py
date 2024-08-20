"""nome = input("Digite o seu nome: ")
idade = int(input(f"Digite sua idade {nome}: "))
def exibir_nome_idade(nome): # inicia o bloco da função com parametro nome
    if idade >= 18:
        print(f"Olá {nome}, você tem {idade} anos e é MAIOR de idade!")
    else:
        print(f"Olá {nome}, você tem {idade} anos e é MENOR de idade!")
exibir_nome_idade(nome) #chama a função"""
# **************************************************************************
"""numeros = 10, 20, 34
def calcula_total(numeros):
    return sum(numeros)
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1
    return antecessor, sucessor
print(calcula_total(numeros))
print(retorna_antecessor_e_sucessor(10))"""
# **********************************************
"""
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
salvar_carro("Fiat", "Palio",1999,"ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")"""


# ************************************************
def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    menssagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(menssagem)

exibir_poema("Segunda, 19 de Agosto de 2024", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)
