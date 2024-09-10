#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo,
#imprimindo o resultado.

while True: 
    num = int(input("Digite um número: "))
    
    if num > 0:
        print(f"O dobro de {num} é {num * 2}")
    else:
        print(f"O triplo de {num} é {num * 3}")
        
    break