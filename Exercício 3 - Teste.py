from ponto1 import Point3D
from ponto2 import perimeter

class Polygon:
    def __init__(self, text, points=None):
        self._text, self._points, self._color = text, points or [], "black"

    @property
    def color(self): return self._color

    @color.setter
    def color(self, v): 
        if v in ["red", "yellow", "green", "black"]: self._color = v

    def add_point(self, p):
        if not any(p.x == q.x and p.y == q.y and p.z == q.z for q in self._points): self._points.append(p)

    def get_perimeter(self): return perimeter(self._points)
    p1 = Point3D(5,7,8)
    p2 = Point3D(5,7,8)
    p3 = Point3D(5,7,8)

    print("Triangulo:",Point3D[p1,p2,p3])
   

   
