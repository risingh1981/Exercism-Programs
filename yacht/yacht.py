# Score categories.
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12


def score(diceRoll, category):
    Y = {1:digit, 2:digit, 3:digit, 4:digit, 5:digit, 6:digit, 7:full_house, 8:four_of_a_kind, 9:little_straight, 10:big_straight, 11:choice, 12:yacht}
    if (category <= 6):
        answer = Y[category](diceRoll, category)
    else:
        answer = Y[category](diceRoll)

    return answer
    

def digit(diceRoll, val):
    return diceRoll.count(val) * val

def full_house(diceRoll):
    setOfRoll = set(diceRoll)
    if ((len(setOfRoll) == 2) and (diceRoll.count(diceRoll[0]) == 2 or diceRoll.count(diceRoll[0]) == 3)):
        return sum(diceRoll)
    else:
        return 0

def four_of_a_kind(diceRoll):
    setOfRoll = set(diceRoll)
    if (len(setOfRoll) > 2):
        return 0
    for ele in setOfRoll:
        if (diceRoll.count(ele) >= 4):
            return 4 * ele
    return 0

    
def little_straight(diceRoll):
    if (sorted(diceRoll) == [1,2,3,4,5]):
        return 30
    return 0

def big_straight(diceRoll):
    if (sorted(diceRoll) == [2,3,4,5,6]):
        return 30
    return 0

def choice(diceRoll):
    return sum(diceRoll)

def yacht(diceRoll):
    if (diceRoll.count(diceRoll[0]) == 5):
        return 50
    else:
        return 0