user_input = input()
user_input_2 = user_input.split()
if len(user_input_2) < 2:
    print(user_input_2)
elif len(user_input_2) > 2:
    a = user_input_2.pop()
    user_input_2.insert(0, a)
    print(user_input_2)
else:
    print(user_input_2)