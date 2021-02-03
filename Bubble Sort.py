def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        flag = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                flag = True
        if not flag:
            break
    return lst


a = [1, 2, 3, 4, 5, 6, 7, 8]
print(bubble_sort(a))
