print('=== DESAFIO 008 ===')
print('Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros:')

medida = float(input('Digite um valor em metros: '))
print(f'A medida de {medida}m equivale a {medida*100}cm e {medida *1000}mm')

print()
medida = float(input('Digite outro valor em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m corresponde a {cm:.0f}cm e {mm:.0f}mm')

print()
medida = float(input('Digite mais um valor em metros: '))
print(f'''A medida de {medida}m corresponde a
{medida/1000}km
{medida/100}hm
{medida/10}dam
{medida*10:.0f}dm
{medida*100:.0f}cm
{medida*1000:.0f}mm''')
