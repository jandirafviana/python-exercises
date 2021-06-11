print('=== DESAFIO 006 ===')
print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada:')

n = int(input('Digite um número:'))
print(f'O dobro de {n} é {n*2}, o triplo é {n*3} e a raiz quadrada é {n**(1/2):.2f}.')


n = int(input('Digite outro número: '))
dobro = n*2
triplo = n*3
raiz = n**(1/2)
print(f'O dobro de {n} é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz:.2f}.')
# Para que o programa force a execução do "meio" (1/2) primeiro ao invés da potência, a gente coloca entre parênteses.
# Porque os parênteses estão na ordem de precedência.
# Format é o método, do objeto que é a string.

n = int(input('Digite outro número: '))
dobro = n*2
triplo = n*3
raiz = pow(n, (1/2))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}.'.format(n, dobro, triplo, raiz))

# pow(power) - função de potência