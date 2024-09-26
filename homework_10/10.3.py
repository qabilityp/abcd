def is_even(digit: int) -> bool:
    """ Перевірка чи є парним число """
    return digit % 2 == 0


assert is_even(2), 'Test1'
assert not is_even(5), 'Test2'
assert is_even(0), 'Test3'
print('OK')
