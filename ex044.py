print('='*10,'LojasVictor','='*10)
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
num = int(input('Qual é a opção? '))

if num == 1:
    print(f'A vista fica {preco-(preco*0.1):.2f} com 10% de desconto.')
elif num == 2:
    print(f'A vista no cartão fica {preco-(preco*0.05):.2f} com 5% de desconto.')
elif num == 3:
    print(f'Em até 2x no cartão fica {preco:.2f}.')
elif num == 4:
    print(f'3x ou mais no cartão fica {preco+(preco*0.2):.2f} com 20% de juros.')
else:
    print('Você selecionou a opção errada, selecione um numero de 1 a 4.')

