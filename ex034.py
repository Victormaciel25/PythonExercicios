sal = int(input('Qual é o salário do funcionário? R$'))
if sal >= 1250:
    newsal = sal + (sal * 0.10)  # 10% de aumento
else:
    newsal = sal + (sal * 0.15)  # 15% de aumento

print(f'Quem ganhava R${sal:.2f} passa a ganhar R${newsal:.2f}')
