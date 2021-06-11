n = str(input('Digite um valor: '))
print(n)
# Independente de especificar que é str,
# naturalmente é string

n = input('Digite um valor: ')
print(type(n))
# Como exemplificado acima

n = float(input('Digite um valor: '))
print(n)
# Número com ponto flutuante. Vai aparecer um número real.

n = bool(input('Digite um valor: '))
print(type(n))
# Valor boleano. Vai mostrar que é um valor lógico, ou seja, boleano. <class 'bool'>

n = bool(input('Digite um valor: '))
print(n)
# Valor boleano. Vai aparecer True.

n = input('Digite algo: ')
print(n.isnumeric())
# Pergunta se o que foi digitado é boleano