import string

intro = input("Введи шось: ")
first, last = intro.split("-")


first_index = string.ascii_letters.index(first)
last_index = string.ascii_letters.index(last)
result = string.ascii_letters[first_index:last_index + 1]

print(result)
