def calcular_desconto(compra):
    if compra <= 2000.00:
        return compra * 0.10
    elif compra <= 3000.00:
        return compra * 0.05
    elif compra <= 5000.00:
        return compra * 0.03
    else:
        return compra * 0.02


compra = float(input("Digite o valor da compra: R$ "))
desconto = calcular_desconto(compra)
pagar = compra - desconto

# Exibição dos resultados
print(f"Valor da compra: R$ {compra:.2f}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {pagar:.2f}")