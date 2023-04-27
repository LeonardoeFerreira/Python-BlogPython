'''
Escreva um programa que solicite ao usuário digitar 
sua altura e peso e calcule seu índice de massa corporal (IMC).
Em seguida, verifique se ele está abaixo do peso, no peso normal ou acima do peso.
'''

altura = float(input("Digite sua altura em metros: "))
peso = float(input("digite seu peso em Kg: "))


imc = peso / (altura **2)

if imc < 18.5:
    print("Seu IMC é {:.2f}, você está abaixo do peso. ".format(imc))
elif imc >= 18.6 and imc <25:
    print("Seu IMC é {:.2f}, você está no peso normal.".format(imc))
else: 
    print("Seu IMC é {:.2f}, você está acima do peso.".format(imc))
    
     