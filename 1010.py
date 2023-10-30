entrada1 = input().split()
codigo1 = int(entrada1[0])
pecas1 = int(entrada1[1])
valor1 = float(entrada1[2])

entrada2 = input().split()
codigo2 = int(entrada2[0])
pecas2 = int(entrada2[1])
valor2 = float(entrada2[2])

dados1 = pecas1 * valor1
dados2 = pecas2 * valor2

total = dados1 + dados2

print("VALOR A PAGAR: R$ "+str("%.2f"%total))