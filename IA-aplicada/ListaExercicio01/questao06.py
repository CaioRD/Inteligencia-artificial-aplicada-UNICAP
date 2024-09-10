#Escreva um algoritmo que lê dois valores booleanos (lógicos) e então determina se ambos são
#VERDADEIROS ou FALSOS. 


def str_to_bool(value):
    return value.lower() in ['true', 'verdadeiro', '1']


valor1_str = input("Digite o primeiro valor booleano (True/False): ")
valor2_str = input("Digite o segundo valor booleano (True/False): ")


valor1 = str_to_bool(valor1_str)
valor2 = str_to_bool(valor2_str)


if valor1 and valor2:
    print("Ambos são VERDADEIROS")
elif not valor1 and not valor2:
    print("Ambos são FALSOS")
else:
    print("Os valores são diferentes")
