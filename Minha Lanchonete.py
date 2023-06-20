cont = 0
print("Bem vindo a Lanchonete do Jean Michel Bete")
print("********************Cardápio**************************")
print(" |  Código |        Descrição        |  Valor(em R$) |")
print(" |   100   |     Cachorro-Quente     |      9,00     |")
print(" |   101   |  Cachorro-Quente Duplo  |     11,00     |")
print(" |   102   |          X-Egg          |     12,00     |")
print(" |   103   |        X-Salada         |     13,00     |")
print(" |   104   |         X-Bacon         |     14,00     |")
print(" |   105   |         X-Tudo          |     17,00     |")
print(" |   200   |    Refrigerante Lata    |      5,00     |")
print(" |   201   |       Chá Gelado        |      4,00     |")
while True:
    codigo = int(input("Entre com o código desejado: "))
    if codigo == 100:
        cont = cont + 9 #cont guarda todos valores dos itens pedidos
        print("Você pediu um Cachorro-Quente no valor de R$9,00")
    elif codigo == 101:
        cont = cont + 11
        print("Você pediu um Cachorro-Quente Duplo no valor de R$11,00")
    elif codigo == 102:
        cont = cont + 12
        print("Você pediu um X-Egg no valor de R$12,00")
    elif codigo == 103:
        cont = cont + 13
        print("Você pediu um X-Salada no valor de R$13,00")
    elif codigo == 104:
        cont = cont + 14
        print("Você pediu um X-Bacon no valor de R$14,00")
    elif codigo == 105:
        cont = cont + 17
        print("Você pediu um X-Tudo no valor de R$17,00")
    elif codigo == 200:
        cont = cont + 5
        print("Você pediu um Refrigerante Lata no valor de R$5,00")
    elif codigo == 201:
        cont = cont + 4
        print("Você pediu um Chá Gelado no valor de R$4,00")
    else:
        print("Opção inválida")
        continue
        print ("O valor a ser pago está em: {:.f}".format(cont))
    resposta = int(input("Deseja pedir mais alguma coisa? \n 1 - Sim \n 0 - Não \n >> "))
    if resposta == 1:
        continue
    else:
        print("O valor total a ser pago é: R${:.2f}".format(cont))
        break
