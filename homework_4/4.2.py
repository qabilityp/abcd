def summ_paired_indexes(a):
    if not a:
        print(0)
        return
    b = []
    for i in range(0, len(a), 2):
        b.append(a[i])
    sum_b = sum(b)
    print (sum_b * a[-1])

summ_paired_indexes([1, 3, 5])
summ_paired_indexes([6])
summ_paired_indexes([])
