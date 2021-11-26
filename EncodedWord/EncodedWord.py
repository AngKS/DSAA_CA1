'''
Name: Ang Kah Shin
Class: DAAA/FT/2B/04
Admin: P2004176
'''

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
