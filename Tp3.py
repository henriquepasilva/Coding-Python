#Ex.1
def cozinha_no_forno( item ):
 tempo_de_cozedura = item.getMinutosDeCozedura()
 print("O forno está a cozinhar durante",
tempo_de_cozedura,"minutos.")

class Pizza():
    def getMinutosDeCozedura(self):
        return(15)

class Broa():
    def getMinutosDeCozedura(self):
        return(30)

Pizza = Pizza()
Broa = Broa()

cozinha_no_forno(Pizza)
cozinha_no_forno(Broa)

#Ex.2
class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def getNomeCompleto(self):
        return self.nome + " " + self.sobrenome

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, idade, numero_mecanografico):
        super().__init__(nome, sobrenome, idade)
        self.numero_mecanografico = numero_mecanografico
    
    def getAluno(self):
        return f"{self.getNomeCompleto()}, {self.numero_mecanografico}"

    def __str__(self):
        return self.getAluno()
    
a = Aluno("Henrique", "Silva", 20, 1234)
print(a)

#Ex.4
class Celsius:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro):
        if isinstance(outro, Celsius):
            return Celsius(self.valor + outro.valor)
        elif isinstance(outro, (int, float)):
            return Celsius(self.valor + outro)
        return NotImplemented

    def __radd__(self, outro):
        return self.__add__(outro)

    def __str__(self):
        return f"{self.valor}°C"

def soma(lista):
    total = Celsius(0)
    for item in lista:
        total += item 
    return total

c1 = Celsius(5)
c2 = Celsius(10)
c3 = Celsius(7)

print(c1 + c2)
print(c1 + 5 + c2)

#Ex.6
from abc import ABC, abstractmethod

class VaiAoForno(ABC):
    @abstractmethod
    def getMinutosDeCozedura(self):
        pass

class Pizza(VaiAoForno):
    def getMinutosDeCozedura(self):
        return 15

class Broa(VaiAoForno):
    def getMinutosDeCozedura(self):
        return 30

def cozinha_no_forno(item):
    tempo_de_cozedura = item.getMinutosDeCozedura()
    print("O forno está a cozinhar durante", tempo_de_cozedura, "minutos.")

pizza = Pizza()
broa = Broa()

cozinha_no_forno(pizza)
cozinha_no_forno(broa)

#Ex.7
from abc import ABC, abstractmethod

class VaiAoForno(ABC):
    @abstractmethod
    def getMinutosDeCozedura(self):
        pass

class Ingrediente:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade 

    def __str__(self):
        return f"{self.nome} ({self.quantidade}g)"

class PizzaMedia(VaiAoForno):
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def getMinutosDeCozedura(self):
        return 15

    def __str__(self):
        lista = ", ".join(str(ing) for ing in self.ingredientes)
        return f"Pizza Média com: {lista}"

class Broa(VaiAoForno):
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def getMinutosDeCozedura(self):
        return 30 

    def __str__(self):
        lista = ", ".join(str(ing) for ing in self.ingredientes)
        return f"Broa com: {lista}"

def cozinha_no_forno(item):
    tempo = item.getMinutosDeCozedura()
    print(f"O forno está a cozinhar durante {tempo} minutos.")
    print("Conteúdo:", item)
    print("-" * 60)

if __name__ == "__main__":
    queijo = Ingrediente("Queijo Mozzarella", 100)
    fiambre = Ingrediente("Fiambre", 80)
    tomate = Ingrediente("Molho de Tomate", 50)
    azeitonas = Ingrediente("Azeitonas", 20)
    farinha = Ingrediente("Farinha", 200)
    mel = Ingrediente("Mel", 50)

    pizza = PizzaMedia([queijo, fiambre, tomate, azeitonas])
    broa = Broa([farinha, mel])

    cozinha_no_forno(pizza)
    cozinha_no_forno(broa)