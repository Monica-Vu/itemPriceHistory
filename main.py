import sys 
import backend
import database

def greeting():
    print("This program allows you to keep track of how the price of a specific item may change by day.")
    print("""Here are your options: 
    - Add an Item (A)
    - Delete an Item from Your Watch List (D)
    - View all Items your Watch List (V)
    - Exit the Program (exit)""")

def decision():
    option = ""
    validOptions = ["A", "D", "V", "R", "P", "EXIT"]

    while (option not in validOptions):
        option = input("What would you like? ").upper()
    
    return str(option).upper()

def path(option):
    if option == "A":
        url = input("Enter the URL: ")
        database.insertItem(url)
    elif option == "D":
        database.printItems()
        url = input("Enter the URL: ")
        database.deleteItem(url)
    elif option == "V":
        database.printItems()
    elif option == "R":
        backend.getDailyPrice()
    elif option == "P":
        database.printPrices()
    else:
        sys.exit()

def addItem():
    url = str(input("What is the url? "))


def main():
    backend.triggerDaily()
    greeting()
    while True: 
        option = decision()
        path(option)

if __name__ == "__main__":
    main() 