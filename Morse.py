from newClass import Text
from SortedList import SortedList
'''
Name: Ang Kah Shin
Class: DAAA/FT/2B/04
Admin: P2004176
'''


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

        letters = morse.split(",")
        for letter in letters:
            for alpha, morse in self.lookup.items():
                if morse == letter:
                    decoded += alpha

        return decoded

    def analyze(self, input, output):
        '''Takes in 2 arguements: Input file and Output. Conducts a morse analysis on the input file and return the results into the output file'''
        try:
            with open(input, "r") as f:
                data = f.readlines()
                f.close()
        except FileNotFoundError:
            return "Input file not found."

        print("\n>>>Analysis has started:")
        stats = {}
        for row,sentence in enumerate(data):
            for column, word in enumerate(sentence.split(" ")):
                decoded = Text(self.decode(word), row, column)
                print(decoded.text)
                if decoded.text in stats:
                    stats[decoded.text].insert(decoded)
                    # print("Exists:",stats[decoded.text])
                else:
                    newList = SortedList()
                    newList.insert(decoded)
                    stats[decoded.text] = newList
                    # print(newList)
        
        for key in stats.keys():
            print(f"{key}: [{stats[key].length}] {stats[key]}")
        # print(stats.keys())
        # print(stats)
          


        # print("\n**Decoded Morse Message" + "\n" + decoded)

        # Morse code statistics
        # get frequency of each word
        # words = decoded.split(" ")
        # wordFreq = {}
        # for word in words:
        #     if word in wordFreq:
        #         wordFreq[word] += 1
        #     else:
        #         wordFreq[word] = 1
        
        

        return decoded
