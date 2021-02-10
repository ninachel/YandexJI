n = int(input())
result = set()
for i in range(n):
    el = int(input())
    if el not in result:
        result.add(el)
        print(el, end='\n')
