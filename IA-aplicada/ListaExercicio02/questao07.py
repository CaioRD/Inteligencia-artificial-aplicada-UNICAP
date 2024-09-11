# Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de
# N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N. 

def calcular_tabuada():
    while True:
        try:
            N = int(input("Digite um valor para N (de 1 a 10): "))
            if 1 <= N <= 10:
                break
            else:
                print("Por favor, digite um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    print(f"\nTabuada de {N}:")
    for i in range(11):
        resultado = i * N
        print(f"{i} x {N} = {resultado}")

calcular_tabuada()
