"""
Crie um programa que leia o nome de uma cidade e diga se
ela começa ou não com o nome "SANTO".
"""
cidade = str(input('Digite o nome da cidade: '))
split = cidade.split()
santo = 'santo' in split[0].lower()
print(f'A cidade {cidade.title()} começa com o nome Santo? {santo}')

"""
#outra forma de fazer:


cidade = str(input('Em que cidade você nasceu?')).strip()  #strip() tira os espaços na frente
print(cid[:5].lower() == 'santo')

"""