salario = float(input())
imposto = 0

if 0.00 < salario <= 2000.00:
    print("Isento")
elif 2000.00 < salario <= 3000.00:
    imposto = 0.08 * (salario - 2000.00)
    print(f"R$ {imposto:.2f}")
elif 3000.00 < salario <= 4500.00:
    imposto = 0.18 * (salario - 3000.00) + 80.00  
    print(f"R$ {imposto:.2f}")
else:
    imposto = 0.28 * (salario - 4500.00) + 350.00  
    print(f"R$ {imposto:.2f}")