numb = int(input("Введи число від 0 до 8640000: "))

day = 24 * 60 * 60
days = numb // 86400
remainder = numb % 86400
hours = remainder // 3600
remainder_2 = remainder % 3600
minutes = remainder_2 // 60
remainder_3 = remainder_2 % 60

print(f"{days} дні, {hours}:{minutes}:{remainder_3}")
