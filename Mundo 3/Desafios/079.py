"""
Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista. Caso o
número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados
em ordem crescente.
"""
v = list()
i = 0
while True:
    v.append(int(input('Digite um número: ')))
    if i > 0:
        while v.count(v[i]) > 1:
            v.pop()
            v.append(int(input('Digite um número que não seja repetido: ')))
        i += 1
    elif i == 0:
        i += 1
    cod = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    while cod not in "SN":
        cod = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if cod == 'N':
        break
print(sorted(v))
