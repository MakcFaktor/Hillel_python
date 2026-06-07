def split_list(lst):
    n = len(lst)
    if n == 0:
        return [[], []]
    mid = (n + 1) // 2
    return [lst[:mid], lst[mid:]]


print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))
