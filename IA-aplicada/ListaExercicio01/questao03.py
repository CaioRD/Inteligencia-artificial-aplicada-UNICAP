# Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar. 



while True:
    numero = int(input("Digite aqui o número desejado "))
    
    if(numero < 0 ):
     print("número inválido, tente novamente! ")
     continue    
    if(numero % 2 == 0):
        print(f"O número {numero} é par! ")
    else:
        print(f"O numero {numero} é ímpar ")
    break