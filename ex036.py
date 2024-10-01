casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = float(casa/(anos * 12))
condicao = salario * 0.3

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}. ')
if prestacao >= condicao:
    print('Empréstimo não pode ser concedido!')
else:
    print('Empréstimo pode ser concedido!')