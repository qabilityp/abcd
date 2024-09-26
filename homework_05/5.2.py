while True:
    a = int(input())
    c = input()
    b = int(input())
    if c == '+':
        print(a + b)
    if c == '-':
        print(a - b)
    if c == '*':
        print(a * b)
    if c == '/' and b != 0:
        print(a / b)

    user_input_2 = input()
    if user_input_2 == 'yes':
        continue
    else:
        break



