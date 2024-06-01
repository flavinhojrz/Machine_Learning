# Escreva um programa que leia uma string de até 20 
# caracteres e em seguida escreva se essa string representa uma placa válida ( “sim” ou “não” ). 
# Uma string é uma placa válida se contiver somente e na sequência: 3 letras maiúsculas, hífen e 4 dígitos numéricos.

def verifica_placa(placa):
    # Verifica o comprimento da placa
    if len(placa) != 8 or placa[3] != '-':
        return 'não'
    
    # Verifica as três primeiras letras
    for i in range(3):
        if not ('A' <= placa[i] <= 'Z'):
            return 'não'
    
    # Verifica os quatro últimos dígitos
    for i in range(4, 8):
        if not ('0' <= placa[i] <= '9'):
            return 'não'
    
    return 'sim'

# Testando a função
placa = input('Digite uma placa: ')
print(verifica_placa(placa))
