class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def get_square(self) -> float:
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other: object) -> 'Rectangle':
        if isinstance(other, Rectangle):
            total_square = self.get_square() + other.get_square()
            return Rectangle(self.width, total_square / self.width)
        return NotImplemented

    def __mul__(self, n: float) -> 'Rectangle':
        if isinstance(n, (int, float)):
            return Rectangle(self.width, self.height * n)
        return NotImplemented

    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height}, square={self.get_square()})'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print(r1)
print(r2)
print(r3)
print(r4)