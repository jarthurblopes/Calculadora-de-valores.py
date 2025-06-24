valor = float(input('Digite o valor da compra: R$ ')) #INPUT DO USUÁRIO
print('''FORMAS DE PAGAMENTO:
[ 1 ] PIX / DINHEIRO
[ 2 ] DÉBITO
[ 3 ] 2X NO CRÉDITO
[ 4 ] 3X OU MAIS NO CRÉDITO. ''') #OPÇOES DO USUÁRIO
escolha = int(input('Qual é a sua opção?: '))
if escolha == 1:
    desconto = valor - (valor * 10 / 100) #SE A ESCOLHA FOR UM
    print('Pagando em pix ou dinheiro, você recebe 10% de desconto. \n Pagando no total R${:.2f}'.format(desconto))
elif escolha == 2:
    desconto = valor - (valor * 5 / 100) #SE A ESCOLHA FOR DOIS
    print('Pagando no débito, você recebe 5% de desconto. Pagando no total R$:{:.2f}'.format(desconto))
elif escolha == 3: #SE A ESCOLHA FOR 3
    print('Pagando em até 2X no cartão, o valor fica no total de R${:.2f}'.format(valor))
elif escolha == 4: #SE A ESCOLHA FOR 4
    juros = valor + (valor * 20 / 100)
    print('Pagando em 3x ou mais no cartão, o valor tem um acréscimo de 20%. \n Pagando no total R${:.2f}'.format(juros))
else: # SE ESCOLHER UM NÚMERO QUE NAO TENHA OPÇÃO
    print('Número inválido, tente novamente.')
