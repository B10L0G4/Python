# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# lado * lado ^ 2

lado = float(input('Qual o lado do quadrado ? \n'))

area = lado ** 2
areaElevada = area * 2


print(f'O quadrado possui lado {lado} sua area é {area} e elevada ao quadrado ficara {areaElevada} ')