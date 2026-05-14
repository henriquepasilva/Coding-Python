#Ex1. 
class Celsius:
    def __init__(self, valor=0):
        self.temperatura = valor

    def get_fahrenheit(self):
        return (self.temperatura * 1.8) + 32

    def get_kelvin(self):
        return self.temperatura + 273.15

temp = Celsius (25)

print("Temperatura em Celsius: ", temp.temperatura)
print("Temperatura em Fahrenheit: ", temp.get_fahrenheit())
print("Temperatura em Kelvin: ", temp.get_kelvin())

#Ex2. 
def soma(lista: list[Celsius]) -> Celsius:
    total = Celsius(0)
    for t in lista:
        total.temperatura += t.temperatura
    return total

def media(lista: list[Celsius]) -> Celsius:
    total = soma(lista)
    media_valor = total.temperatura / len(lista)
    return Celsius(media_valor)

c1 = Celsius(20)
c2 = Celsius(25)
c3 = Celsius(30)

lista = [c1, c2, c3]
resultado = media(lista)
print("Média em Celsius:", resultado.temperatura)
print("Média em Fahrenheit:", resultado.get_fahrenheit())

#Ex3.
class Celsius:
    def __init__(self, valor=0):
        self._temperatura = 0
        self.temperatura = valor

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < -273.15:
            raise ValueError("A temperatura não pode ser inferior a -273.15 ºC.")
        self._temperatura = valor

    def get_fahrenheit(self):
        return (self.temperatura * 1.8) + 32

    def get_kelvin(self):
        return self.temperatura + 273.15

#Ex4. 
class Celsius:
    def __init__(self, valor=0):
        self.set_temperatura(valor)

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, valor):
        if valor < -273.15:
            self.__temperatura = -273.15
        else:
            self.__temperatura = valor

    def get_fahrenheit(self):
        return (self.__temperatura * 1.8) + 32

    def get_kelvin(self):
        return self.__temperatura + 273.15

#Ex5. 
def soma(lista: list[Celsius]) -> Celsius:
    total = Celsius(0)
    for t in lista:
        total.set_temperatura(total.get_temperatura() + t.get_temperatura())
    return total


def media(lista: list[Celsius]) -> Celsius:
    total = soma(lista)
    media_valor = total.get_temperatura() / len(lista)
    return Celsius(media_valor)

#Ex6. 
class Celsius:
    def __init__(self, valor=0):
        self.set_temperatura(valor)

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, valor):
        if valor < -273.15:
            self.__temperatura = -273.15
        else:
            self.__temperatura = valor

    temperatura = property(get_temperatura, set_temperatura)

    def get_fahrenheit(self):
        return (self.__temperatura * 1.8) + 32

    def get_kelvin(self):
        return self.__temperatura + 273.15

#Ex7.
class Celsius:
    def __init__(self, valor=0):
        self.temperatura = valor

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < -273.15:
            self.__temperatura = -273.15
        else:
            self.__temperatura = valor

    def get_fahrenheit(self):
        return (self.temperatura * 1.8) + 32

    def get_kelvin(self):
        return self.temperatura + 273.15

#Ex7 (2).
from num2words import num2words

class Celsius:
    def __init__(self, valor=0):
        self.temperatura = valor

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < -273.15:
            self.__temperatura = -273.15
        else:
            self.__temperatura = valor

    def get_fahrenheit(self):
        return (self.temperatura * 1.8) + 32

    def get_kelvin(self):
        return self.temperatura + 273.15

    # Método auxiliar privado
    def _unidade(self):
        return "grau" if abs(self.temperatura) == 1 else "graus"

    # Método público que devolve a temperatura por extenso
    def extenso(self):
        temp_int = int(self.temperatura)
        # Converte número em palavras, incluindo negativo
        temp_str = num2words(temp_int, lang='pt')
        return f"{temp_str.capitalize()} {self._unidade()} Celsius"

#Ex8. 
c = Celsius(25)

print(c.temperatura)  # ✅ 25

try:
    print(c.__temperatura)  # ❌ Vai dar AttributeError
except AttributeError as e:
    print("Erro:", e)

print(c.__dict__)

#Ex9. 
class Celsius:
    def __init__(self, valor=0):
        self.temperatura = valor

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < -273.15:
            self.__temperatura = -273.15
        else:
            self.__temperatura = valor

    def get_fahrenheit(self):
        return (self.temperatura * 1.8) + 32

    def get_kelvin(self):
        return self.temperatura + 273.15

    @classmethod
    def soma(cls, lista: list['Celsius']) -> 'Celsius':
        total = cls(0)
        for t in lista:
            total.temperatura += t.temperatura
        return total

    @classmethod
    def media(cls, lista: list['Celsius']) -> 'Celsius':
        total = cls.soma(lista)
        media_valor = total.temperatura / len(lista)
        return cls(media_valor)

c1 = Celsius(20)
c2 = Celsius(25)
c3 = Celsius(30)
lista = [c1, c2, c3]

resultado_soma = Celsius.soma(lista)
resultado_media = Celsius.media(lista)

print(resultado_soma.temperatura)  
print(resultado_media.temperatura) 