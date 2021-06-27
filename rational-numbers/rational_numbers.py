from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        numer, denom = Rational.lowest_terms(numer,denom)
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return ((self.numer == other.numer) and (self.denom == other.denom))
    
    def __str__(self) -> str:
        return '{}/{}'.format(self.numer, self.denom)

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        lcm = Rational.lcm(self.denom,other.denom)
        numerSum = self.numer*(lcm/self.denom) + other.numer*(lcm/other.denom)
        numerSum, denomSum = Rational.lowest_terms(numerSum, lcm)
        return Rational(numerSum, denomSum)

    def __sub__(self, other):
        lcm = Rational.lcm(self.denom,other.denom)
        numerSub = self.numer*(lcm/self.denom) - other.numer*(lcm/other.denom)
        numerSub, denomSub = Rational.lowest_terms(numerSub, lcm)
        return Rational(numerSub, denomSub)

    def __mul__(self, other):
        numerMul = self.numer * other.numer
        denomMul = self.denom * other.denom
        numerMul, denomMul = Rational.lowest_terms(numerMul, denomMul)
        return Rational(numerMul, denomMul)

    def __truediv__(self, other):
        if ((self.denom * other.numer) != 0):
            numerDiv = self.numer * other.denom
            denomDiv = self.denom * other.numer
            numerDiv, denomDiv = Rational.lowest_terms(numerDiv, denomDiv)
            return Rational(numerDiv, denomDiv)
        else:
            raise ZeroDivisionError("Cannot divide due to divide by zero error.")

    def __abs__(self):
        return Rational(abs(self.numer),abs(self.denom))

    def __pow__(self, power):
        numerPow = self.numer ** abs(power)
        denomPow = self.denom ** abs(power)
        if (power < 0):
            numerPow, denomPow = denomPow, numerPow
        return Rational(numerPow, denomPow)

    def __rpow__(self, base):
        result = (base ** self.numer) ** (1/self.denom)
        return round(result,8)
        

    @staticmethod
    def recursiveGCD(a,b):
        if ((a == 0) or (b == 0)):
            return max(abs(a),abs(b))
        # Calculate Remainder:
        r = a % b
        # Recursive Base Case:
        if (r == 0):
            return abs(b)
        # Recursive Call
        return Rational.recursiveGCD(b, r)
        
    @staticmethod
    def lcm(a,b):
        if (a>b):
            start = a
        else:
            start = b
        for i in range(start, a*b + 1):
            if (i % a == 0) and (i % b == 0):
                return i
    
    @staticmethod
    def lowest_terms(numer, denom):
        if (numer < 0) and (denom < 0):
            numer,denom = abs(numer),abs(denom)
        elif (denom < 0):
            numer, denom = -numer, abs(denom)
        factor = Rational.recursiveGCD(numer,denom)
        if (factor != 1):
            numer = numer/factor
            denom = denom/factor
        return numer, denom
                