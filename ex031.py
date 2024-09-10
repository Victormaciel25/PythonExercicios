# 0,50 por km em viagens de até 200km
# 0,45 para viagens mais longas

dist = int(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {dist:.1f}km.')
resultado = int()
if dist <= 200:
    resultado = dist * 0.50
else:
    resultado = dist * 0.45
print(f'E o preço da sua passagem será de R${resultado:.2f}')