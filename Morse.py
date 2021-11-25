from Text import Text
from EncodedWord import EncodedWord
from itertools import zip_longest
import numpy as np
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
        self.__lookup = self.__class__.table

    def displayOutput(self, output, method='H'): 
        output = output.split(" ")
        encoded = [word.split(',') for word in output]
        countEncoded = [(x.count('.') + x.count('-')) for i, x in enumerate(encoded)]
        print(encoded)
        def maxNum(l):
            if len(l) == 1:
                return l[0]
            else:
                if l[1] > l[0]:
                    return maxNum(l[1:])
                else:
                    return maxNum( [l[0]] + l[2:] )

        print("Third:", maxNum(countEncoded))


    def encode(self, sentence, mode='H'):
        '''Takes in 1 argument(sentence) and return the encoded sentence in Morse'''

        morseCode = []
        # validate to ensure that sentence only consist of only alphabets and space
        words = sentence.split(" ")
        for word in words:
            encoded = ""
            for i, letter in enumerate(word):
                if not letter.isalpha() and not letter.isspace() and not letter.isdigit():
                    return "Please only include alphabets and spaces in your sentence."
                if letter.upper() in self.__lookup:
                    if i != len(word) - 1:
                        encoded += self.__lookup[letter.upper()] + ","
                    else:
                        encoded += self.__lookup[letter.upper()]
            morse = EncodedWord(word, encoded)
            morseCode.append(morse)

        
        if mode == 'V':
            print(sentence)
            arr = []
            for obj in morseCode:
                arr.extend(obj.char)
                arr.append(" ")

            maxLength = len(max(arr, key=len))
            arr = ','.join([ (" " * (maxLength - len(x))) + x for x in arr])

            for char in zip_longest(*arr.split(','), fillvalue=''):
                print(''.join(char))        
            return ''
        
        return ' '.join(obj.morse for obj in morseCode)

    def decode(self, morse):
        decoded = ""
        # validate to ensure that sentence only consist of only alphabets and space

        letters = morse.split(",")
        for letter in letters:
            for alpha, morse in self.__lookup.items():
                if morse == letter:
                    decoded += alpha

        return decoded

    def analyze(self, input, output='report.txt'):
        '''Takes in 2 arguements: Input file and Output. Conducts a morse analysis on the input file and return the results into the output file'''

        report = ""
        try:
            with open(input, "r") as f:
                data = f.readlines()
                f.close()
        except FileNotFoundError:
            return "<Input file not found.>\n"

        try:
            with open("stopwords.txt", "r") as f:
                stopwords = [word.upper() for word in f.read().split("\n")]
                f.close()
        except FileNotFoundError:
            return "Stopwords file not found."

        print("\n>>>Analysis has started:")
        stats = {}
        decodedString = ""

        for row, sentence in enumerate(data):
            for column, word in enumerate(sentence.split(" ")):
                decoded = Text(self.decode(word), word, row, column)
                if decoded.text in stats:
                    stats[decoded.text].insert(decoded)
                else:
                    newList = SortedList()
                    newList.insert(decoded)
                    stats[decoded.text] = newList
                decodedString += decoded.text + " "
            decodedString += "\n"
        uniqueWords = [key for key in stats.keys()]

        # Add decoded string into report
        report += ("*** Decoded Message\n" + decodedString)

        sortedUniqueWords = sorted(uniqueWords, key=lambda x: (stats[x].length, len(x), x))
        lengths = sorted({stats[key].length for key in sortedUniqueWords}, reverse=True)

        for length in lengths:
            report += f"\n*** Morse Code with frequency => {length}\n"
            for key in sortedUniqueWords:
                if stats[key].length == length:

                    report += f"{self.encode(key, 'H')}\n[{key}]: ({stats[key].length}) {stats[key]}\n"

        # Essential Message Printing
        # load Stopwords file
        try:
            with open("stopwords.txt", "r") as f:
                stopwords = [word.upper() for word in f.read().split("\n")]
                f.close()
        except FileNotFoundError:
            return "Stopwords file not found."

        # remove stopwords from uniqueWords
        noStopwords = [(word, stats[word].outputArr()) for word in sortedUniqueWords if word not in stopwords]

        # sort nostopwords
        noStopwords = sorted(noStopwords, key=lambda x: (x[1][0], len(x[1])))

        ESSENTIAL = ""
        for length in lengths:
            for word, arr in noStopwords:
                if len(arr) == length:
                    ESSENTIAL += f"{word} "
        report += f"\n*** Essential Message:\n{ESSENTIAL}\n"
        print(report)

        # write report to output file
        try:
            with open(output, "w") as f:
                f.write(report)
                f.close()
        except FileNotFoundError:
            return "Output file not found."
