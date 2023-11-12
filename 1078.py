n = int(input())
x = 0
multiplica = 1

if n > 2 and n < 1000:
    while x < 10:
        x += 1
        multiplica = x * n
        print(x, "x", n, "=", multiplica)