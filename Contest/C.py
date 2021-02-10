n = int(input())
nums = set()
for i in range(n):
    el = int(input())
    nums.add(el)
for el in sorted(list(nums)):
    print(el, end='\n')
