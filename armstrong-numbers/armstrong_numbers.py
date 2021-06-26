def is_armstrong_number(number):
    length = len(str(number))
    sum = 0
    toManipulate = number
    while (toManipulate >= 1):
        sum += (toManipulate % 10) ** length
        toManipulate = toManipulate // 10
    return True if (sum == number) else False
    