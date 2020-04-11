# joseman212
# 4/11/20

def year_days(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f'{year} has 366 days'
            return f'{year} has 365 days'
        return f'{year} has 366 days'
    return f'{year} has 365 days'