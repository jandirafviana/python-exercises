#CURSO DE PYTHON - AULA 7: OPERAÇÕES ARITMÉTICOS
#  + Adição
#  - Subtração
#  * Multiplicaação
#  / Divisão
#  ** Potência
#  // Divisão inteira
#  % Resto da divisão

#  Operador binário = Operador que precisa de 2 operandos

# Operadores aritméticos podem ser usados como string.

print('='*20)
# Vai mostrar o '=' 20 vezes

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print('- Vai aparecer o nome normal.')
print( )

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {:20}!'.format(nome))
print('- Vai aparecer o nome dentro de 20 espaços. E a exclamação no final.')
# O nome foi escrito dentro de 20 espaços.
# Ex: Jan - 3 caracteres pro nome e 17 espaços.
print( )

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {:>20}!'.format(nome))
print('- Com o sinal de "maior" o nome aparece alinhado à direita.')
# Se colocar um sinal de maior, eu faço um alinhamento
# à direita em 20 espaços. Colocando um sinal de menor,
# fica alinhado à esquerda:
print( )

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {:<20}!'.format(nome))
print('- Com o sinal de menor, o nome aparece alinhado à esquerda.')
print( )

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {:^20}!'.format(nome))
print('Agora o nome aparece centralizado, dentro de 20 espaços.')
print( )

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {:=^20}!'.format(nome))
print('Agora o nome aparece centralizado, dentro de 20 espaços e com os iguais em volta.')
print( )
