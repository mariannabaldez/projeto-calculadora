class Calculadora:
    def __init__(self):
        self.numero = int(input("primeiro valor:"))
        self.numero2 = int(input("segundo valor: "))


    @classmethod
    def operacao(cls):
        cls.soma

    @property
    def soma(self):
        return self.numero + self.numero2

    @property
    def subtrai(self):
        return self.numero - self.numero2

    @property
    def multiplica(self):
        return self.numero * self.numero2

    @property
    def divide(self):
        return self.numero / self.numero2

    @property
    def calcula_resto(self):
        return self.numero % self.numero2


#x = Calculadora()

#resultado_soma = x.soma
#print(resultado_soma)
valor1 = input("Digite o primeiro valor: ")
operacao = input("Operação: ")
valor2 = input("segundo valor: ")

import operator

operacoes = {"+": operator.add,
             "-": operator.sub,
             "*": operator.mul,
             "/": operator.mod,
            }
operacoes.get()

print(valor1 + operacao + valor2)
# numero = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))
# operacao = input("Digite a operação que deseja fazer na conta: "
#
# "(somar, subtrair, multiplicar, etc)")
#
#
# contas(numero,numero2,operacao)
#
# if operacao == "somar": soma(numero, numero2)
# elif operacao == "subtrair": subtrai(numero, numero2)
# elif operacao == "multiplicar": multiplica(numero, numero2)
# elif operacao == "dividir": dividi(numero, numero2)
# elif operacao == "resto": resto(numero, numero2)



