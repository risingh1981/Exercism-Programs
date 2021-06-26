def convert(number):
    return "".join(val for key, val in {3:"Pling", 5:"Plang", 7:"Plong"}.items() if (number % key == 0)) or str(number)
