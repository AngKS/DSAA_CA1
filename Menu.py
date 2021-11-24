
class Menu:
    '''Menu class takes in 3 parameters:
    1. question: The question to be asked to the user
    2. order: Boolean value to determine whether the menu should be ordered or not
    3. callback: The function to be called when the user enters a valid input

    Functions Available:
    1. insert(items): Inserts items into the menu
    2. __str__(): Prints the menu
    '''

    def __init__(self, question, order, options= None):
        self.qn = question
        self.ord = order
        self.__items = []
        self.length = 0
        self.options = options

    def insert(self, items):
        for item in items:
            self.length += 1
            self.__items.append(item)

    def __checkInput(self, userInput):
        # Check user input to see if it exists in the list
        # If it does, return the index of the item
        if self.options == None:
            if userInput.isnumeric():
                userInput = int(userInput)
                if userInput >= 1 and userInput <= self.length:
                    return str(userInput)
            print("** <Invalid input> **")
            return self.show()
        else:
            if userInput.upper() in self.options:
                return userInput.upper()
            print("** <Invalid input> **")
        return self.show()

    def __str__(self):
        print("\n" + self.qn)
        if self.ord:
            for i in range(self.length):
                print(str(i+1) + ". " + self.__items[i])
        else:
            for item in self.__items:
                print("-", item)

        return ""

    def show(self):
        print("\n" + self.qn)
        if self.ord:
            for i in range(self.length):
                print(str(i+1) + ". " + self.__items[i])
        else:
            for item in self.__items:
                print("-", item)

        userInput = self.__checkInput(input("Enter choice: "))
        return userInput


def testFunction(userInput):
    print("You entered: ", userInput + 1)
    return ""
