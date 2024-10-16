# Zadanie 1
# Stwórz klasę implementującą liczby zespolone oraz przeciąż dla niej operatory dodawania i odejmowania

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        if self.imag < 0:
            return f"{self.real} - {-self.imag}i"
        else:
            return f"{self.real} + {self.imag}i"


z1 = ComplexNumber(3, 4)  # 3 + 4i
z2 = ComplexNumber(1, -2)  # 1 - 2i

z3 = z1 + z2
print(z3)  # 4 + 2i

z4 = z1 - z2
print(z4)  # 2 + 6i
