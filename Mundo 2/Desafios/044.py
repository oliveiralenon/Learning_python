"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque : 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros
"""
preco = float(input('Digite o preço do produto: R$ '))
print('Digite qual a forma de pagamento.\n1 - À vista dinheiro/cheque.\n2 - À vista no cartão.')
print('3 - Em 2x no cartão de crédito.\n4 - Em 3x ou mais no cartão de crédito.')
cod = int(input('Digite o código da forma de pagamento: '))
if cod == 1:
    print(f'Valor com desconto de 10% R$ {(preco * 0.9):.2f}')
elif cod == 2:
    print(f'Valor com desconto de 5% R$ {(preco * 0.95):.2f} ')
elif cod == 3:
    print(f'Valor em 2x sem juros: 2 x R$ {(preco / 2):.2f}')
elif cod == 4:
    parcelas = int(input('Digite em quantas parcelas você deseja pagar (de 3 - 12 parcelas): '))
    print(f'Valor em {parcelas} no cartão de crédito: {parcelas} x R$ {((preco * 1.2) / parcelas):.2f}')
else:
    print('\033[1;31mO código digitado não corresponde a uma opção de pagamento.\033[m')
