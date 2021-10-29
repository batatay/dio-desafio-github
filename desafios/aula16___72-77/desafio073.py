#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Apenas os 5 primeiros colocados; b) Os últimos 4 colocados da tabela; c) Uma lista com os times em ordem alfabética; d) Em que posição na tabela está o time da Chapecoense.
times = ('Palmeiras', 'Bragantino', 'Atlético-MG', 'Fortaleza', 'Athletico-PR', 'Bahia', 'Fluminense', 'Flamengo', 'Santos', 'Atlético-GO', 'Ceará', 'Corinthians', 'Juventude', 'São Paulo', 'Internacional', 'América-MG', 'Sport', 'Cuiabá', 'Chapecoense', 'Grêmio')
print('=*=' * 20)
print('{:^60}'.format(' TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL: '))
print('=*=' * 20)
print(times)
print('=-=' * 20)
print(f'Os 5 primeiros colocados são: \n{times[0:5]}')
print('=-=' * 20)
print(f'Os últimos 4 colocados são: \n{times[-4:]}')
print('=-=' * 20)
print(f'Times em ordem alfabética: \n{sorted(times)}')
print('=-=' * 20)
print(f'O Chapecoense está na posição: {times.index("Chapecoense")+1}')