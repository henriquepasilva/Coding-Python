class PowTwo:
    def __init__(self, max = 0):
        self.max = max
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador >= self.max:
            raise StopIteration

        resultado = 2 ** self.contador
        self.contador += 1
        return resultado

p = PowTwo(5)

for valor in p:
    print(valor)