def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        temp = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = temp
    return lst


a = [9, 5, 4, 7, 3, 2, 1]
print(selection_sort(a))
