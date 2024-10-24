total_descontos = 0

for i in range(10):
     nome = input("Digite o nome do cliente: ")
     valor_compra = float(input("Digite o valor da compra: R$ "))

    if valor_compra >= 1500:
        desconto = valor_compra * 0.20
    else:
        desconto = valor_compra * 0.15


    valor_a_pagar = valor_compra - desconto


    print(f"\n--- Dados do Cliente ---")
    print(f"Cliente: {nome}")
    print(f"Valor da compra: R$ {valor_compra:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
    print("-------------------------")

   total_descontos += desconto


print(f"\nTotal de descontos dados: R$ {total_descontos:.2f}")