"""
Faça um programa que leia algo pelo teclado e mostra
na tela o seu tipo primitivo e todas as informações
possíveis sobre ele.
"""
algo = input("Digite algo: ")
print("Tipo: ", type(algo))
print("É maiúsculo?", algo.isupper())
print("É minúsculo?", algo.islower())
print('É numérico?', algo.isalnum())
print('É alpha?', algo.isalpha())
print('É alpha numérico?', algo.isalnum())
