# Set para remover valores duplicados
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)

# print(l2)
# Set são iteráveis (for, in, not in)
# s1 = {1, 2, 3}
# print(s1)

# Métodos (add, update, clear, discard)
# s1 = set()
# s1.add('Cassiano')
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()
# s1.discard('Olá mundo')
# print(s1)

"""
Operadores úteis:
união (union) - une: |
intersecção - itens presente em ambos: &
diferença - Itens presentes apenas no set da esqueda: -
diferença simétrica - itens que não estão em ambos: ^
"""

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}

# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s1 - s2
# s3 = s1 ^ s2

# print(s3)
