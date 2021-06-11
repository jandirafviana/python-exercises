n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('A soma é {}'.format(n1+n2))
print( )

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
# , end= ' '    no final da linha não vai quebrar, vai aparecer a linha de baixo em seguida na mesma linha.
# \n    esse comando coloca tudo na mesma linha, mesmo tendo dois comandos print um abaixo do outro.
# 0 3f indica quantas casas decimais o número vai mostrar. 3 casas flutuantes.
print('A divisão inteira é {} e a potência é {}.'.format(di, e))
# :.3f (dois pontos, .3 casas flutuantes)
# Vídeo Python#07 aos 27:45

print( )
print(A soma é {}, o produto {}, a divisão {}, a divisão inteira {} e a potencia é {} (s, m, d, di, e.format')'
