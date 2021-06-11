print('=== DESAFIO 005 ===')
print('Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:')

n = int(input('Digite um número:'))
print(f'O sucessor de {n} é {n+1} e o antecessor de {n} é {n-1}.')
# Primeiro exemplo. Com o novo format.

n = int(input('Digite outro numero:'))
print('O sucessor de {} é {} e o antecessor de {} é {}.'.format(n, n+1, n, n-1))
# Segundo exemplo. Com o format antigo.

n = int(input('Digite outro numero:'))
s = n+1
a = n-1
print('O sucessor de {} é {} e o antecessor de {} é {}.'.format(n, s, n, a))
# Resposta do professor: Usando 3 variáveis (n, s, a). Dá pra fazer somente com uma variável, mas se eu precisar do sucessor e do antecessor
# lá na frente, o interessante é que eu guarde numa variável. Mas como eu quero mostrar o resultado e acabou o programa,
# dá pra colocar direto nos parênteses o n+1 e n-1 (substituindo as máscaras, assim como no terceiro exemplo).
# Com menos variáveis, você economiza mais memória.
