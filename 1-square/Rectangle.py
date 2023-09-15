from Shape import Shape


class Rectangle(Shape):
    def __init__(self):
        self.width = float(input("Ширина >> "))
        self.height = float(input("Высота >> "))

    def calculate_square(self):
        return self.height * self.width
