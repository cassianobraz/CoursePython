def quicksort(lista):
    if len(lista) < 2:
        return lista

    meio = len(lista) // 2
    pivo = lista.pop(meio)
    menores = [i for i in lista if i <= pivo]
    maiores = [i for i in lista if i > pivo]

    return quicksort(menores) + [pivo] + quicksort(maiores)


print(quicksort([2, 5, 4, 1, 10]))
