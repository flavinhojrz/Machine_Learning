# Escreva um programa que leia uma string de até 20 
# caracteres e em seguida escreva se essa string representa uma placa válida ( “sim” ou “não” ). 
# Uma string é uma placa válida se contiver somente e na sequência: 3 letras maiúsculas, hífen e 4 dígitos numéricos.

import re

def verify_plate(plate):
    # Verificando se a placa tem essas caracteristicas
    if re.fullmatch(r'[A-Z]{3}-\d{4}', plate):
        return 'yes'
    else:
        return 'no'
    
plate = input("Enter plate: ")
print(verify_plate(plate))