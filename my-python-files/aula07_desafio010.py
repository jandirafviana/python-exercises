print('=== DESAFIO 010 ===')
print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.\nConsidere: US$ 1.00 = R$ 3.27.')
print()
print('Olá, sou o conversor de moedas!')
BR = float(input('Quantos reais você possui na carteira? R$ '))
US = 3.27
CONV = BR / US
print(f'Com R$ {BR:.2f} reais, você pode comprar US$ {CONV:.2f} dólares, levando em conta a cotação do dólar a R$ {US} reais.')

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
print(f'Com R$ {real:.2f}, você pode comprar US$ {dolar:.2f} dólares')
