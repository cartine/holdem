class Rectangle:
    def __init__(self, length, height):
        self.LENGTH = length
        self.HEIGHT = height

    def __str__(self):
        return f"Rectangle with length={self.LENGTH} and height={self.HEIGHT}"

    def area(self):
        return self.LENGTH * self.HEIGHT

    def perimeter(self):
        return 2 * (self.HEIGHT + self.LENGTH)

    def compare_area(self, rectangle):
        return self.area() - rectangle.area()


if __name__ == '__main__':
    r1 = Rectangle(3, 4)
    print(r1)
    print(f"area: {r1.area()}")
    print(f"perimeter: {r1.perimeter()}")
    print()
    r2 = Rectangle(2, 9)
    print(r2)
    print(f"area: {r2.area()}")
    print(f"perimeter: {r2.perimeter()}")
    print()
    print(f"The difference in area between the 2 rectangles is: {r1.compare_area(r2)}")
