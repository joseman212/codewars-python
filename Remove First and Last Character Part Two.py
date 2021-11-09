#joseman212
#11/8/2021


def array(string):
    nString = ''
    myString = string.split(',')
    if len(myString) > 2:
        myString.pop(0) and myString.pop(-1)
        for m in range(len(myString)):
            nString += myString[m] + ' '
        return nString.strip()
    return None
