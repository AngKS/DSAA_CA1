
'''
Name: Ang Kah Shin
Class: DAAA/FT/2B/04
Admin: P2004176
'''

# morse code dictionary
lookUpTable = {}

# Morse Code Class


class Morse:

    table = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..", "1" : ".----", "2" : "..---",
        "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....",
        "7" : "--...", "8" : "---..", "9" : "----.", "0" : "-----"
    }

    def __init__(self):
        self.lookup = self.__class__.table

    def encode(self, sentence):
        # validate to ensure that sentence only consist of only alphabets and space
        for letter in sentence:
            if not letter.isalpha() and not letter.isspace():
                return "Please only include alphabets and spaces in your sentence."

morse1 = Morse()
print(morse1.encode("Hello! World123"))
        


