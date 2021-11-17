
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
        
    def __str__(self):
        print("\n" + self.qn)
        if self.ord:
            for i in range(self.length):
                print(str(i+1) + ". " + self.__items[i])
        else:
            for item in self.__items:
                print("-", item)

        userInput = input(">> ")
        return self.callback(userInput)

def testFunction(userInput):
    print("You entered: "+ userInput)
    return ""

newMenu = Menu("What do you want to do?", True, testFunction)

newMenu.insert([
    "Hang out",
    "Watch movies",
    "Watch the sunset"
])

print(newMenu)
    
    
