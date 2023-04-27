'''
Escreva um programa que solicite ao usuário digitar
uma letra e verifique se ela é uma vogal ou uma consoante.
'''

letra = input("Digite uma letra: ")

if letra in 'aeiouAEIOU':
    print("A letra digitada é uma Vogal. ")
else: 
    print("A letra digitada é uma consoante.")