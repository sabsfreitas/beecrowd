testes = int(input())

for teste in range(testes):
    palavra = input().lower()
    char = {}
    for c in palavra:
        if c.isalpha() and c not in char:
            char[c] = palavra.count(c)

    ordem = sorted(char.items(), key = lambda x: (-x[1], x[0]))
    maior = ordem[0][1]
    resultado = ''
    for c in ordem:
        if c[1] == maior:
            resultado += c[0]
        else:
            break
    print(resultado)