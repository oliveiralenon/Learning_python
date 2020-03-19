"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
IMC e msotre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 24: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 < imc <= 24:
    print('Você está no peso ideal.')
elif 24 < imc <= 30:
    print('Você está com sobrepeso.')
elif 30 < imc <= 40:
    print('Você está no estágio de obesidade.')
elif imc > 40:
    print('Você está com obesidade mórbida.')
