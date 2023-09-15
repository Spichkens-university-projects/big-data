from CLI.CLI import CLI
import os


class Maths:
    def __init__(self):
        self.second = None
        self.first = None

    def set_two_args(self):
        self.first = float(input("Первое число >> "))
        self.second = float(input("Второе число >> "))

    def set_one_arg(self):
        self.first = float(input("Xисло >> "))

    def add(self):
        return self.first + self.second

    def subtraction(self):
        return self.first - self.second

    def div_with_mod(self):
        return self.first / self.second

    def div(self):
        return self.first // self.second

    def my_pow(self):
        return pow(self.first, self.second)

    def my_abs(self):
        return abs(self.first)


def main():
    maths = Maths()
    cli = CLI("Выберите действие:",
              ["Сложение", "Вычитание", "Деление с остатком", "Целочисленное деление", "Модуль", "Степень"])

    if cli.selected_option == "Модуль":
        maths.set_one_arg()
        maths.my_abs()
    else:
        maths.set_two_args()

        if cli.selected_option == "Сложение":
            print(maths.add())
        elif cli.selected_option == "Вычитание":
            print(maths.subtraction())
        elif cli.selected_option == "Деление с остатком":
            print(maths.div_with_mod())
        elif cli.selected_option == "Целочисленное деление":
            print(maths.div())
        elif cli.selected_option == "Степень":
            print(maths.my_pow())


if __name__ == "__main__":
    while True:
        main()
        input()
        os.system("cls")
