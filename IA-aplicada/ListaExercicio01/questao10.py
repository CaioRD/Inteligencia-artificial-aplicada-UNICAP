# #O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar
# uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura )2

# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo
# com a tabela abaixo.
# IMC em adultos Condição
# Abaixo de 18,5 Abaixo do peso
# Entre 18,5 e 25 Peso normal
# Entre 25 e 30 Acima do peso
# Acima de 30 obeso 

def calcula_imc():
    try:
        peso = float(input("Digite o peso em kg: "))
        altura = float(input("Digite a altura em metros (ex: 1.75): "))
    except ValueError:       
        print("Peso ou altura inválidos. Por favor, digite números válidos.")
        return
   
    if peso <= 0 or altura <= 0:
        print("Peso ou altura inválidos. Ambos devem ser maiores que zero.")
        return
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Condição: Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Condição: Peso normal")
    elif 25 <= imc < 30:
        print("Condição: Acima do peso")
    else:
        print("Condição: Obeso")


calcula_imc()
