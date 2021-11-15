
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
    """
        Name: Morse
        Description: 

    """
    table = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----.", "0": "-----"
    }

    def __init__(self):
        self.lookup = self.__class__.table

    def encode(self, sentence):
        '''Takes in 1 argument(sentence) and return the encoded sentence in Morse'''
        morseCode = ""
        # validate to ensure that sentence only consist of only alphabets and space
        words = sentence.split(" ")
        for word in words:
            for i, letter in enumerate(word):
                if not letter.isalpha() and not letter.isspace() and not letter.isdigit():
                    return "Please only include alphabets and spaces in your sentence."
                if letter.upper() in self.lookup:
                    if i != len(word) - 1:
                        morseCode += self.lookup[letter.upper()] + ","
                    else:
                        morseCode += self.lookup[letter.upper()]
                else:
                    morseCode += " "
            morseCode += " "
        return morseCode

    def decode(self, morse):
        decoded = ""
        # validate to ensure that sentence only consist of only alphabets and space
        words = morse.split(" ")
        for word in words:
            letters = word.split(",")
            for letter in letters:
                for alpha, morse in self.lookup.items():
                    if morse == letter:
                        decoded += alpha
            decoded += " "
            # decoded += " "

        return decoded


morse1 = Morse()
encoded = morse1.encode("SOS Our sHiP NEEds HeLP")
print(encoded)

print(morse1.decode(encoded))
