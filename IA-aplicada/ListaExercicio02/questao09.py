# Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
# P.G. contendo 10 valores. 

def imprimir_pg():
    try:
        A = float(input("Digite o valor inicial A: "))
        R = float(input("Digite a razão R: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
        return

    print("\nSequência em Progressão Geométrica (P.G.):")
    for i in range(10):
        termo = A * (R ** i)
        print(f"Termo {i + 1}: {termo:.2f}")

imprimir_pg()
