#atividade 04 ><
print('Segue abaixo valor da Maçã:\n 01 unidade: R$1,30 \n Acima de 11 unidades: R$1,00')
qtdmaça = int(input('Digite a quantidade de maçãs desejada: '))

if qtdmaça >= 12:
    qtdmaça = 1.0 * qtdmaça
    print('O valor da compra foi: ',qtdmaça)
else:
    qtdmaça = 1.30 * qtdmaça
    print('O valor da compra foi de: ',qtdmaça)




