# def write_number(num):
#   print(num)

# write_number(2)

# project inital calculate

import math


def write_menu():
    print("Escolha uma operação: ")
    print("1 - Raiz quadrada")
    print("2 - Soma da sequência")
    print("0 - Sair do programa")


def calc_raiz_quadrada():
    entrada = int(input("Insira um número: "))
    result = math.sqrt(entrada)
    print("Result: " + str(result))


def calc_sum_sequency():
    entrada = int(input("Insira a quantidade de números a serem somados: "))

    total = 0
    for i in range(entrada):
        entrada = int(input("Insira o próximo número: "))
        total = total + entrada

    print("Resultado da soma dos valores: " + str(total))


print("-" * 20)
print("Calculadora Python")
print("-" * 20)


entrada = 1
while entrada != 0:
    write_menu()
    entrada = int(input(">"))
    if entrada == 1:
        calc_raiz_quadrada()
    elif entrada == 2:
        calc_sum_sequency()
    else:
        print("Adeus!")
