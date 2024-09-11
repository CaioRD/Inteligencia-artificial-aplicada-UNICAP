# Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
# média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
# negativos e o percentual de valores negativos e positivos

def analisar_valores():
    soma_valores = 0
    quantidade_positivos = 0
    quantidade_negativos = 0
    total_valores = 0
    
    while True:
        try:
            valor = float(input("Digite um valor (ou 0 para parar): "))
            if valor == 0:
                break
            
            soma_valores += valor
            total_valores += 1
            
            if valor > 0:
                quantidade_positivos += 1
            elif valor < 0:
                quantidade_negativos += 1
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    
    if total_valores == 0:
        print("Nenhum valor foi inserido.")
        return

    media = soma_valores / total_valores
    percentual_positivos = (quantidade_positivos / total_valores) * 100
    percentual_negativos = (quantidade_negativos / total_valores) * 100

    print(f"\nMédia aritmética dos valores lidos: {media:.2f}")
    print(f"Quantidade de valores positivos: {quantidade_positivos}")
    print(f"Quantidade de valores negativos: {quantidade_negativos}")
    print(f"Percentual de valores positivos: {percentual_positivos:.2f}%")
    print(f"Percentual de valores negativos: {percentual_negativos:.2f}%")


analisar_valores()
