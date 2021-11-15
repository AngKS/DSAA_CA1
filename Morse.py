
'''
Name: Ang Kah Shin
Class: DAAA/FT/2B/04
Admin: P2004176
'''


class Node:
    def __init__(self):
        self.nextNode = None


# Morse Code Class
class Morse:
    table = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..",
    }

    def __init__(self):
        self.lookup = self.__class__.table

    def encode(self, sentence):
        encoded = ""
        # validate to ensure that sentence only consist of only alphabets and space
        for letter in sentence:
            if not letter.isalpha() and not letter.isspace():
                return "Please only include alphabets and spaces in your sentence."

            encoded += self.lookup[letter.upper()] + ","

    def decode(self, sentence):
        decoded = ""
        # validate to ensure that sentence only consist of only alphabets and space
        for letter in sentence:
            if not letter.isalpha() and not letter.isspace():
                return "Please only include alphabets and spaces in your sentence."

        return decoded


morse1 = Morse()
print(morse1.encode("Hello! World123"))
