# jose Perez
# 7/10/2020


def find_multiples(integer, limit):
    ans = []
    for n in range(integer, limit + 1, integer):
        ans.append(n)
    return ans
