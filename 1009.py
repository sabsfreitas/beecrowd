nome = input()
salario_fixo = float(input())
total_vendas = float(input())
comissao = 0.15

total = salario_fixo + (total_vendas * comissao)

print("TOTAL = R$ "+str("%.2f"%total))