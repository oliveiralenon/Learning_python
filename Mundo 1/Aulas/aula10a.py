"""
Condições (if, else, elif)

----------------------------------------------------
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

---------------------------------------------------
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

"""

"""nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
if m >= 6:
    print('Parabéns, sua média foi boa.')
else:
    print('Sua média foi ruim, estude mais.')

# outra forma de fazer o if - else
# print('Parabéns' if m >= 6 else 'Estude mais!')
