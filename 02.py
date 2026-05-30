number = int(input("Введіть число: "))

print("Квадрат числа:", number * number)

#-------------------------------------------------------------

num_1 = int(input("Введіть перше число: "))
num_2 = int(input("Введіть друге число: "))
num_3 = int(input("Введіть третє число: "))

print("Середнє:", (num_1 + num_2 + num_3) / 3)

#-------------------------------------------------------------

minutes = int(input("Введіть кількість хвилин: "))
hours = minutes // 60
remaining_minutes = minutes % 60

print("Годин:", hours)
print("Хвилин:", remaining_minutes)

#-------------------------------------------------------------

price = float(input("Введіть ціну: "))
discount = float(input("Введіть знижку (%): "))

print("Ціна зі знижкою:", price - (price * discount / 100))

#-------------------------------------------------------------

num = int(input("Введіть число: "))
last_digit = abs(num) % 10

print("Остання цифра:", last_digit)

#-------------------------------------------------------------

length = float(input("Введіть довжину: "))
width = float(input("Введіть ширину: "))

perimeter = 2 * (length + width)

print(f"Периметр: {perimeter:.0f}")

#-------------------------------------------------------------

numb = int(input("Введіть 4-значне число: "))

d1 = numb // 1000
d2 = (numb // 100) % 10
d3 = (numb // 10) % 10
d4 = numb % 10

print(d1)
print(d2)
print(d3)
print(d4)