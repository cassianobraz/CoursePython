lista = [
    'a', 1, 1.1, True, [0, 1, 2],
    (1, 2), {0, 1}, {'nome': 'Cassiano'},
]

for item in lista:
    if isinstance(item, set):
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print(item.upper())

    if isinstance(item, (int, float)):
        print(item, item * 2)
