class Calc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        if self.c == "+":
            return self.a + self.b

    def subtraction(self):
        if self.c == "-":
            return self.a - self.b

    def division(self):
        try:
            if self.c == "/":
                return self.a / self.b
        except ZeroDivisionError:
            return "Деление на ноль запрещено"

    def multiplication(self):
        if self.c == "*":
            return self.a * self.b


try:
    while True:
        try:
            c = input("Введите операцию: ")
            if c not in ("+", "-", "*", "/"):
                raise ValueError("Неподдерживаемая операция")
            try:
                a_str, b_str = input("Введите два числа через пробел: ").split()
                a = int(a_str)
                b = int(b_str)
                calc = Calc(a, b, c)
                print(calc.division())
                break
            except ValueError:
                print("Вы ввели строковое значение")

        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
finally:
    print("Спасибо за использование нашей программы")
