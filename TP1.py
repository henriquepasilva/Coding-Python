import sys

# Ex 1.
class Pessoa:
    pass

# Ex 2.
pessoa_1 = Pessoa()
print("Pessoa 1:", pessoa_1)

# Ex 3.
print("ID de pessoa_1:", id(pessoa_1))

# Ex 5.
pessoa_2 = Pessoa()
print("Pessoa 2:", pessoa_2)
print("ID de pessoa_2:", id(pessoa_2))

# Ex 6.
print("Número de referências a pessoa_1:", sys.getrefcount(pessoa_1))

# Ex 7.
class Pessoa:
    pass

pessoa_1 = Pessoa()
pessoa_2 = Pessoa()

a = pessoa_1

lista = []
lista.append(a)

print(sys.getrefcount(pessoa_1))

# Ex 8.  
a = 1
b = 1
print(a is b)  # True → o Python reutiliza sempre o mesmo objeto para inteiros pequenos

a = [1]
b = [1]
print(a is b)  # False → cada lista criada é um objeto novo

a = [1]
b = a
print(a is b)  # True → b apenas aponta para a mesma lista já existente em a

a = [1]
b = a[:]  # ou list(a)
print(a is b)  # False → ao copiar a lista cria-se um objeto diferente na memória

# Ex 9. 
class PizzaMedia:
    diametro_cm = 30   # atributo de classe 
    
    def __init__(self, nome):
        self.nome = nome  # atributo de instância

# Ex 10.   
class Pizza:
    def __init__(self, nome):
        self.nome = nome

    def nome_maiusculas(self):
        return self.nome.upper()

pizza = Pizza("Margherita")
print(pizza.nome_maiusculas())

# Ex 12. e 13. 
class Pizza:
    def __init__(self, nome, ingredientes=None):
        self.nome = nome
        if ingredientes is None:
            self.ingredientes = ["tomate", "queijo mozarella"]
        else:
            self.ingredientes = ingredientes

pizza1 = Pizza("Margherita")
print(pizza1.ingredientes)

pizza2 = Pizza("Pepperoni", ["pepperoni", "queijo"])
print(pizza2.ingredientes)

# Ex 14. 
from math import pi

class Pizza:
    def __init__(self, nome, raio):
        self.nome = nome
        self.raio = raio

    def area(self):
        return pi * self.raio ** 2

pizza = Pizza("Margherita", 15)
print(pizza.area()) 

# Ex 15. 
class Ingrediente:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

ingrediente = Ingrediente("queijo", 100)
print(ingrediente.nome, ingrediente.quantidade)

class PizzaMedia:
    def __init__(self, nome, ingredientes=None):
        self.nome = nome
        if ingredientes is None:
            self.ingredientes = [Ingrediente("tomate", 50), Ingrediente("queijo mozarella", 100)]
        else:
            self.ingredientes = ingredientes

# Teste
pizza = PizzaMedia("Margherita")
for ing in pizza.ingredientes:
    print(ing.nome, ing.quantidade)

# Ex 16. 
class PizzaMedia:
    def __init__(self, nome, ingredientes=None):
        self.nome = nome
        if ingredientes is None:
            self.ingredientes = [Ingrediente("tomate", 50), Ingrediente("queijo mozarella", 100)]
        else:
            self.ingredientes = ingredientes

    def peso_ingredientes(self):
        return sum(ing.quantidade for ing in self.ingredientes)

pizza = PizzaMedia("Margherita")
print(pizza.peso_ingredientes()) 

# Ex 15. e 16. (B)
class PizzaPequena(PizzaMedia):
    def __init__(self, nome, ingredientes=None):
        super().__init__(nome, ingredientes)
        self.raio = 10

class PizzaMedia(PizzaMedia):
    def __init__(self, nome, ingredientes=None):
        super().__init__(nome, ingredientes)
        self.raio = 15

class PizzaGrande(PizzaMedia):
    def __init__(self, nome, ingredientes=None):
        super().__init__(nome, ingredientes)
        self.raio = 20
        
pizza = PizzaGrande("Pepperoni")
print(pizza.raio)