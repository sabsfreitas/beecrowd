itens = { 
    1: ['Cachorro quente', 4.00], 
    2: ['X-Salada', 4.50],
    3: ['X-Bacon', 5.00],
    4: ['Torrada simples', 2.00],
    5: ['Refrigerante', 1.50]
}

entrada = input().split()

codigo = int(entrada[0])
qtd = int(entrada[1])

total = 0.0

if codigo in itens:
    valor = itens[codigo][1]
    total = valor * qtd

print(f"Total: R$ {total:.2f}")
