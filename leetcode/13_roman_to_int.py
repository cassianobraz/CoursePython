def roman(s: str) -> int:
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    anterior = 0

    for c in reversed(s):
        valor = valores[c]
        if valor < anterior:
            total -= valor
        else:
            total += valor
        anterior = valor

    return total


print(roman("LII"))
