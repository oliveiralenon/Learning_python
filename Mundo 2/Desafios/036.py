"""
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos anos
ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será
negado.
"""
valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Qual é o salário do comprador? R$ '))
anos = float(input('Pagará o empréstimo em quantos anos? '))
pag_mensal = valor_casa / (anos * 12)
if pag_mensal > salario * 0.3:
    print('Empréstimo negado!')
else:
    print('-' * 60)
    print(f'Empréstimo de R$ {valor_casa:.2f} cedido. \nDeverá ser pago em mensalidades de R${pag_mensal:.2f} no período de {anos * 12} meses.')
