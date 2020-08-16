# Joseman212
# 8/16/2020


def next_item(xs, item):
    xs = iter(xs)
    if item in xs:
        return next(xs, None)
