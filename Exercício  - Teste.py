from math import sqrt

class Point3D:
    def __init__(self, x, y, z): self.x, self.y, self.z = x, y, z
    def about(self): return f"{self.x}-{self.y}-{self.z}"
    def distance(self, o): return sqrt((self.x - o.x)**2 + (self.y - o.y)**2 + (self.z - o.z)**2)

def perimeter(pts): return sum (pts[i].distance(pts[i+1]) for i in range(len(pts)-1)) if len(pts) > 1 else 0
def middle_point(a,b): return Point3D((a.x+b.x)/2, (a.y+b.y)/2, (a.z+b.z)/2)


if __name__ == '__main__':
    p1, p2, p3 = Point3D(0,0,0), Point3D(1,1,1), Point3D(2,2,2)
    print("Perímetro:", perimeter([p1, p2, p3]))
    print("Ponto médio:", middle_point(p1, p3).about())
