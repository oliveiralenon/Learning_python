"""
Crie um progrma que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas minúsculos
- Quantas letras ao todo (sem considerar espaços)
= Quantas letras tem o primeiro nome.
"""
nome = str(input('Digite seu nome completo: '))
separado = nome.split()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', ''))))
print(f'Seu primeiro nome é {separado[0]} e ele tem', len(separado[0]), 'letras')
