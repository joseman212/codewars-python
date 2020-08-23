# Joseman212
# 8/23/2020

import re


def get_number_from_string(string):
    return int("".join(re.findall(r'\d+', string)))
