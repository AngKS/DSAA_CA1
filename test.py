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

sentence = "SOS WE NEED HELP"
morseCode = ""
condition = True
words = sentence.split(" ")
for word in words:
    for i, letter in enumerate(word):
        if not letter.isalpha() and not letter.isspace() and not letter.isdigit():
            print("Please only include alphabets and spaces in your sentence.")
        if letter.upper() in table:
            if i != len(word) - 1:
                morseCode += table[letter.upper()] + ","
            else:
                morseCode += table[letter.upper()]
        else:
            morseCode += " "

    morseCode += " "
print(morseCode)
# morseCode = morseCode.split(" ")
# morseCode = [morse.split(",") for morse in morseCode]

# def maxNum(l):
#     if len(l) == 1:
#         return l[0]
#     else:
#         if l[1] > l[0]:
#             return maxNum(l[1:])
#         else:
#             return maxNum( [l[0]] + l[2:] )

# maxArr = []            
# for arr in morseCode:
#     maxArr.append(len(maxNum(arr)))

# print(maxArr)
# print(morseCode)

