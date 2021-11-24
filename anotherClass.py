

class EncodedWord:
    '''
    sentence: array
    morse: array
    '''
    def __init__(self, word, morse):
        self.word = word
        self.morse = morse
        self.morseLength = len(morse)
        self.char = morse.split(",")
    
    def maxChar(self):
        maxNum = 0
        for char in self.char:
            if len(char) > maxNum:
                maxNum = len(char)
        return maxNum

    def hPrint(self):
        print(f"{self.word} {self.morse}")
        
    def padding(self):
        padded = []
        maxLen = self.maxChar()
        for char in self.char:
            if len(char) < self.maxChar():
                padded.append(" " * (maxLen - len(char)) + char)
            else:
                padded.append(char)
        return padded
    
    def __str__(self):
        return f"{self.morse}"

# m1 = EncodedWord("hello", "....,.,.-..,.-..,---")
# print(m1.maxChar())
# # print(m1.padding())
# print(m1.word)
# print(m1.__str__('V'))
