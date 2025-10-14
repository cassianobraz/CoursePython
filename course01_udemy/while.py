# count = 0

# while count <= 100:
#     count += 1

#     if count % 2 == 0:
#         continue

#     print(f"Apenas impar: {count}")

#     if count == 41:
#         break

# qtd_rows = 5
# qtd_columns = 5

# line = 1
# while line <= qtd_rows:
#     column = 1
#     while column <= qtd_columns:
#         print(line, column)
#         column += 1
#     line += 1

# print('Finish')

# nome = 'Cassiano Pereira'

# contador = 0
# new_name = ''
# while contador < len(nome):
#     letra = nome[contador]
#     new_name += f'{letra}*'
#     contador += 1

# print(new_name)

# texto = 'Python'

# novo_texto = ''
# for i in texto:
#     novo_texto += f'*{i}'
# print(novo_texto)

# def soma(x, y, z=None):
#     if z is not None:
#         print(f'{x=} {y=} {z=}', x+y+z)
#     else:
#         print(f'{x=} {y=}', x+y)

# soma(1, 2)
#################

"""
escopo de função em python
"""

x = 1


def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)
