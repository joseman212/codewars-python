# Joseman212
# 7/13/2020


def difference_in_ages(ages):
    sorted = ages.sort()
    low = ages[0]
    high = ages[-1]
    diff = high - low
    return (low, high, diff)
