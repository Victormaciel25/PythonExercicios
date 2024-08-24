import random
opcoes = [input(f'Aluno {i+1}: ') for i in range(4)]
sorteado = random.choice(opcoes)
print(f'O aluno escolhido foi {sorteado}')
