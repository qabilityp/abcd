import string
import keyword
def variable_name(a):
    if a[0].isdigit():
        print(False)
        return
    if any(i.isupper() for i in a):
        print(False)
        return
    symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~'
    if any(i in symbols for i in a):
        print(False)
        return
    c = a.count('_')
    if c > 1:
        print(False)
        return
    if a in keyword.kwlist:
        print(False)
        return
    print(True)

variable_name("variable1")
variable_name("1variable")
variable_name("Variable")
variable_name("var_iable")
variable_name("var__iable")
variable_name("for")
