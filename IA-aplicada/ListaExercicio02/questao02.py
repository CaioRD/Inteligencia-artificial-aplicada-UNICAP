# Desenvolver um algoritmo que leia a altura de 15 pessoas. 
# Este programa deverá calcular e mostrar :

# a. A menor altura do grupo;
# b. A maior altura do grupo;

def calcular_alturas():
    alturas = []

   
    for i in range(15):
        while True:
            try:
                altura = float(input(f"Digite a altura da pessoa {i + 1}: "))
                alturas.append(altura)
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

   
    menor_altura = min(alturas)
    maior_altura = max(alturas)

   
    print(f"A menor altura do grupo é: {menor_altura:.2f} metros")
    print(f"A maior altura do grupo é: {maior_altura:.2f} metros")


calcular_alturas()
