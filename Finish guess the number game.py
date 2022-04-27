
# Joseman212
# 4/27/2022
# Finish guess the number game


class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives < 1:
            raise ValueError('Omae wa mo shindeiru')
        elif n == self.number:
            return True
        elif n != self.number:
            self.lives -= 1
            return False
