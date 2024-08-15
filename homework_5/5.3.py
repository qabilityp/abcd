import string

user_input = input().title()
user_input_2 = "".join(i for i in user_input if i not in string.punctuation and i != ' ')
user_input_3 = '#' + user_input_2
if len(user_input) > 140:
    print(user_input_3[:141])
else:
    print(user_input_3)

