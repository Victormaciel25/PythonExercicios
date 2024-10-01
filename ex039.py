from datetime import date

ano = int(input('Ano de nascimento: '))
hoje = date.today().year
alist =  hoje - ano
print(f'Quem nasceu em {ano} tem {alist} anos em 2024.')
x = 18 - alist
data = hoje + x
if alist <= 18:
 print(f'Ainda faltam {x} anos para o alistamento.')
 print(f'Seu alistamento será em {data}.')
else:
 print(f'Você ja passou da idade de alistamento.')

