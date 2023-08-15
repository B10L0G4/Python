#  Faça um Programa que pergunte quanto você ganha por hora
#  e o número de horas trabalhadas no mês.
#  Calcule e mostre o total do seu salário no referido mês.

horaTrabalhoDia = float(input('Quantas horas vc trabalha por dia ?\n '))
horaTrabalhoMes = float(input('Quantas horas vc trabalhou este mês ?\n '))
valorHora = float(input('Quanto é sua hora de trabalho?\n '))

salarioDia = valorHora * horaTrabalhoDia
salarioMes = valorHora * horaTrabalhoMes

print(f'Seu salario por hora é {valorHora}, hoje vc trabalhou {horaTrabalhoDia} e seu salario do dia é {salarioDia}')
print(f'Este mês seu salario será {salarioMes}')
