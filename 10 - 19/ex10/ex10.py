# Faça um Programa que verifique se uma letra digitada
# é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite o sexo biologico: ")

letra = letra.upper()

if letra == "F":
    print("Feminino")
else:
    if letra == "M":
        print("Masculino")
    else:
        print("Sexo Inválido")

