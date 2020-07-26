# Joseman212
# 5/31/2020


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if(mpg * fuel_left >= distance_to_pump):
        return True
    return False
