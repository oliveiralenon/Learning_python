"""
Crie um programa que o usuário digite uma expressão
matemática qualquer que use parênteses. Seu aplicativo
deverá analsiar se a expressão passada está com parênteses
abertos e fechados na ordem correta.
"""
from math import fabs
formula = str(input('Digite a fórmula: '))
list(formula)
colchetes1 = formula.count('[')
colchetes2 = formula.count(']')
parenteses1 = formula.count('(')
parenteses2 = formula.count(')')
chaves1 = formula.count('{')
chaves2 = formula.count('}')
if colchetes1 != colchetes2:
    print(f'Expressão {formula} está errada, existem {fabs(colchetes1 - colchetes2)} colchetes abertos.')
elif parenteses1 != parenteses2:
    print(f'Expressão {formula} está errada, existem {fabs(parenteses1 - parenteses2)} parênteses abertos.')
elif chaves1 != chaves2:
    print(f'Expressão {formula} está errada, existem {fabs(chaves1 - chaves2)} chaves abertas.')
else:
    print(f'A expressão {formula} está correta!')

"""
Resolução do guanabara:

expr = str(input('Digite a expressão'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')

"""
