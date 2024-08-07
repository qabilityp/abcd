user_input = input()
user_split = user_input.split()
a = int(user_split[0])
b = int(user_split[2])
c = user_split[1]
if c == '+':
    print (a + b)
if c == '-':
    print (a - b)
if c == '*':
    print (a * b)
if c == '/' and b != 0:
    print (a / b)