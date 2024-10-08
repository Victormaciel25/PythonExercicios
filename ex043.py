peso = float(input('Qual é seu peso? (Kg) '))
altura = input('Qual é sua altura? (m) ').replace(",",".")
altura = float(altura)
imc = peso / altura ** 2

print(f'O IMC dessa pessoa é de {imc:.2f}')

if imc <= 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 < imc <= 25:
    print('Você está no PESO NORMAL')
elif 25 < imc <= 30:
    print('Você está com SOBREPESO')
elif 30 < imc <= 40:
    print('Você está com OBESIDADE')
elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA')

