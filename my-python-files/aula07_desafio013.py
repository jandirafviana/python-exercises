print('=== DESAFIO 013 ===')
print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento:')

salário = float(input('Digite seu salário atual: R$ '))
novo = float(salário + (salário * 15/100))
print(f'O seu novo salário com 15% de aumento é R$ {novo:.2f}')
print()
salário = float(input('Digite seu salário atual: R$ '))
print(f'O seu novo salário com 15% de aumento é R$ {salário * 1.15:.2f}')
