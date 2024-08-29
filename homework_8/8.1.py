def add_one(some_list) -> list[int]:
    some_list_join = int(''.join(map(str, some_list)))
    some_list_join_2 = some_list_join + 1
    return [int(i) for i in str(some_list_join_2)]


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
