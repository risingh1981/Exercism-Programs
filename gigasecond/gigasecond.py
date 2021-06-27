from datetime import timedelta
def add(moment):
    gigaSecond = 10 ** 9
    newTime = moment + timedelta(seconds = gigaSecond)
    return newTime
