''''
Escreva um programa que solicite ao usuário digitar um número
inteiro e verifique se ele é par ou ímpar.
'''

numero = int(input("Digite o número inteiro: "))

if numero % 2 == 0:
    print(numero, "é um numero par")
else:
    print(numero, "é um numero impar")