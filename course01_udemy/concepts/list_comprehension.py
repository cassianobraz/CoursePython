# print(list(range(10)))

# lista = [numero*2 for numero in range(10)]
# print(lista)
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]

# print(*novos_produtos, sep='\n')
# p(novos_produtos)

# lista = [n for n in range(10) if n < 5]
# print(lista)

# lista = [(x, y) for x in range(3) for y in range(3)]
# p(lista)

# lista = [[(word) for word in 'Cassiano'] for x in range(1)]
# p(lista)

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# for chave, valor in produto.items():
#     print(chave, valor)

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

# print(dict(dc))

s1 = {i for i in range(10)}
print(s1)
