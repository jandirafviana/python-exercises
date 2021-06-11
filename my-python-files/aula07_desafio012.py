print('=== DESAFIO 012 ===')
print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto:')

preço = float(input('Digite o valor do produto: R$ '))
novo = float(preço - (preço * 5/100))
print(f'O preço do produto com 5% de desconto é R$ {novo:.2f}')

preço = float(input('Digite o valor do produto: R$ '))
print(f'O preço do produto com 5% de desconto é R$ {preço * 0.95:.2f}')

# O símbolo "%" no Python é usado como resto da divisão.

# Equação:
# R$ 10 ---- 100%
# X -------- 5%
# 10* 5/100
# = 0.5 (ou seja, 5% de 10)

# 1500*10/100
# = 150.0 (10% de 1.500 é 150)

# 875*15/100
# 131.25 (15% de 875 é 131.25)

