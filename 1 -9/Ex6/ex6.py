# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math




# area  = Math.PI * (raio * raio);

raio = float(input('Qual o raio do circulo? \n'))

area = math.pi * (raio * raio)

print(f'A area do circulo é {raio} e possui  {area:.2f} de area')
