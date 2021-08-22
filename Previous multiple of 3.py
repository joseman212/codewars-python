# joseman212
# 8/22/2021


def prev_mult_of_three(n):
    while n > 0:
        if n % 3 == 0:
            return n
        n = n // 10
    return None
