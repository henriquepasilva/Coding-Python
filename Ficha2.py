

def num2words(num, lang = None):
    return  f"#{num}#"
class Celsius:
    def __init__(self, valor=0):       # 1 lê-mos a temperatura por uma variável, c = Celsius(24), isto é chamamos a Classe e passamos um valor "24" como parametro.Para assim obter-mos um resultado (temperatura).                                   #
        if valor < -273.15:
            valor = -273.15
        self.__temperatura = valor

                                                # 3 Criamos este if pois como temperaturas em fahrenheit
        #self.__set_temperatura(valor)          # 5

    def to_fahrenheit(self):
        return (self.__temperatura * 1.8) + 32

    #def __set_temperatura(self, temperatura):    # 4 Criamos um set para manipularmos a temperatura fora da Classe Celsius
#
 #       if temperatura < -273.15:
  #          temperatura = -273.15
#        self.__temperatura = temperatura

    #def get_temperatura(self):                                     # 4 Devolve a temperatura
      #  return self.__temperatura

   # temperatura = property(get_temperatura, __set_temperatura)         #6

    @property                                                           #7
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < -273.15:
            valor = -273.15
        self.__temperatura = valor


    def __get_degree_text(self):                                #7
        if  self.__temperatura in (1,-1):
        #if self.__temperatura == 1 or self.__temperatura == -1:
            return "grau"
        return  "graus"

    def extenso(self):
        s = num2words(self.__temperatura)
        lst = {
            s[0].upper() + s[1:],
            self.__get_degree_text(),
            "Celsius"
        }
        return " ".join(lst)


    @staticmethod
    def soma(lista):         #2
        sum = Celsius(0)
        for t in lista:
            sum.temperatura += t.temperatura
        #sum.set_temperatura(sum.get_temperatura() + t.get_temperatura())
        return sum


def media(lista___):
    s = Celsius.soma(lista___)
    s.temperatura = s.temperatura / len(lista___)
    #s.set_temperatura(s.get_temperatura()/len(lista___))
    return s
    #return  Celsius(s.temperatura / len(lista___))


lista = [Celsius(15), Celsius(41), Celsius(3)]

s = Celsius.soma(lista)
print("Temperatura soma em ºC : ", s.temperatura)
print("Temperatura soma em ºF : ", s.to_fahrenheit())

m = media(lista)
print("Temperatura media em ºC : ", m.temperatura)
print("Temperatura media em ºF : ", m.to_fahrenheit())

c = Celsius(24)
graus_negativos = Celsius(-300)
print(graus_negativos.temperatura)

print(c.temperatura)
print(c.to_fahrenheit())

print("A: ", Celsius(-1).extenso())
print("B: ", Celsius(0).extenso())
print("C: ", Celsius(1).extenso())
print("D: ", Celsius(2).extenso())
