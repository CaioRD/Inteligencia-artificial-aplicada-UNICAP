# Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
# Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
# números lidos. O número que encerrará a leitura será zero.

def calcular_estatisticas():
    quantidade_pares = 0
    quantidade_impares = 0
    soma_pares = 0
    soma_geral = 0
    total_numeros = 0

    while True:
        try:
            numero = int(input("Digite um número positivo (ou 0 para parar): "))
            if numero == 0:
                break
            if numero < 0:
                print("Número negativo não é permitido. Por favor, digite um número positivo.")
                continue

            if numero % 2 == 0:
                quantidade_pares += 1
                soma_pares += numero
            else:
                quantidade_impares += 1
            
            soma_geral += numero
            total_numeros += 1
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    if total_numeros == 0:
        print("Nenhum número positivo foi inserido.")
        return

    media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
    media_geral = soma_geral / total_numeros

    print(f"\nQuantidade de números pares: {quantidade_pares}")
    print(f"Quantidade de números ímpares: {quantidade_impares}")
    print(f"Média dos valores pares: {media_pares:.2f}")
    print(f"Média geral dos números lidos: {media_geral:.2f}")

calcular_estatisticas()
