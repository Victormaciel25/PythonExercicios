nome = str(input('Digite seu nome completo: ').strip())
primeiro_nome = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {primeiro_nome[0]}')
print(f'Seu último nome é {primeiro_nome[len(primeiro_nome)-1]}')

