
class Menu:
    def __init__(self, question, order, callback):
        self.qn = question
        self.ord = order
        self.__items = []
        self.length = 0
        self.callback = callback

    def insert(self, items):
        for item in items:
            self.length += 1
            self.__items.append(item)
        
    def __checkInput(self, userInput):
        # Check user input to see if it exists in the list
        # If it does, return the index of the item
        if userInput.isnumeric():
            userInput = int(userInput)
            if userInput >= 1 and userInput <= self.length:
                return userInput - 1
        print("Invalid input")
        return self.__str__()

    def __str__(self):
        print("\n" + self.qn)
        if self.ord:
            for i in range(self.length):
                print(str(i+1) + ". " + self.__items[i])
        else:
            for item in self.__items:
                print("-", item)

        userInput = self.__checkInput(input("Enter choice: "))
        return self.callback(userInput)

def testFunction(userInput):
    print("You entered: ", userInput + 1)
    return ""

newMenu = Menu("What do you want to do?", True, testFunction)

newMenu.insert([
    "Hang out",
    "Watch movies",
    "Watch the sunset"
])

print(newMenu)
    
    
