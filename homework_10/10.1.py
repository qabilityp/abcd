from typing import Callable, Iterator
from inspect import isgenerator


def pow_(x: int) -> int:
    return x ** 2


def some_gen(begin: int, end: int, func: Callable[[int], int]) -> Iterator[int]:
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    current = begin
    yield current

    for i in range(end - 1):
        current = func(current)
        yield current


gen = some_gen(2, 4, pow_)
assert isgenerator(gen), 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
