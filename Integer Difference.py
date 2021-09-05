# joseman212
# 9/5/2021


def int_diff(lst, n):
    ans = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if abs(lst[i] - lst[j]) == n:
                ans += 1
    return ans
