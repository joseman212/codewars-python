# Joseman212
# 8/16/2020


def shortcut(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    ans = ''
    for s in s:
        if s not in vowels:
            ans += s
    return ans
