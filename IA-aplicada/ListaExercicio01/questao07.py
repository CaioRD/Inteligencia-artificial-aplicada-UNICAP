#Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar,
#imprimir o resultado desta operação.

def somarValor():
    numero = int(input("digite o valor que deseja: "))
    
    while True:
        if numero < 0:
            print("não é possível realizar a operação com números negativos")
            continue
        elif numero % 2 == 0:
             numero += 5
             print("O número é par, então seu valor incrementa + 5")
             print(f"O valor do número é {numero}")
        elif numero % 2 == 1:
             numero += 8
             print("O número é par, então seu valor incrementa + 8")
             print(f"O valor do número é {numero}")

        break
somarValor()