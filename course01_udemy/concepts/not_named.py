def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multipla = multiplicar(1, 5, 7)
print(multipla)


def pareimpar(numero):
    if numero % 2 == 0:
        return 'Par'
    return 'Impar'


print(pareimpar(multipla))
