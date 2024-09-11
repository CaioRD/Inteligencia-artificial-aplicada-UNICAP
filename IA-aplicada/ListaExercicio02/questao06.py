#Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200. 

def gerar_impares():
    
    for numero in range(100, 201):
        if numero % 2 != 0:  # Verifica se o número é ímpar
            print(numero)

gerar_impares()
