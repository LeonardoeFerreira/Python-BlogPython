'''
Escreva um programa para pedir ao usuário 
digitar duas datas e determine qual é mais recente.

'''

from datetime import datetime


data01 = input("Digire a primeira data (DD/MM/AA): ")
data02 = input("digite a segunda data (DD/MM/AAA): ")


data01_obj = datetime.strptime(data01, "%d/%m/%Y")
data02_obj = datetime.strptime(data02, "%d/%m/%Y")


if data01_obj > data02_obj: 
    print("A primeira data é recente. ")
elif data02_obj > data01_obj:
    print("A segunda data é mais recente. ")
else: 
    print("As duas datas são iguais")