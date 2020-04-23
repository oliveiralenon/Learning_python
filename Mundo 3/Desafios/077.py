"""
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as duas vogais.
"""
palavras = ('sapo', 'abacaxi', 'teto', 'criança', 'senhora', 'adulto')
for t in palavras:
    print(f'A palavra {t} tem as vogais: ', end='')
    print(f'{"a " * t.count("a")}{"e " * t.count("e")}{"i " * t.count("i")}{"o " * t.count("o")}'
          f'{"u " * t.count("u")}')

"""
for palavras in p:
    if letra.lower() in 'aeiou':
        print(letra, end= ' ')
"""