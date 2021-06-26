def classify(number):
    aliquotsum = 0
    if (not(isinstance(number, int))):
        raise AssertionError("Input value must be an integer.")
    elif (number < 1):
        raise ValueError("Input value must be greater than or equal to 1.")
    for i in range(1,number):
        if (number % i == 0):
            aliquotsum += i
    if (aliquotsum == number):
        return "perfect" 
    elif (aliquotsum < number):
        return "deficient"
    else:
        return "abundant"

