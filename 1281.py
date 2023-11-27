N = int(input())
while N:
    N -= 1
    feira = {}
    total = 0.0

    M = int(input())
    while M:
        M -= 1
        nome, valor = input().split()
        feira[nome] = float(valor)

    P = int(input())
    while P:
        P -= 1
        nome, qtd = input().split()
        total += feira[nome] * int(qtd)

    print(f'R$ {total:.2f}')
