"""
Escreva um programa que pergunte o salário de um funcionário
e calcule o valo do seu aumento.

Para salários superiores a R$ 1.250,00 cauclule um aumento
de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input('Digite seu salário: '))
if salario >= 1250:
    salario_total = salario * 1.1
    print(f'Seu salário é R$ {salario:.2f} e com o aumento de 10% ficará R$ {salario_total:.2f}')
else:
    salario_total = salario * 1.15
    print(f'Seu salário é R$ {salario:.2f} e com o aumento de 15% ficará R$ {salario_total:.2f}')
