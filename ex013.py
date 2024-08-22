sal = float(input('Qual o salário do funcionário? R$'))
aut = sal * (15/100)
aumento = sal + aut
print(f'Um funcionário que ganhava R${sal}, com 15% de aumento, passa a receber R${aumento:.2f}')