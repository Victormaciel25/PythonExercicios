frase = input('Digite uma frase: ').upper().strip()
quantidade_a = frase.count('A')
posicao_a = frase.find('A')
ultima_posicao_a = frase.rfind('A')

print(f'A letra "A" aparece {quantidade_a} vezes na frase.')

if posicao_a != -1:
    print(f"A primeira letra 'A' aparece na posição {posicao_a + 1}.")
else:
    print("A letra primeira letra 'A' não foi encontrada na frase.")

if ultima_posicao_a != -1:
    print(f"A última letra 'A' aparece na posição {ultima_posicao_a + 1}.")
else:
    print("A letra ultima letra 'A' não foi encontrada na frase.")