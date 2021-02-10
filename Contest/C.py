n = int(input())
last_printed = 0
for i in range(n):
    el = int(input())
    if i == 0:
        print(el)
        last_printed = el
    else:
        if el != last_printed:
            print(el)
            last_printed = el
    if i == n - 1:
        