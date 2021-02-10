n = int(input())
hash_map = dict()
for i in range(n):
    el = int(input())
    if el not in hash_map:
        hash_map[el] = 1
        print(el, end='\n')
