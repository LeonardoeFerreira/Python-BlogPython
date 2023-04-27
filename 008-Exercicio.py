'''
Escreva um programa que solicite ao usuário 
digitar um número e verifique se ele é divisível por 3 e 5.
'''

numero = int(input("Digite um numero:"))

if numero % 3 == 0 and numero % 5 == 0: 
    print("O número é divisivel por 3 e 5.")
else: 
    print("O número não é dividido por 3 e 5 ")