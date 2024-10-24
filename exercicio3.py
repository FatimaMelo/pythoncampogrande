compra = float(input("Digite o valor da compra: R$ "))
desconto = 0.0

if compra <= 2000.00:
    desconto = compra * 0.10
elif compra <= 3000.00:
    desconto = compra * 0.05
elif compra <= 5000.00:
    desconto = compra * 0.03
else:
    desconto = compra * 0.02


pagar = compra - desconto

# Exibição dos resultados
print(f"Valor da compra: R$ {compra:.2f}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {pagar:.2f}")