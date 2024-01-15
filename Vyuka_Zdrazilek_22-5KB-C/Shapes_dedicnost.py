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

    def content(self):
        return self.b * self.getA()

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


if __name__ == "__main__":
    rec = Rectangle()
    rec1 = Rectangle(5, 6)

    cb = Cube(5)
    print(cb.volume())
    cb.print()