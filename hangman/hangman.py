# Game status categories
# Change the values as you see fit
STATUS_WIN = "Win"
STATUS_LOSE = "Lose"
STATUS_ONGOING = "Ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = "_" * len(self.word)

    def guess(self, char):
        if (self.status == STATUS_LOSE) or (self.status == STATUS_WIN):
            raise ValueError("You have already lost the game" if (self.status == STATUS_LOSE) else "You have already won the game.")
        occurrences = Hangman.find_occurrences(self.word, char)
        if (len(occurrences) == 0) or (char in self.masked_word):
            self.update_remaining_guesses()
        else:
            char_arr = list(self.masked_word)
            for occurrence in occurrences:
                char_arr[occurrence] = self.word[occurrence]
            self.masked_word = "".join(char_arr)
        if (self.masked_word == self.word):
            self.status = STATUS_WIN
        
    def update_remaining_guesses(self):
        self.remaining_guesses -= 1
        if (self.remaining_guesses == -1):
            self.status = STATUS_LOSE


    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

    @staticmethod
    def find_occurrences(string, ch):
        return [i for i, letter in enumerate(string) if letter == ch]
