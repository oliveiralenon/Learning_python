"""
Crie um programa que leia dois valores e mostre um menu
na tela:

[1]somar
[2]multiplicar
[3] maior
[4]novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada
caso.
"""

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
cod = 0
while cod != 5:
    print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa")
    cod = int(input('Digite a operação desejada: '))
    if cod == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif cod == 2:
        mult = n1 * n2
        print(f'{n1} x {n2} = {mult}')
    elif cod == 3:
        if n1 > n2:
            maior = n1
            menor = n2
        else:
            maior = n2
            menor = n1
        print(f' {maior} é maior que {menor}.')
    elif cod == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif cod == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Programa finalizado')
