import string

user_input = input()
star_char, end_char = user_input.split('-')
star_index = string.ascii_letters.index(star_char)
end_index = string.ascii_letters.index(end_char)
string_letters = string.ascii_letters[star_index:end_index+1]
print(string_letters)

