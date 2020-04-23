"""
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da Chapecoense.
"""
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético Paranaense',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético MG', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro MG', 'CSA', 'Chapecoense', 'Avaí')
print('Os primeiros cinco colocados do campeonato brasileiro 2019 foram: ', end='')
for cont in range(0, 5):  # ou... print(f'Os 5 primeiros times foram: {times[0:5]})
    print(f'{cont + 1}º', times[cont], end=', ' if cont < 6 else '.')
print('\nOs últimos colocados na tabela do brasileirão 2019 foram: ', end='')
for cont in range(-4, 0):
    print(f'{21 + cont}º', times[cont], end=', ')
print('\nTimes em ordem alfabética:', sorted(times))
print(f'A Chapecoense terminou o campeonato na posição', times.index('Chapecoense') + 1, 'º.')
