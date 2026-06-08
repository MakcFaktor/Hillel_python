import keyword

str_1 = input("Веди імя змінної: ")

is_valid = True

if str_1[0].isdigit():
    is_valid = False

for char in str_1:
    if not (char.isalpha() or char.isdigit() or char == '_'):
        is_valid = False
    if char.isupper():
        is_valid = False


if "__" in str_1:
    is_valid = False
if str_1 in keyword.kwlist:
    is_valid = False

print(is_valid)
