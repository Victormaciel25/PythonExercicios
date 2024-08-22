# 60 reais por dia
# 0,15 centavos por km rodado

dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))

p1 = dias * 60
p2 = km * 0.15

print(f'O total a pagar é de R${p1 + p2:.2f}')