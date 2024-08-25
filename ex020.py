import random
opcoes = [input(f'Aluno {i+1}: ') for i in range(4)]
random.shuffle(opcoes)
print(f'A ordem de apresentação é {opcoes}')