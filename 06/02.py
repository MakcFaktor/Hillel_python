numb = int(input("Введи число від 0 до 8640000: "))

day = 24 * 60 * 60
days = numb // 86400
remainder = numb % 86400
hours = remainder // 3600
remainder_2 = remainder % 3600
minutes = remainder_2 // 60
remainder_3 = remainder_2 % 60

word = ""

if days == 0:
    word = "днів"
elif days % 10 == 1 and days != 11:
    word = "день"
elif 2 <= days % 10 <= 4 and not (11 <= days <= 14):
    word = "дні"
else:
    word = "днів"

h = str(hours).zfill(2)
m = str(minutes).zfill(2)
s = str(remainder_3).zfill(2)
print(f"{days} {word}, {h}:{m}:{s}")
