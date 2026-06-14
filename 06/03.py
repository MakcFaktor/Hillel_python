numb = input("Введи цифри: ")
result = 1
for char in numb:
    result *= int(char)

while result > 9:
    temp = str(result)
    result = 1
    for char in temp:
        result *= int(char)

print(result)
