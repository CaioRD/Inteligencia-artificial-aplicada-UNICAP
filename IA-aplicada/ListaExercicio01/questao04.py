#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se
#somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se
#atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

while True: 
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    
    if a == b:
        c = a + b
        print(f"O valor de C é: {c}")
    else:
        c = a * b
        print(f"O valor de C é: {c}")
    break