# Média abaixo de 5.0 reprovado
# Média entre 5.0 e 6.9 recuperação
# Média 7.0 ou superior aprovação

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2 
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media}.')

if media < 5:
    print('O aluno está REPROVADO')
elif media >= 5 and media <= 6.9:
    print('O aluno está de RECUPERAÇÃO')
elif media >= 7:
    print('O aluno está APROVADO')