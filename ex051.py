print('=' * 30)
print('     10 TERMOS DE UMA PA    ')
print('=' * 30)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
soma = 0

print(primeiro)
for c in range(1, 10):
    soma = soma + razao
    print(soma)
print('ACABOU')
