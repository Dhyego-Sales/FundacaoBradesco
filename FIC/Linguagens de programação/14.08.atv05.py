qtdhoras = float(input('Informe a quantidade de horas realizada no mês: '))
salarioatual = float(input('Informe o valor da sua hora: '))

if qtdhoras > 160:
    salariobase = 160 * salarioatual
    extra = (((qtdhoras - 160) * salarioatual) * 1.5)
    salariototal = salariobase + extra
    print('Seu salário ficou um total de R$: ',salariototal)
else:
    salariobase = qtdhoras * salarioatual
    print('Seu salário ficou um total de R$: ',salariobase)







