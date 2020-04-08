# joseman212
# 4/8/2020

def elevator(left, right, call):
    if abs(call-right) <= abs(call-left):
        return "right"
    return "left"
