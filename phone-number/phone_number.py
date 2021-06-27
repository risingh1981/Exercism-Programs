class PhoneNumber:
    def __init__(self, number):
        self.number, self.area_code = PhoneNumber.cleanupAndextractor(number)
        

    def pretty(self):
        return "("+ self.area_code + ")-" + self.number[3:6] + "-" + self.number[6:]
    

    @staticmethod
    def cleanupAndextractor(number):
        digits =["0","1","2","3","4","5","6","7","8","9"]
        cleaned_up = ""
        for i in range(len(number) - 1, -1, -1):
            if number[i] in digits:
                cleaned_up = number[i] + cleaned_up
        # Reduce number down to 10 digits
        if (len(cleaned_up) < 10) or (len(cleaned_up) > 11):
            raise ValueError("Incorrect number of digits in number")
        elif (len(cleaned_up) == 11) and (cleaned_up[0] == "1"):
            cleaned_up = cleaned_up[1:]
        elif (len(cleaned_up) == 11):
            raise ValueError("Country code must be a 1")
        # At this point, cleaned_up contains a 10 digit number.
        # Extract area code and check validity
        area_code = cleaned_up[:3]
        if (area_code[0] == "0") or (area_code[0] == "1"):
            raise ValueError("Area code may not start with a 0 or 1.")
        # Check that exchange code doesn't start with 1.
        if (cleaned_up[3] == "1") or (cleaned_up[3] == "0"):
            raise ValueError("Exchange code may not start with 0 or 1.")
        # Area code and number are ready to be returned by the function
        return cleaned_up, area_code



