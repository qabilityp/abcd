def split_list(user_input):
    if len(user_input) < 2:
        print(user_input)
    elif len(user_input) > 2:
        a = user_input.pop()
        user_input.insert(0, a)
        print(user_input)
    else:
        print(user_input)
