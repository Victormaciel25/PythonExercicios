import random

nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')

opcoes = [nome1, nome2, nome3, nome4]
sorteado = random.choice(opcoes)

print(f'O aluno escolhido foi {sorteado}')