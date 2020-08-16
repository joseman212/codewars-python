# Joseman212
# 8/16/2020


def is_vow(inp):
    ans = []
    for i in inp:
        if i == 97:
            ans.append('a')
        elif i == 101:
            ans.append('e')
        elif i == 105:
            ans.append('i')
        elif i == 111:
            ans.append('o')
        elif i == 117:
            ans.append('u')
        else:
            ans.append(i)
    return ans
