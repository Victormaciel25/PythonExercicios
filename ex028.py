import random

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
quest = int(input('Em que número eu pensei? '))
numero = random.randint(0,5)
if numero == quest:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {numero} e não no {quest}.')
