# 12) Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas
# 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de
# aproveitamento, usando a fórmula:
# MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7
# A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do aluno,
# suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a
# mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o conceito for D ou E.
# Média de aproveitamento Conceito
# >= 90 A
# >= 75 e < 90 B
# >= 60 e < 75 C
# >= 40 e < 60 D
# < 40 E 

def calcular_media():
    
    numero_identificacao = input("Digite o número de identificação do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    media_exercicios = float(input("Digite a média dos exercícios: "))
    
    media_aproveitamento = (nota1 + (nota2 * 2) + (nota3 * 3) + media_exercicios) / 7
    
    if media_aproveitamento >= 90:
        conceito = 'A'
    elif media_aproveitamento >= 75:
        conceito = 'B'
    elif media_aproveitamento >= 60:
        conceito = 'C'
    elif media_aproveitamento >= 40:
        conceito = 'D'
    else:
        conceito = 'E'
    
    if conceito in ['A', 'B', 'C']:
        status = 'Aprovado'
    else:
        status = 'Reprovado'
    
   
    print(f"\nNúmero de Identificação: {numero_identificacao}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média dos Exercícios: {media_exercicios}")
    print(f"Média de Aproveitamento: {media_aproveitamento:.2f}")
    print(f"Conceito: {conceito}")
    print(f"Status: {status}")


calcular_media()
