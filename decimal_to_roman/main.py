from modules.conversions import ConvertNumbers as conv

def enterToContinue():
    '''
    This function will call the menu when the enter button is pressed.
    '''
    input("\n\nPress enter to continue...")
    menu()

def error():
    '''
    This function will print that the user entered an invalid option
    and will call the enter to continue method.
    '''
    print("\n[ERROR] Invalid option...\n")
    enterToContinue()

def convertDecimal():
    '''
    This function will ask for an integer and will call the
    convert module to transform it into a roman number.
    '''
    n = int(input("Enter the decimal number: "))
    print("\nThe number is : ", conv.decimalToRoman(n))
    enterToContinue()
    
def convertRoman():
    '''
    This function will ask for a roman number string and will call the
    convert module to transform it into a decimal number.
    '''
    r = str(input("Enter the roman number: "))
    print("\nThe number is : ", conv.romanToDecimal(r))
    enterToContinue()

def menu():
    '''
    This function will ask for input for user to perform the following functions:
    * Convert decimal to roman
    * Convert roman to decimal
    '''
    op = 0
    while op != 3:
        print()
        print("1) Convert decimal to roman")
        print("2) Convert roman to decimal")
        print("3) Exit")
        print()

        try:
            op = int(input("Enter the option : "))
        except ValueError as e:
            print("\n[ERROR] Invalid option...")
            enterToContinue()

        if type(op) not in [int, float]:
            raise ValueError("\n[ERROR] Invalid option...")

        if op == 1:
            convertDecimal()
        elif op == 2:
            convertRoman()
        elif op ==3:
            exit()
        else:
            error()

if __name__ == "__main__":
    menu()