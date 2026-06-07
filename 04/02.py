def sum_multiply(lst):
    if not lst:
        return 0
    even_sum = sum(lst[::2])
    return even_sum * lst[-1]


print(sum_multiply([0, 1, 7, 2, 4, 8]))
print(sum_multiply([1, 3, 5]))
print(sum_multiply([6]))
print(sum_multiply([]))
