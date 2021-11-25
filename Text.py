from Node import Node

'''
Name: Ang Kah Shin
Class: DAAA/FT/2B/04
Admin: P2004176
'''


class Text(Node):
    def __init__(self, text, morse, x, y):
        self.text = text
        self.morse = morse
        self.morseLength = len(morse)
        self.x = x
        self.y = y
        super().__init__()

    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.x == otherNode.x and self.y == otherNode.y

    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'<' not supported between instances of 'Point' and 'NoneType'")
        if self.x < otherNode.x:
            return True
        elif self.x == otherNode.x:
            return self.y < otherNode.y
        else:
            return False

    def __str__(self):
        return f"{(self.x, self.y)}"
