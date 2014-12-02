#!/usr/bin/env python
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        #FOIL
        f = self.real * other.real
        o = self.real * other.imaginary
        i = self.imaginary * other.real
        l = self.imaginary * other.imaginary
        real = f - l
        imaginary = o + i
        return Complex(real, imaginary)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.real * other.imaginary - self.imaginary * other.real) / denominator
        return Complex(real, -imaginary)

    def __str__(self):
        sign = "+" if self.imaginary >= 0 else "-"
        return "{}{}{}i".format(self.real, sign, abs(self.imaginary))

    def get_conjugate(self):
        return Complex(self.real, -self.imaginary)

    def get_modulus(self):
        # pythag: a^2 * b^2 = c^2
        # c = sqrt(a**2 + b**2)
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def get_argument(self):
        return math.atan2(self.imaginary, self.real)

def main():
    test = Complex(1, 2)
    test2 = Complex(3, 4)
    print("Test complex: " + str(test))
    print("Test conjugate: " + str(test.get_conjugate()))
    print("Test modulus: " + str(test.get_modulus()))
    print("Test argument: " + str(test.get_argument()))
    print("Test addition: {} + {} = {}".format(test, test2, test+test2))
    print("Test subtraction: {} - {} = {}".format(test, test2, test-test2))
    print("Test multiplication: {} * {} = {}".format(test, test2, test * test2))
    print("Test division: {} / {} = {}".format(test, test2, test/test2))

if __name__ == "__main__":
    main()
