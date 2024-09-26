import string

user_input = input()
user_input_2 = "".join(i for i in user_input if i not in string.punctuation)
user_input_3 = user_input_2.split()
user_input_4 = "".join(word[0].upper() + word[1:].lower() for word in user_input_3)
user_input_5 = '#' + user_input_4
if len(user_input) > 140:
    print(user_input_5[:140])
else:
    print(user_input_5)

