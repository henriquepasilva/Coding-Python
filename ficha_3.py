from abc import ABC, abstractmethod

#1
def cozinha_no_forno (item):
    tempo_de_cozed = item.getMinutosCozeduras()
    print("O forno está a cozinhar durante", tempo_de_cozed,"minutos. ")


#5
class VaiaoForno(ABC):
    @abstractmethod
    def getMinutosCozeduras(self):...
        #pass


class Pizaa(VaiaoForno):
   def getMinutosCozeduras(self):
        return 5

class Broa(VaiaoForno):
    def getMinutosCozeduras(self):
        return 20

#piz1 = Pizaa()
#broa1 = Broa()

#cozinha_no_forno(piz1)
#cozinha_no_forno(broa1)

#-*-*-*-*-*-*-*-*-*---*-*-*---*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-

#2 e #3

class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome =  sobrenome

    def getNome(self):
        return self.nome + ", " + self.sobrenome

    def __str__(self):
      return self.getNome()

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, numerario):
        super().__init__(nome, sobrenome)
        self.numerario = numerario

    def GetAluno(self):
       return self.getNome() + ", " + str(self.numerario)


    def __str__(self):
        #return super().__str__() + ", " + str(self.numerario)
        return self.GetAluno()

aluno = Aluno("João", "Silva", 1234)
print("",aluno)




#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*

#4
class Celsius():
    def __init__(self, valor = 0 ):
        self.temperatura = valor

    def __add__(self, other):
        if isinstance(other, Celsius):
            return Celsius(self.temperatura + other.temperatura)

a = Celsius(5)
b = Celsius(15)

print("VALOR SOMA : ", (a+b).temperatura)

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

#6

#class PizzaPP(PizzaMedia):
    #tamanho_cm = 15


#class PizzaGG(PizzaMedia):
    #tamanho_cm = 40



