# Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de
# A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 

def calcular_fatorial():
    try:
        A = int(input("Digite o valor para calcular o fatorial: "))
        if A < 0:
            print("O valor deve ser um número inteiro não negativo.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return

    fatorial = 1
    sequencia = []

    for i in range(A, 0, -1):
        fatorial *= i
        sequencia.append(str(i))
    
    sequencia_str = " X ".join(sequencia)
    print(f"\n{A}! = {' X '.join(sequencia)} = {fatorial}")

calcular_fatorial()
