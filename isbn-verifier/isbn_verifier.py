def is_valid(isbn):
    cleaned_up = clean_up(isbn)
    if cleaned_up:
        return check_digit(cleaned_up[:-1]) == cleaned_up[-1]
    else:
        return False

# Returns false if in process of clean-up it finds ISBN is not valid.
def clean_up(isbn):
    extracted_isbn = ""
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    idx = 0
    for char in isbn:
        if (idx <= 8) and (char in digits):
            extracted_isbn += char
        elif (idx == 9) and ((char in digits) or (char == "X")):
            extracted_isbn += char
        else:
            return False
        idx += 1
    return extracted_isbn

# Check function for ISBN. Returns the check digit of ISBN given first 9 digits.
def check_digit(ISBN):
    i = 1
    sum = 0
    for char in ISBN:
        sum = sum + i*int(char)
        i += 1
    return "X" if ((sum % 11) == 10) else str((sum % 11) == 10)

