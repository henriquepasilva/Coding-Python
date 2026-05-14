def num2words(num, lang = None):
    return  f"#{num}#"

class Celsius():
    def __init__(self, valor =0 ):
        if valor < -273.15:
            valor = -273.15
        #self.__temperatura = self.set_temperatura(valor)
        self.__temperatura = valor

    def to_fahr(self):
        return (self.__temperatura * 1.8) + 32


    #def set_temperatura(self, valor):
      #  if valor < -273.15:
        #    valor = -273.15
        #self._temperatura = valor

    #def get_temperatura(self):
        #return self.
    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, new_valor):
        if new_valor < -273.15:
            valor = -273.15
        self.__temperatura = new_valor

    def extenso(self):
        if self.__temperatura == 0:
            return "Zero graus Celsius"
        elif self.__temperatura == 1:
            return "Um grau Celsius"
        else:
            return f"{num2words(self.__temperatura, lang='pt_BR')} graus Celsius"


def soma(lista):
    sum = Celsius(0)
    for t in lista:
        sum.temperatura += t.temperatura
    return sum

def media(lista):
    total = soma(lista)
    media_Celsus = total.temperatura / len(lista)
    return media_Celsus



temp = Celsius(32)
lista_Celsius=[Celsius(40), Celsius(30), Celsius(15), Celsius(14) ]
soma_CELS = soma(lista_Celsius)
media_CELS = media(lista_Celsius)

print(" TEMP EM CELSIUS : ", temp.temperatura)
print("Soma : ", soma_CELS.temperatura)
print("media : ", media_CELS)

print(Celsius(-1).extenso())  # Menos um grau Celsius
print(Celsius(0).extenso())   # Zero graus Celsius
print(Celsius(1).extenso())   # Um grau Celsius
print(Celsius(2).extenso())   # Dois graus Celsius
