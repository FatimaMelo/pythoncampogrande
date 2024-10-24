
nivel = int(input("Digite o nível do professor (1 ou 2): "))
horas_aula = float(input("Digite a quantidade de horas de aula dadas no mês: "))

# Verificando se o nível é válido
if nivel == 1:
    salbase = 56 * horas_aula
elif nivel ==2:
    salbase = 66 * horas_aula
else:
    print("Nível Inexistente!")
    salbase = 0

dsr = salbase * 0.15
salario = salbase + dsr

print(f"O salário do professor é: R${salario:.2f}")

