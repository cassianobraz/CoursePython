# pessoa = {
#     'nome': 'Cassiano Pereira',
#     'sobrenome': 'Braz',
#     'idade': 18,
#     'altura': 1.76,
#     'enderecos': [
#         {'rua': 'tal tal', 'numero': 123},
#         {'rua': 'outra rua', 'numero': 123},
#     ]
# }

# print(pessoa)
# for chave in pessoa:
#     print(chave, pessoa[chave])

pessoa = {}

pessoa['nome'] = 'Cassiano'
print(pessoa)

"""
Métodos úteis dos dicionarios 
- len -> quantas chaves
- keys -> iterável com as chaves
- values -> iterável com os valores
- setdefault -> adiciona valor se a chave não existe
- copy -> retorna uma cópia rasa (shallow copy)
- get -> obtém uma chave
- pop -> apaga um item com a chave espefcificada (del)
- popitem -> apaga o último item adicionado
- update -> atualiza um dicionário com outro
"""
