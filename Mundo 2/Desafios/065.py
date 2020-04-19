"""

Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e menor valores lidos. O pro-
grama deve perguntar ao usuário se ele quer ou não continuar
a digitar valores.

"""

num = int(input('Digite um número inteiro: '))
cod = "S"
soma = num
cont = 1
maior = num
menor = num
while cod == 'S':
    cod = str(input('Você gostaria de inserir mais números [S/N]? ')).upper()
    if cod == 'S':
        num = int(input('Digite um número inteiro: '))
        soma += num
        cont += 1
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(f'A média entre os números é: {soma / cont:.2f}\nO maior número digitado foi o {maior}\nO menor número digitado foi o {menor}')