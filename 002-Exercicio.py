'''
Escreva um programa que peça para o usuário digitar
sua idade e verifique se ele é elegível para votar ou não.

'''

idade = int(input("Digite sua idade:"))

if idade >=18: 
    print("Você é elegivel para votar!")
else:
    print("Você não é elegivel para votar ainda.")