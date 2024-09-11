#11) Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal deetiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
# para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado.
# Código Condição de pagamento
# 1 À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 À vista no cartão de crédito, recebe 15% de desconto
# 3 Em duas vezes, preço normal de etiqueta sem juros
# 4 Em duas vezes, preço normal de etiqueta mais juros de 10% 




def calcula_preco():
    while True:
        try:
            preco_etiqueta = float(input("Digite o preço de etiqueta do produto: R$ "))
        except ValueError:
            print("Preço inválido. Por favor, digite um número válido.")
            continue

        print("""
        Escolha a condição de pagamento:
        1 - À vista em dinheiro ou cheque, recebe 10% de desconto
        2 - À vista no cartão de crédito, recebe 15% de desconto
        3 - Em duas vezes, preço normal de etiqueta sem juros
        4 - Em duas vezes, preço normal de etiqueta mais juros de 10%
        5 - Sair
        """)

        try:
            condicao_pagamento = int(input("Digite o código da condição de pagamento: "))
        except ValueError:
            print("Código inválido. Por favor, digite um número entre 1 e 5.")
            continue

        if condicao_pagamento == 1:
            preco_final = preco_etiqueta * 0.90  # 10% de desconto
            descricao = "à vista em dinheiro ou cheque, com 10% de desconto"
        elif condicao_pagamento == 2:
            preco_final = preco_etiqueta * 0.85  # 15% de desconto
            descricao = "à vista no cartão de crédito, com 15% de desconto"
        elif condicao_pagamento == 3:
            preco_final = preco_etiqueta  # Preço normal
            descricao = "em duas vezes, preço normal de etiqueta sem juros"
        elif condicao_pagamento == 4:
            preco_final = preco_etiqueta * 1.10  # 10% de juros
            descricao = "em duas vezes, preço normal de etiqueta mais juros de 10%"
        elif condicao_pagamento == 5:
            print("Saindo do programa.")
            break
        else:
            print("Código de condição de pagamento inválido.")
            continue

        print(f"O valor a ser pago pelo produto é: R$ {preco_final:.2f} ({descricao}).")

# Chama a função para calcular o preço
calcula_preco()
