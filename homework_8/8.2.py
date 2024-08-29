def is_palindrome(text: str) -> bool:
    text_lower = ''.join(char.lower() for char in text if char if char.isalnum())
    return text_lower == text_lower[::-1]


assert is_palindrome('A man, a plan, a canal: Panama'), 'Test1'
assert not is_palindrome('0P'), 'Test2'
assert is_palindrome('a.'), 'Test3'
assert not is_palindrome('aurora'), 'Test4'
print("ОК")
