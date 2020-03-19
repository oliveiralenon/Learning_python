"""
Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar
um triângulo. Verifique também que tipo de triângulo será formado:

- Equilátero > Todos lados iguais
- Isósceles > 2 lados iguais
- Escaleno > Todos lados diferentes
"""
a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print(f'O triângulo de lados {a}, {b}, {c} é do tipo equilátero.')
    elif a != b != c != a:
        print(f'O triângulo de lados {a}, {b}, {c} é do tipo escaleno.')
    else:
        print(f'O triângulo de lados {a}, {b}, {c} é do tipo isósceles.')
else:
    print('Não é possível formar um triângulo com os lados informados.')
