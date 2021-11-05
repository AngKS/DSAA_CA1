
'''
Name: Ang Kah Shin
Class: DAAA/FT/2B/04
Admin: P2004176
'''

# morse code dictionary
lookUpTable = {}

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
        for letter in sentence:
            if not letter.isalpha() and not letter.isspace() and not letter.isdigit():
                return "Please only include alphabets and spaces in your sentence."
            # convert letter to uppercase
            letter = letter.upper()
            # check if letter is in the dictionary
            if letter in self.lookup:
                # if letter is in the dictionary, append the morse code to the morse code list
                morseCode += self.lookup[letter] + ","
            elif letter == " ":
                morseCode += " "
            else:
                # if letter is not in the dictionary, return error message
                return "Input Unknown!"
        return morseCode

morse1 = Morse()
print("Hello World123")
print(morse1.encode("Hello World123"))
