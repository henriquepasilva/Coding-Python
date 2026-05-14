from math import sqrt

class Point3D:
    # declarar as variaveis
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # declarar o identificar self
    def about(self):
        return f"{self.x}-{self.y}-{self.z}"

    # calcular a distancia com a equação dada no enuciado(sqrt(self - other) ** 2)
    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

if __name__ == '__main__':
    # Criar os pontos das variaveis que estao criadas na classe
    p1 = Point3D(1.0, 2.0, 3.0)
    p2 = Point3D(2.0, 3.0, 1.0)
    
    # Imprimir os valores dos pontos e a distancia
    print("Ponto 1:", p1.about())
    print("Ponto 2:", p2.about())
    print("Distância:", p1.distance(p2))  



