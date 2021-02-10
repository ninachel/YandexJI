import itertools


def valid_parentheses(seq):
    stack = []
    for i in range(len(seq)):
        if seq[i] == ')':
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(seq[i])
    if not stack:
        return True
    return False


n = int(input())
sample = "(" * n + ")" * n
options = list(set(itertools.permutations(sample)))
result = []
for x in options:
    if valid_parentheses(x):
        result.append(''.join(x))
for x in sorted(result):
    print(x)
