def calcula_potencia(numero, numero2):
    calculo = numero
    for i in range(1, numero2):
        calculo *= numero
    return calculo


from functools import reduce
def calcula_raiz(numero):
    list =[]
    for i in range(0, numero):
        if numero % i == 0:
            list.append(i)
    reduce(lambda x, y: x * y, list)


def operacao_escolhida(operacao):
    operacoes = {"+": lambda numero, numero2: numero + numero2,
                 "-": lambda numero, numero2: numero - numero2,
                 "*": lambda numero, numero2: numero * numero2,
                 "/": lambda numero, numero2: numero / numero2,
                 "%": lambda numero, numero2: numero % numero2,
                 "^": calcula_potencia,
                 "v": calcula_raiz
                 }
    return operacoes.get(operacao)


desenho_calculadora = [[7, 8, 9, "%", "v"],
                       [4, 5, 6, "*", "/"],
                       [1, 2, 3, "^", "-"],
                       [0, "+", "="]]
print(desenho_calculadora)
numero = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja fazer na conta: "
                 "(+, -, *, /, %, ^, v) ")
calculo = operacao_escolhida(operacao)
print(calculo(numero, numero2))