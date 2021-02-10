def anagrams(str1, str2):
    if len(str1) != len(str2):
        return 0
    str1_letters = dict()
    str2_letters = dict()
    for c in str1:
        if c in str1_letters:
            str1_letters[c] += 1
        else:
            str1_letters[c] = 1
    for c in str2:
        if c in str2_letters:
            str2_letters[c] += 1
        else:
            str2_letters[c] = 1
    return str1_letters == str2_letters


first = input()
second = input()
if anagrams(first, second):
    print(1)
else:
    print(0)
