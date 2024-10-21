frase = str(input('Digite uma frase: ')).strip().upper()
# Separar as palavras da frase em uma lista
palavras = frase.split()
# Juntar as palavras sem o espaço
junto = ''.join(palavras)

inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

###### (SEM O for)
# inverso = junto[::-1]
# print(f'O inverso de {junto} é {inverso}')

if junto == inverso:
    print('É um palindromo')
else:
    print('Não é um palindromo')