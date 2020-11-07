# Joseman212
# 11/6/2020


def pythagorean_triple(integers):
    c = max(integers)
    integers.remove(c)
    return c ** 2 == (integers[0] ** 2) + (integers[1] ** 2)
