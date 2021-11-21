
'''
Name: Ang Kah Shin
Class: DAAA/FT/2B/04
Admin: P2004176
'''
# Writing program

from Morse import Morse
from Menu import Menu


def mainBanner():
    banner = '''
*******************************************
* ST1507 DSAA: MorseCode Message Analyzer *
*-----------------------------------------*
*                                         *
* - Done by: Ang Kah Shin (P2004176)      *
* - Class: DAAA/FT/2B/04                  *
******************************************* 
    '''
    return banner


def main():
    '''The main Program loop'''
    # program variables:
    pMode = 'h'
    morse = Morse()

    print(mainBanner())
    # Main menu selection
    mainMenu = Menu("Please select your choice (1, 2, 3, 4)", True )
    # add options into mainMenu
    mainMenu.insert([
        "Change Printing Mode",
        "Convert Morse Code to Text",
        "Analyze Morse Code Message",
        "Exit"
    ])
    # print mainMenu
    userInput = mainMenu.show()
    
    if userInput == '1':
        print(f"Current printing mode is: {pMode}")
    elif userInput == '2':
        inputMorse = input("Enter morse code you wish to decode: ")
        result = morse.decode(inputMorse)
        print("Decoded message:", result)
    elif userInput == '3':
        inputFile = input("Enter the input file name: ")
        outputFile = input("Enter the output file name: ")
        print(morse.analyze(inputFile, outputFile))
        print("\n>>>Analysis has started:")
        


if __name__ == "__main__":
    main()
