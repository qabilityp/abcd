def sort_null(a):
    for i in a:
        if i == 0:
            a.remove(i)
            a.append(i)
    print(a)

sort_null([0, 1, 0, 12, 3])
sort_null([0])
sort_null([1, 0, 13, 0, 0, 0, 5])
sort_null([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0])
