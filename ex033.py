valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
valor3 = int(input('Terceiro valor: '))

if valor1 < valor2 and valor3:
    print(f'O menor valor digitado foi {valor1}.')
elif valor2 < valor1 and valor3:
    print(f'O menor valor digitado foi {valor2}.')
elif valor3 < valor1 and valor2:
    print(f'O menor valor digitado foi {valor3}.')

if valor1 > valor2 and valor3:
    print(f'O maior valor digitado foi {valor1}.')
elif valor2 > valor1 and valor3:
    print(f'O maior valor digitado foi {valor2}.')
elif valor3 > valor1 and valor2:
    print(f'O maior valor digitado foi {valor3}.')