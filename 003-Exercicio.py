'''
Escreva um programa que peça para o usuário digitar
uma senha e verifique se ela atende aos requisitos
de complexidade, como, pelo menos, 8 caracteres,
incluindo letras maiúsculas e minúsculas, números
e caracteres especiais...

'''

import re

while True:
    senha = input("Digite sua senha: ")
    if (len(senha) < 8 or 
        not re.search("[a-z]", senha) or 
        not re.search("[A-Z]", senha) or 
        not re.search("[0-9]", senha) or 
        not re.search("[!@#$%^&*()_+-={};':\"|,.<>/?~]", senha)):
        
        print("A senha deve ter pelo menos 8 caracteres e incluir letras maiúsculas, minúsculas, números e caracteres especiais.")
    else:
        print("Senha válida!")
        break