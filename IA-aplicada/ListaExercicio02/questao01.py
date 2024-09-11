#Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de
#três e que se encontram no conjunto dos números de 1 até 500. 

def soma_impares_multiplos_de_tres():
    soma = 0
    for numero in range(1, 501):
        if numero % 2 != 0 and numero % 3 == 0:
            soma += numero
    return soma

# Chama a função e imprime o resultado
resultado = soma_impares_multiplos_de_tres()
print(f"A soma de todos os números ímpares que são múltiplos de três entre 1 e 500 é: {resultado}")
