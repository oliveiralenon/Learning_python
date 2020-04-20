"""
Interrompendo repetições while.

COMMAND -> BREAK

n = cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    cont += 1


n = s = 0
while True: # While true torna a repetição infinita
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}'}

"""