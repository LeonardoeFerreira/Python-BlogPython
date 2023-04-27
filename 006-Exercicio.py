'''
Escreva um programa que solicite ao usuário digitar
um número e verifique se ele é positivo, negativo ou zero.

'''

numero =float(input("Digite"))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
    
else: 
    print(" O numero é zero")