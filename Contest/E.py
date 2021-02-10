def anagrams(str1, str2):
    if len(str1) != len(str2):
        return 0
    for c in str1:
        if c not in str2:
            return 0
    return 1


first = input()
second = input()
print(anagrams(first, second))
