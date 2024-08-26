def correct_sentence(text):
    sentence_cptl = text[0].upper() + text[1:]
    if '.' not in text[-1]:
        return sentence_cptl + '.'
    else:
        return sentence_cptl

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
