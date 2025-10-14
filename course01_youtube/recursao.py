def funcao(x):
    print(x)
    if x >= 0:
        funcao(x - 1)
    else:
        return


def sauda(nome):
    print("Olá " + nome)
    sauda2(nome)
    print("Preparando-se para dizer tchau")
    tchau()


def sauda2(nome):
    print("Como você está " + nome + "?")


def tchau():
    print("ok, tchau!")


# sauda('Cassiano')

def fatorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fatorial(x - 1)


print(fatorial(3))


# def soma(lista):
#     valor = 0
#     for i in lista:
#         valor += 1
#         return valor


# def soma_recursiva(lista):
#     if not lista:
#         return 0

#     return lista.pop(0) + soma_recursiva(lista)


# print(soma_recursiva([1, 2, 3]))
