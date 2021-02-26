# joseman212
# 2/25/2021


def two_highest(arg1):
    unique = set(arg1)
    if len(unique) == 0:
        return []
    largest = max(unique)
    unique.remove(largest)
    if len(unique) == 0:
        return [largest]
    else:
        nextLargest = max(unique)
        return [largest, nextLargest]
