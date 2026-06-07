def calculate(num_1, num_2, action):
    if action == "+":
        return num_1 + num_2
    elif action == "-":
        return num_1 - num_2
    elif action == "*":
        return num_1 * num_2
    elif action == "/":
        if num_2 != 0:
            return num_1 / num_2
        else:
            return "Помилка: ділення на нуль!"
    else:
        return "Невідома дія!"


while True:
    action = input("Введи дію (+, -, *, /, вихід): ")
    if action == "вихід":
        print("До побачення!")
        break

    num_1 = int(input("Перша цифра: "))
    num_2 = int(input("Друга цифра: "))

    result = calculate(num_1, num_2, action)
    print(f"Результат: {result}")
