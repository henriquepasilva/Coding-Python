import math

class Point3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

if __name__ == '__main__':
    def calculate_distance(p1, p2):
       dx = p1.x
       
        distance = math.sqrt(dx**2 + dy**2 + dz**2)
        return distance

    p1 = Point3D(0, 2, 3)
    p2 = Point3D(0, 4, 6)

    distance = calculate_distance(p1, p2)
    print("Distance between p1 and p2:", distance)
