user_input = input()
user_input_2 = user_input.split()
if len(user_input_2) % 2 == 0:
    a = user_input_2[(len(user_input_2) // 2):]
    b = user_input_2[:len(user_input_2) // 2]
    print([b] + [a])
elif len(user_input_2) % 2 != 0:
    a = user_input_2[len(user_input_2) // 2 + 1:]
    b = user_input_2[:len(user_input_2) // 2 + 1]
    print([b] + [a])
else:
    print([b] + [a])
