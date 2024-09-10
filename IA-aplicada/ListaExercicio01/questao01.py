#Faça um algoritmo que leia os valores A, B, C e 
# imprima na tela se a soma de A + B é menor que C. 


a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

def testSum():
    if a + b < c:
        print("O valor da soma de " , a , " + " , b , " é menor que " , c)
    elif a + b == c:
        print("O valor da soma de " , a , " + " , b , " é igual a " , c)
    else:
        print("O valor da soma de " , a , " + " , b , " é maior que " , c)

testSum()