# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 \* ((F-32) / 9).

fahrenheitGraus = float(input('Qual a temperatura em graus fahrenheit hj? '))

celsius = (fahrenheitGraus - 32) / 1.8

print(f'A temperatura em graus Fahrenheit hoje é {fahrenheitGraus}F° '
      f'e sua temperatura equivalente em graus Celsius é {celsius:.1f}C°')
