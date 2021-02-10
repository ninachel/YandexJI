n = int(input())
cur_len = 0
max_len = 0
for i in range(n):
    el = int(input())
    if el == 1:
        cur_len += 1
    else:
        if cur_len > max_len:
            max_len = cur_len
        cur_len = 0
max_len = max(cur_len, max_len)
print(max_len)
