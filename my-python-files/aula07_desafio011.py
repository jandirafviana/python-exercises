print('=== DESAFIO 011 ===')
print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área \ne a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²:')

L = float(input('Digite a largura da parede: '))
A = float(input('Digite a altura da parede: '))
ÁREA = L*A
LITROS = ÁREA / 2
print(f'Sua parede tem a dimensão de {L}m x {A}m e sua área é de {ÁREA}m². Para pintá-la, você irá precisar de {LITROS:.2f} litros de tinta.')

