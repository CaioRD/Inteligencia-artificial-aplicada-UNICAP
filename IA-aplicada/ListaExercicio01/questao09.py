# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, utilizando as seguintes fórmulas:
#● para homens: (72.7 * h) – 58;
# para mulheres: (62.1 * h) – 44.7. 

def calcula_peso():
    while True:
        sexo = input("Digite o sexo (m/f): ").lower()
        if sexo != "m" and sexo != "f":
            print("Sexo inválido. Por favor, digite 'm' para masculino ou 'f' para feminino.")
            continue
        
        try:
            altura = float(input("Digite a altura em metros (ex: 1.75): "))
        except ValueError:
            print("Altura inválida. Por favor, digite um número.")
            continue

        if sexo == "m":
            peso_ideal = (72.7 * altura) - 58
        elif sexo == "f":
            peso_ideal = (62.1 * altura) - 44.7
        
        print(f"O peso ideal para uma pessoa do sexo {'masculino' if sexo == 'm' else 'feminino'} com altura {altura}m é {peso_ideal:.2f} kg.")
        break

calcula_peso()
