n = int(input())
result = []
for i in range(n):
    el = int(input())
    if el not in result:
        result.append(el)
        print(el, end='\n')
