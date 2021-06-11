n1 = input('Digite um valor: ')
print(type(n1))
# 1: Vai mostrar como string

n1 = int(input('Digite um valor: '))
print(type(n1))
# 2: Vai mostrar como número inteiro

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma vale', s)
# 3: Vai somar os dois números
# Pois foi especificado que n1 e n2 são números inteiros: n1 = int

n1 = input('Digite um valor: ')
n2 = input('Digite outro: ')
s = n1 + n2
print('A soma vale', s)
# 4: Vai concatenar os dois números
# Ou seja, juntar uma string à outra
# Pois não foi especificado nada sobre n1 e n2, ou seja, são strings por padrão.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre ', n1, 'e', n2, ' vale', s)
# 5: Vai somar os dois números e mostrar na resposta
# A soma entre n1 e n2 vale ...

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
# 6: Vai somar os dois números e mostrar na resposta
# Versão mais enxuta do código usando .FORMAT
# A soma entre uma máscara e outra máscara vale ...

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))
# 7: Vai somar os dois números e mostrar na resposta
# Versão mais enxuta do código usando .FORMAT
# E marcando 0, 1 e 2 para identificar cada máscara ...