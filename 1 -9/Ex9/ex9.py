# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius e o inverso .
# C = 5 \* ((F-32) / 9).


tipoF= input('Você deseja converter qual tipo de temperatura ? \n Para Fahreheit digite f: \n Para Celsius digite c:\n')

if tipoF == 'f' :
      graus = float(input('Qual a temperatura \n'))
      celsius = (graus - 32) / 1.8
      print(f'A temperatura em graus Fahrenheit hoje é {graus}F°'
            f' e sua temperatura equivalente em graus Celsius é {celsius:.1f}C°')
else:
      graus = float(input('Qual a temperatura \n'))
      fahrenheit = (graus * 1.8 ) + 32
      print(f'A temperatura em graus Celsius é  hoje é {graus}F° '
            f'e sua temperatura equivalente em graus Fahrenheit é {fahrenheit:.1f}f°')
