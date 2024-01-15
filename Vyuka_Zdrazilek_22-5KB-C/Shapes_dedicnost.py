class Shape:
    def __init__(self):
        print("Vykresluji obrazec")

class Square(Shape):
    def __init__(self, a=0):
        super().__init__()
        self.a = a
        print("Vytvarime ctverec")

    def content(self):
        return self.a * self.a

    def perimeter(self):
        return self.a * 4

    def getA(self):
        return self.a

    def print(self):
        print(f"Ctverec se stranami o delce {self.a}")

class Rectangle(Square):
    def __init__(self, a=0, b=0):
        super().__init__(a)
        self.b = b
        print("Vytvarime obdelnik")

    def perimeter(self):
        return 2 * self.b + 2 * self.getA()

    def print(self):
        print(f"Obdelnik se stranami o delce {self.getA()} a {self.b}")

class Cube(Square):
    def __init__(self, a=0):
        super().__init__(a)
        print("Vytvarime kostku")

    def volume(self):
        return self.content() * self.getA()

    def print(self):
        print(f"Kostka se stranami o delce {self.getA()}")

class Block(Rectangle):
    def __init__(self, a=0, b=0, c=0):
        super().__init__(a, b)
        self.c = c
        print("Vytvarime kvadr")

    def volume(self):
        return self.content() * self.c

    def print(self):
        print(f"Kvadr se stranami o delce {self.getA()}, {self.b} a {self.c}")

class Circle(Shape):
    def __init__(self, r=0):
        self.r = r
        print("Vytvarime kruh")

    def content(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r

    def print(self):
        print(f"Kruh s polomerem {self.r}")

class Cylinder(Circle):
    def __init__(self, r=0, h=0):
        super().__init__(r)
        self.h = h
        print("Vytvarime valec")

    def volume(self):
        return self.content() * self.h

    def print(self):
        print(f"Valec s polomery {self.r} a vyskou {self.h}")

class Ball(Circle):
    def __init__(self, r=0):
        super().__init__(r)
        print("Vytvarime kouli")

    def volume(self):
        return (4/3) * 3.14 * (self.r ** 3)

    def print(self):
        print(f"Koule s polomerem {self.r}")


if __name__ == "__main__":
    rec = Rectangle()
    rec1 = Rectangle(5, 6)
    cb = Cube(5)
    block = Block(2, 3, 4)
    circle = Circle(3)
    cylinder = Cylinder(5, 10)
    ball = Ball(5)
    
    print(cb.volume())
    rec1.print()
    cb.print()
    block.print()
    circle.print()
    cylinder.print()
    ball.print()
