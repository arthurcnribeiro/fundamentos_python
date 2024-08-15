"""Descrição
Escreva uma solução que informe se um determinado ano é bissexto. Um ano é considerado bissexto se ele for
divisível por 4. No entanto, anos que são divisíveis por 100 não são bissextos, a menos que também sejam
divisíveis por 400. Esta regra é usada para corrigir o calendário, de modo que ele fique em conformidade
com o ano solar.
REGRA:
Um ano é bissexto se:
1. Ele é divisível por 4 e não é divisível por 100.
2. Ou ele é divisível por 400."""

ano = int(input("Digite um Ano: "))
if ano % 4 == 0:
    print("SIM")
elif ano % 100 == 0 and ano % 400 == 0:
    print("SIM")
else:
    print("NÃO")