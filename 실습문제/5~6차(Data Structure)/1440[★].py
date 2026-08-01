# <문제>
def reverse_string():
    pass


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH

#<solve>
def reverse_string(text):
    return text[::-1]


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
