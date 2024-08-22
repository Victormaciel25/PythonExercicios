p = float(input('Qual é o preço do produto? R$'))
x = float(input('Qual a porcentagem de desconto? '))
desconto = p * (x/100)
novo_preco = p - desconto
print(f'O produto que custava R${p:.2f}, na promoção com desconto de {x:.0f}% vai custar R${novo_preco:.2f}')