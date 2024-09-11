#Escreva um algoritmo que leia três valores inteiros e 
# diferentes e mostre-os em ordem decrescente. 

def  ordena_valores():
    while True:
        a = int(input("digite o primeiro valor: "))
        b = int(input("digite o segundo valor: "))
        c = int(input("digite o terceiro valor: "))
        
        if a == b and a == c and b == c:
            print("Os valores digitados são iguais, por favor digite valores diferentes")
        elif a == b or a == c or b == c:
            print("Os valores digitados são iguais, por favor digite valores diferentes")
        else:
            if a > b and a > c:
                if b > c:
                    print(f"Ordem decrescente: {a}, {b}, {c}")
                else:
                    print(f"Ordem decrescente: {a}, {c}, {b}")
            elif b > a and b > c:
                if a > c:
                    print(f"Ordem decrescente: {b}, {a}, {c}")
                else:
                    print(f"Ordem decrescente: {b}, {c}, {a}")
            else:
                if a > b:
                    print(f"Ordem decrescente: {c}, {a}, {b}")
                else:
                    print(f"Ordem decrescente: {c}, {b}, {a}")
            break

ordena_valores()
            
            