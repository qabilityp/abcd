def split_list(user_input_2):
    if len(user_input_2) % 2 == 0:
        a = user_input_2[(len(user_input_2) // 2):]
        b = user_input_2[:len(user_input_2) // 2]
        print([b] + [a])
    else:
        a = user_input_2[len(user_input_2) // 2 + 1:]
        b = user_input_2[:len(user_input_2) // 2 + 1]
        print([b] + [a])

split_list([1, 2, 3, 4, 5, 6])
split_list([1, 2, 3])
split_list([1, 2, 3, 4, 5])
split_list([1])
split_list([])
