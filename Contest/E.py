def anagrams(str1, str2):
    if len(str1) != len(str2):
        return 0
    flag = 0
    for c in str1:
        if c in str2:
            flag = 1
        else:
            return 0
    return flag


first = input()
second = input()
print(anagrams(first, second))
