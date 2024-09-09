def common_elements() -> set[int]:
    a_multiple_3 = list(range(0, 101, 3))
    b_multiple_5 = list(range(0, 101, 5))
    a_set = set(a_multiple_3)
    b_set = set(b_multiple_5)
    intersection_ab = a_set.intersection(b_set)
    return intersection_ab


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
