import math

class Kalkulator:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.a + other.a)
        else:
            print("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.a - other.a)
        else:
            print("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.a * other.a)
        else:
            print("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.a / other.a)
        else:
            print("Unsupported operand type for /")

    def __pow__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(pow(self.a, other.a))
        else:
            print("Unsupported operand type for ^")

    def log(self, other):
        if isinstance(other, Kalkulator):
            if self.a <= 0 or other.a <= 0 or other.a == 1:
                return "Invalid input for logarithm"
            return Kalkulator(math.log(self.a, other.a))
        else:
            return "Unsupported operand type for log"

    def __str__(self):
        return f"{self.a}"

print(f"{'=' * 10} Kalkulator Sederhana {'=' * 10}")
print("1. +     3. -    5. *    7. Lainnya untuk keluar\n2. /     4. ^    6. log")
number1 = Kalkulator(int(input("a: ")))

while(True):
    operator = input("operator: ")
    if operator not in ('+', '-', '*', '/', '^', "log"):
        break

    number2 = Kalkulator(int(input("b: ")))
    if operator == "+":
        number1 += number2
    elif operator == "-":
        number1 -= number2
    elif operator == "*":
        number1 *= number2
    elif operator == "/":
        number1 /= number2
    elif operator == "^":
        number1 **= number2
    elif operator == "log":
        result = number1.log(number2)
        if isinstance(result, str):
            print(result)
        else:
            number1 = result
            print(f"a: {number1}")
        continue

    print(f"a: {number1}")