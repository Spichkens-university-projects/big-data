from Shape import Shape


class Triangle(Shape):
    def __init__(self):
        self.base = float(input("Сторона >> "))
        self.height = float(input("Высота >> "))

    def calculate_square(self):
        return self.height * self.base / 2
