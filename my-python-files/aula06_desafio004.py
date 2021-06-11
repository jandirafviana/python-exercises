n1 = int(input ('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} é {}'.format(n1, n2, s))

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))

n = input('Digite algo: ')
# Esse 'n' que estamos analisando é um objeto. Em n.isnumeric por exemplo.
# Todo objeto tem características e realiza funcionalidade. Tem atributos e métodos.
# Todo objeto string tem métodos (isnumeric, isalnum)
# No caso desse código, como tem parênteses depois de cada objeto, a gente está trabalhando métodos.

print('{} É um número?'.format(n), n.isnumeric())
print('{} É alfanumérico?'.format(n), n.isalnum())
print('{} É uma letra do alfabeto?'.format(n), n.isalpha())
print('{} É um valor ASCII?'.format(n), n.isascii())
# Um valor ASCII é um valor entre 0 e 127.
print('{} É um número decimal?'.format(n), n.isdecimal())
print('{} É um digito?'.format(n), n.isdigit())
# Verifica se a string consiste apenas de digitos.
print('{} É um identificador?'.format(n), n.isidentifier())
# O isidentifier() retornará True se todos os caracteres são
# válidos para escrever um identificador no código, então eles
# são letras maiúsculas e minúsculas, dígitos, desde que não
# seja o primeiro caractere e mais alguns caracteres Unicode.
print('{} Está minúsculo?'.format(n), n.islower())
# Python string method islower() checks whether all the
# case-based characters (letters) of the string are lowercase.
print('{} Está maiúsculo?'.format(n), n.isupper())
print('{} É printável?'.format(n), n.isprintable())
# O isprintable() retornará True quando todos os caracteres são
# visíveis quando manda imprimi-los, isto incluindo os óbvios,
# mas também alguns menos óbvios como os que geram espaço em branco
# que não deixam de serem imprimíveis. Um exemplo de caractere não
# imprimível é o nulo (\0). Ele tem que ocupar espaço em tela ou papel.
# O mais comum de usá-lo é saber que se ele contará para determinar
# o espaço ocupado em um impressão qualquer em qualquer suporte
# ou se poderá causar algum erro por que criar uma situação
# inesperada, por exemplo um \8 que é um backspace, então ele pode
# retroceder uma caractere, então em vez de ocupar mais um caractere
# ele ocupa menos, apagando o anterior.
print('{} É um espaço?'.format(n), n.isspace())
# Python string method isspace() checks whether the string consists
# of whitespace.
print('{} Está capitalizada?'.format(n), n.istitle())
#Ou seja, primeira letra maiúscula.
print('{} É uma letra do alfabeto?'.format(n), n.__init_subclass__())

s = 'I Love Python.'
if s.isalnum() == True:
    print('É alfanumérico')
else:
    print('Não é alfanumérico')

s = 'Python'
if s.istitle() == True:
    print('Titlecased String')
else:
    print('Not a Titlecased String')

s = 'Eu adoro Python.'
if s.isupper() == True:
    print('A frase está em maiúsculo')
else:
    print('Não está em maiúsculo')
