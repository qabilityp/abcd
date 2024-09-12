def is_even(number: int) -> bool:
    return (number & 1) == 0


assert is_even(2494563894038**2), 'Test1'
assert not is_even(1056897**2), 'Test2'
assert not is_even(24945638940387**3), 'Test3'
