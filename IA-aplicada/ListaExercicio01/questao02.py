#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos). 


def cadastrar():
    while True:
        nome = input("Digite o nome desejado: ")
        sexo = input("Digite o sexo (m/f): ").lower()
        estado_civil = input("Digite o estado civil (solteiro/casado): ").lower()

        if sexo != "m" and sexo != "f":
            print("Sexo inválido. Por favor, digite novamente.")
            continue  

        if estado_civil != "solteiro" and estado_civil != "casado":
            print("Estado civil inválido. Por favor, digite novamente.")
            continue  
        
        if sexo == "f" and estado_civil == "casado":
            tempo_casada = int(input("Digite o tempo de casada (anos): "))
        else:
            tempo_casada = None

        print("O nome escolhido foi:", nome)
        print("O sexo de", nome, "é", sexo)
        print("O estado civil de", nome, "é", estado_civil)

        if tempo_casada is not None:
            print("O tempo de casada de", nome, "é", tempo_casada, "anos")
        
        break  

cadastrar()