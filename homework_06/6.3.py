while True:
    user_input = input()
    while len(user_input) > 1:
        digits = list(map(int, str(user_input)))
        product = 1
        for i in digits:
            product *= i
        user_input = str(product)
    print(product)