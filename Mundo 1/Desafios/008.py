"""
Digite um programa que leia um valor em metros e o exiba convertido
em centímetros e milímetros.
"""
metro = float(input("Digite o valor em metros: "))
print("{0}m é igual a {1}cm e também é igual a {2}mm".format(metro, (metro*100), (metro*1000)))
