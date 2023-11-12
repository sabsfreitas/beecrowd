n = int(input())

for i in range(n):
    x = int(input())
    z = int(x / 2)
    soma = 0
    for y in range(1, z + 1):
        if(x % y == 0):
            soma += y
    if(soma == x):
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")