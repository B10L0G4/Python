#Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

inteiroPrime = int(input('Digite o primeiro numero inteiro: '))
inteiroSecon= int(input('Digite o segubdo numero inteiro: '))
real = float(input('Digite um numero real: '))

produto = (inteiroPrime * 2) * (inteiroSecon / 2)
print('Produto do dobro do primeiro número com metade do segundo número', produto)

soma = (inteiroPrime * 3) + real
print('Soma do triplo do primeiro número com o terceiro número', soma)

cubo = real ** 3
print(f'Terceiro elevado ao cubo {cubo:.2f}')
