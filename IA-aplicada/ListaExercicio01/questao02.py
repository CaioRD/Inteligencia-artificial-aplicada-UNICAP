#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos). 

nome = input("Digite o nome desejado: ")
sexo = input("Digite o sexo (m/f): ")
estado_civil = input("Digite o estado civil (solteiro/casado): ")

def cadastrar():
    
    while true:    
        if sexo != "m" and sexo != "f":
            print("Sexo inválido")
        if estado_civil != "solteiro" and estado_civil != "casado":
            print("Estado civil inválido")        
        break
    if sexo == "f" and estado_civil == "casado":
            tempo_casada = int(input("Digite o tempo de casada (anos): "))
            
    print("O nome escolhido foi: " , nome)
    print("O sexo de " , nome , " é " , sexo)
    print("O estado civil de " , nome , " é " , estado_civil)
    
    if tempo_casada == true:
        print("O tempo de casada de " , nome , " é " , tempo_casada)
    
cadastrar()