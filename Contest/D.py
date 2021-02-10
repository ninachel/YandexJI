def valid_parentheses(s, l, r, pairs):
    if l == pairs and r == pairs:
        print(s)
    else:
        if l < pairs:
            valid_parentheses(s + '(', l + 1, r, pairs)
        if r < l:
            valid_parentheses(s + ')', l, r + 1, pairs)


n = int(input())
valid_parentheses('', 0, 0, n)
