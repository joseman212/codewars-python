# Joseman212
# 8/23/2020


def duck_duck_goose(players, goose):
    while len(players) < goose:
        goose = goose - len(players)
    return players[goose - 1].name
