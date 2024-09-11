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
        # Solicita o peso e a altura do usuário
        peso = float(input("Digite o peso em kg: "))
        altura = float(input("Digite a altura em metros (ex: 1.75): "))
    except ValueError:
        # Caso o usuário insira valores inválidos
        print("Peso ou altura inválidos. Por favor, digite números válidos.")
        return

    # Verifica se os valores são positivos
    if peso <= 0 or altura <= 0:
        print("Peso ou altura inválidos. Ambos devem ser maiores que zero.")
        return

    # Calcula o IMC
    imc = peso / (altura ** 2)
    
    # Exibe o IMC calculado
    print(f"Seu IMC é: {imc:.2f}")

    # Determina a condição de acordo com o IMC
    if imc < 18.5:
        print("Condição: Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Condição: Peso normal")
    elif 25 <= imc < 30:
        print("Condição: Acima do peso")
    else:
        print("Condição: Obeso")

# Chama a função para calcular o IMC
calcula_imc()
