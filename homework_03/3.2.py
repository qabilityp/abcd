def move_element(user_input):
    if not user_input:
        print(user_input)
    else:
        a = user_input.pop()
        user_input.insert(0, a)
        print(user_input)

move_element([12, 3, 4, 10])
move_element([1])
move_element([])
move_element([12, 3, 4, 10, 8])
move_element([1, 2])




