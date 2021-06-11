print('=== DESAFIO 009 ===')
print('Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada:')

n = int(input('Digite um número inteiro qualquer e veja a sua tabuada: '))
print(f'ADIÇÃO:\n {n} + 0 = {n+0} \n {n} + 1 = {n+1} \n {n} + 2 = {n+2} \n {n} + 3 = {n+3} \n {n} + 4 = {n+4} \n {n} + 5 = {n+5} \n {n} + 6 = {n+6} \n {n} + 7 = {n+7} \n {n} + 8 = {n+8} \n {n} + 9 = {n+9} ')
print('-' * 12)
print(f'SUBTRAÇÃO:\n {n} - 0 = {n-0} \n {n} - 1 = {n-1} \n {n} - 2 = {n-2} \n {n} - 3 = {n-3} \n {n} - 4 = {n-4} \n {n} - 5 = {n-5} \n {n} - 6 = {n-6} \n {n} - 7 = {n-7} \n {n} - 8 = {n-8} \n {n} - 9 = {n-9} ')
print('-' * 12)
print(f'MULTIPLICAÇÃO:\n {n} x 0 = {n*0} \n {n} x 1 = {n*1} \n {n} x 2 = {n*2} \n {n} x 3 = {n*3} \n {n} x 4 = {n*4} \n {n} x 5 = {n*5} \n {n} x 6 = {n*6} \n {n} x 7 = {n*7} \n {n} x 8 = {n*8} \n {n} x 9 = {n*9} ')
print('-' * 12)
print(f'DIVISÃO:\n {n} ÷ 1 = {n/1} \n {n} ÷ 2 = {n/2} \n {n} ÷ 3 = {n/3} \n {n} ÷ 4 = {n/4} \n {n} ÷ 5 = {n/5} \n {n} ÷ 6 = {n/6} \n {n} ÷ 7 = {n/7} \n {n} ÷ 8 = {n/8} \n {n} ÷ 9 = {n/9} ')
print()

n = int(input('Digite um número qualquer e veja sua tabuada: '))
print(f'''MULTIPLICAÇÃO:
{n} x {0:2} = {n*0}
{n} x {1:2} = {n*1}
{n} x {2:2} = {n*2}
{n} x {3:2} = {n*3}
{n} x {4:2} = {n*4}
{n} x {5:2} = {n*5}
{n} x {6:2} = {n*6}
{n} x {7:2} = {n*7}
{n} x {8:2} = {n*8}
{n} x {9:2} = {n*9}
{n} x {10:2} = {n*10}
''')
# Esse ":2" é para que o segundo número mostre 2 casas alinhadas.
