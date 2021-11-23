from newClass import Text
from anotherClass import EncodedWord
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


    def encode(self, sentence):
        '''Takes in 1 argument(sentence) and return the encoded sentence in Morse'''

        ENCODED = []
        # validate to ensure that sentence only consist of only alphabets and space
        words = sentence.split(" ")
        print(words)
        for word in words:
            encoded = ""
            for i, letter in enumerate(word):
                if not letter.isalpha() and not letter.isspace() and not letter.isdigit():
                    return "Please only include alphabets and spaces in your sentence."
                if letter.upper() in self.lookup:
                    if i != len(word) - 1:
                        encoded += self.lookup[letter.upper()] + ","
                    else:
                        encoded += self.lookup[letter.upper()]
                else:
                    encoded += " "
            obj = EncodedWord(word, encoded)
            # morseCode.append(obj)
            print(obj.word, end=" ")
            
            ENCODED.append(obj)
        print(" ".join(Eword.__str__(mode='V') for Eword in ENCODED), end=" ")
        return ENCODED

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
        print("*** Decoded Message", "\n", decodedString)
        sortedUniqueWords = sorted(
            uniqueWords, key=lambda x: (stats[x].length, len(x), x))
        lengths = sorted(
            {stats[key].length for key in sortedUniqueWords}, reverse=True)

        for length in lengths:
            print(f"\n*** Morse Code with frequency => {length}")
            for key in sortedUniqueWords:
                if stats[key].length == length:
                    print(
                        f"{self.encode(key)}\n[{key}]: [{stats[key].length}] {stats[key]}")

        # Essential Message Printing

        # load Stopwords file
        try:
            with open("stopwords.txt", "r") as f:
                stopwords = [word.upper() for word in f.read().split("\n")]
                f.close()
        except FileNotFoundError:
            return "Stopwords file not found."

        # remove stopwords from uniqueWords
        noStopwords = [(word, stats[word].outputArr())
                       for word in sortedUniqueWords if word not in stopwords]
        # sort nostopwords

        noStopwords = sorted(noStopwords, key=lambda x: (x[1][0], len(x[1])))

        ESSENTIAL = ""
        for length in lengths:
            for word, arr in noStopwords:
                if len(arr) == length:
                    ESSENTIAL += f"{word} "
        return "\n***Essential Message:\n" + ESSENTIAL


morse1 = Morse()
print(morse1.encode("Help I need help real quick"))
# morse1.displayOutput("....,.,.-..,.--. .. -.,.,.,-.. ....,.,.-..,.--. .-.,.,.- --.-,..-,..,-.-.,-.-")
