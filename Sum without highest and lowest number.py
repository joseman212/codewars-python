# Joseman212
# 8/23/2020


def sum_array(arr):
    if arr == None or arr == [] or len(arr) < 3:
        return 0
    else:
        arr = sorted(arr)
        return sum(arr[1:-1])
