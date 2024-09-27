from math import gcd


class Fraction:
    def __init__(self, a: int, b: int) -> None:
        if b == 0:
            raise ValueError('Знаменник не може бути рівним 0')
        common_divisor = gcd(a, b)
        self.a = a // common_divisor
        self.b = b // common_divisor

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        if isinstance(other, Fraction):
            return Fraction(self.a * other.a, self.b * other.b)
        return NotImplemented

    def __add__(self, other: 'Fraction') -> 'Fraction':
        if isinstance(other, Fraction):
            num = self.a * other.b + other.a * self.b
            denom = self.b * other.b
            return Fraction(num, denom)
        return NotImplemented

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        if isinstance(other, Fraction):
            num = self.a * other.b - other.a * self.b
            denom = self.b * other.b
            return Fraction(num, denom)
        return NotImplemented

    def __eq__(self, other: 'Fraction') -> bool:
        if isinstance(other, Fraction):
            return self.a == other.a and self.b == other.b
        return NotImplemented

    def __gt__(self, other: 'Fraction') -> bool:
        if isinstance(other, Fraction):
            return (self.a * other.b) > (other.a * self.b)
        return NotImplemented

    def __lt__(self, other: 'Fraction') -> bool:
        if isinstance(other, Fraction):
            return (self.a * other.b) < (other.a * self.b)
        return NotImplemented

    def __str__(self) -> str:
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
