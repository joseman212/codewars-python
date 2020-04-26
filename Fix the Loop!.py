# joseman212
# 4/25/2020


def list_animals(animals):
    ans = ''
    for count, el in enumerate(animals, start=1):
        ans += f'{count}. {el}\n'
    return ans
