
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
    pMode = 'H'
    while 1:
        morse = Morse()

        print(mainBanner())
        # Main menu selection
        mainMenu = Menu("Please select your choice (1, 2, 3, 4)", True )
        # add options into mainMenu
        mainMenu.insert([
            "Change Printing Mode",
            "Convert Text to Morse Code",
            "Analyze Morse Code Message",
            "Exit"
        ])
        # print mainMenu
        userInput = mainMenu.show()
        
        if userInput == '1':
            print(f"Current printing mode is: {pMode}")
            changeMode = Menu("\nEnter 'h' for horizontal or 'v' for vertical, then press enter", True, ['H', 'V'] )
            userInput = changeMode.show()
            print(f"The print mode has been changed to {'Vertical' if userInput == 'V' else 'Horizontal'}")
            pMode = userInput 
        elif userInput == '2':
            inputMorse = input("Enter Message you wish to encode: ")
            morse.encode(inputMorse, mode=pMode)
            # print("Encoded message:", msg)
        elif userInput == '3':
            inputFile = input("Enter the input file name: ")
            outputFile = input("Enter the output file name: ")
            print(morse.analyze(inputFile, outputFile))

        elif userInput == '4':
            print("Exiting program...")
            exit()
        else:
            print("Invalid input. Please try again.")
            main()
        
        userInput = input("\nPress Enter to continue...")
            


if __name__ == "__main__":
    
    main()
