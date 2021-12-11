def desenho_calculadora():
    desenho_calculadora = [[7, 8, 9],
                           [4, 5, 6],
                           [1, 2, 3],
                           [0, "", ""]]
    print(f"{desenho_calculadora}")


def soma(numero, numero2):
    return numero + numero2


def subtrai(numero, numero2):
    return numero - numero2


def multiplica(numero, numero2):
    return numero * numero2


def divide(numero, numero2):
    return numero / numero2


def calcula_resto(numero, numero2):
    return numero % numero2


numero = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja fazer na conta: "
                 "(somar, subtrair, multiplicar, etc)")


if operacao == "somar": soma(numero, numero2)
elif operacao == "subtrair": subtrai(numero, numero2)
elif operacao == "multiplicar": multiplica(numero, numero2)
elif operacao == "dividir": dividi(numero, numero2)
elif operacao == "resto": resto(numero, numero2)