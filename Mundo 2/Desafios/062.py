"""
Melhore o desafio 061, perguntando para o usuário se ele
quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos.
"""
termo = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão da PA: '))
cod = 1
cont = 0
while cod != 0:
    if cont == 0:
        cod = int(input('Digite quantos termos da PA você deseja visualizar: '))
        cont += 1
    else:
        cod1 = cod
        cod = int(input('Você gostaria de adicionar mais quantos termos na PA (0 para fechar)? '))
        if cod != 0:
            cod = cod1 + cod
    for i in range(0, cod):
        pa = termo + (razao * i)
        print(pa, end=' -> ')
    print('Fim!')
    print('')



