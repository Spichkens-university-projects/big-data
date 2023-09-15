from Shape import Shape
import math


class Circle(Shape):
    def __init__(self):
        self.radius = float(input("Радиус >> "))

    def calculate_square(self):
        return math.pi * pow(self.radius, 2)
