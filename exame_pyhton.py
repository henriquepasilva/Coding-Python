import math


class PizzaMedia():
    tamanho_cm = 30

    def __init__(self, nome, lista):
        self.nome = nome
        self.lista = lista

    def Devolve_iausculas(self):
        return self.nome.upper()

    def AreaCalcula(self):
        raio = self.tamanho_cm / 2
        return math.pi * (raio ** 2)

    def listar_ingr(self):
        return self.lista

    def adicionar_ingr(self, ingr):
        self.lista.append(ingr)


class PizzaPP(PizzaMedia):
    tamanho_cm = 15


class PizzaGG(PizzaMedia):
    tamanho_cm = 40


p = PizzaMedia("pra que", [])
pp = PizzaPP("nome pequena", [])
gg = PizzaGG("nome grnade", [])
print("Nome : ", p.Devolve_iausculas())
print("NOME PIZZA PEQUENA :  ", pp.Devolve_iausculas())

lista_ingr = ["tomate", "quieji", "cogumelo"]
p.adicionar_ingr(lista_ingr)
pp.adicionar_ingr(lista_ingr)
print("INgrients : ", p.listar_ingr())
print("INGRENDSTA PP:  ", pp.listar_ingr())

arecm = p.AreaCalcula()
areapp = pp.AreaCalcula()
print("areA pizza:  ", arecm)
print("Area ppp: ", areapp)

