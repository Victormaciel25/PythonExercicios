speed = int(input('Qual é a velocidade atual do carro? '))

if speed <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = (speed - 80) * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')   