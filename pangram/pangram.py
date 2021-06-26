import string
def is_pangram(sentence):
    abcs = set(string.ascii_lowercase)
    letters = set()
    for char in sentence.lower():
        if (char in abcs):
            letters.add(char)
    return True if (abcs == letters) else False
        


