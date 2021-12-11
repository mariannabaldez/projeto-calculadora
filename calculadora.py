def desenho_calculadora():
    desenho_calculadora = [[7, 8, 9],
                           [4, 5, 6],
                           [1, 2, 3],
                           [0, "", ""]]
    print(f"{desenho_calculadora}")
def somar(numero, numero2):
    resultado = numero + numero2
    print(f"{numero} + {numero2} = {resultado} ")

def subtrair(numero, numero2):
    resultado = numero - numero2
    print(f"{numero} - {numero2} = {resultado} ")

def multiplicar(numero, numero2):
    resultado = numero * numero2
    print(f"{numero} x {numero2} = {resultado} ")

def dividir(numero, numero2):
    resultado = numero / numero2
    print(f"{numero} / {numero2} = {resultado} ")

def resto(numero, numero2):
    resto = numero % numero2
    print(f"{numero} % {numero2} = {resto}")


numero = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja fazer na conta: "
                 "(somar, subtrair, multiplicar, etc)")

if operacao == "somar": somar(numero, numero2)
elif operacao == "subtrair": subtrair(numero, numero2)
elif operacao == "multiplicar": multiplicar(numero, numero2)
elif operacao == "dividir": dividir(numero, numero2)
elif operacao == "resto": resto(numero, numero2)