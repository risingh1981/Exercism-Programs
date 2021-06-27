from math import sqrt

def score(x, y):
    dist = sqrt((x ** 2) + (y ** 2))
    if (dist <= 1):
        return 10
    elif (dist <= 5):
        return 5
    elif (dist <=10):
        return 1
    else:
        return 0
