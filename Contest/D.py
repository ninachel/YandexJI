import itertools


def valid_parentheses(seq):
    pass


n = int(input())
sample = "(" * n + ")" * n
options = list(itertools.permutations(sample))
for x in options:
    if valid_parentheses(x):
        print(''.join(x))
