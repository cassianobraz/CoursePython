pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

pessoa_completa = {**pessoa, **dados_pessoa}


def nomeados(*args, **kwargs):
    print(f'Não nomeados: {args}')

    for chave, valor in kwargs.items():
        print(chave, valor)


# nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

nomeados(**configuracoes)
