'''
Escreva um programa que solicite ao usuário
digitar dois números e verifique se o primeiro
número é divisível pelo segundo número.

'''

numero01 = int(input("Digite o primeiro numero"))
numero02 = int(input("Digite o segundo numero"))

if numero01 % numero02 == 0:
    print(f"Numero {numero01} é divisivel por {numero02}")
else:
    print("Número não é divisivel")