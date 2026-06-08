str_1 = input("Введи будь яке речення: ")

clean = ""

for char in str_1:
    if char.isalpha() or char.isspace():
        clean += char

result = "#" + clean.title().replace(' ', '')
print(result[:140])
