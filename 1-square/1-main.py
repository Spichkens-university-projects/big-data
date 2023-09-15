from Circle import Circle
from Rectangle import Rectangle
from Triangle import Triangle
from CLI.CLI import CLI
import os


def main():
    cli = CLI("Площадь фигур. Выберите фигуру:", ["Круг", "Треугольник", "Прямоугольник"])

    if cli.selected_option == "Круг":
        print(Circle().calculate_square())

    elif cli.selected_option == "Треугольник":
        print(Triangle().calculate_square())

    elif cli.selected_option == "Прямоугольник":
        print(Rectangle().calculate_square())


if __name__ == "__main__":
    while True:
        main()
        input()
        os.system("cls")
