# A classe PizzaMedia possui um atributo de classe
 # diametro_cm que é compartilhado por todas as instâncias
 # e um atributo de instância nome que é específico para cada instância individual. def __int__(self, nome):

from math import pi

class PizzaMedia():
        diametro_cm = 30

        @classmethod
        def getCalcula_Area(cls):
            return ((cls.diametro_cm/2)**2)*pi  #14  Criamos um método da class PizzaMedia, onde utilizamos
                                                #    um "classmethod" para calcular a area.
        def __init__(self, nome, lista):
            self.nome = nome
            self.lista = lista            #12 Inicialização da lista
            self.__num_fatias = 0

        def UPPER(self):                # 10 Método UPPER, onde transforma todos os caracteres em MAIUSCULAS!!
            return self.nome.upper()


        def getNumFatias(self):
            return self.__num_fatias

        def setNumFatias(self, value):
            if value < 0:
                value = 0
            self.__num_fatias = value

        numFatias = property(getNumFatias, setNumFatias)



#class PizzaPequena(PizzaMedia):    # 15 Criamos uma class derivada da class 'Pai' -> PizzaMedia, como o diametro não
    #diametro_cm = 20                # não está incluido dentro do __init__ da class Pai, então teremos que criar novos
                                        # diametros

#class PizzaGrande(PizzaMedia):
    #diametro_cm = 40

PizzaMedia.setNumFatias(3)

print("Num de fatias", PizzaMedia.getNumFatias() )





#pizza = PizzaMedia("Margarita")
#print(pizza.UPPER())

ingredientes_pizza  = ["tomate", "queijo mozarela"]        #13
pizza = PizzaMedia("Magarina", ingredientes_pizza)


#print(pizza.UPPER(), pizza.lista)

#print(PizzaMedia.getCalcula_Area())





