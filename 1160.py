
T = int(input())
for i in range(T):
    PA, PB, G1, G2 = input().split()
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)
    a = 0

    while (PA <= PB):
        cPA = int((PA * (G1 / 100)))
        cPB = int((PB * (G2 / 100)))
        a += 1
        PA += cPA
        PB += cPB
        if (a > 100):
            break
    if (a > 100):
        print("Mais de 1 seculo.")
    else:
        print("%d anos." % a)