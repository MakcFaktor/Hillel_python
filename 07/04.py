def common_elements():
    num_1 = [num for num in range(10) if num % 3 == 0]
    num_2 = [num for num in range(10) if num % 5 == 0]
    set_1 = set(num_1)
    set_2 = set(num_2)

    return set_1 & set_2
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
