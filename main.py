import sys 

def greeting():
    print("This program allows you to keep track of how the price of a specific item may change by day.")
    print("""Here are your options: 
    - Add an Item (A)
    - Delete an Item from Your Watch List (D)
    - View all Items your Watch List (V)
    - Exit the Program (exit)""")

def decision():
    option = ""
    validOptions = ["A", "D", "V", "EXIT"]

    while (option not in validOptions):
        option = input("What would you like? ").upper()
    
    return str(option).upper()

def path(option):
    if option == "A":
        addItem()
    elif option == "D":
        print("We'll call another function to delete the item to the watch list")
    elif option == "V":
        print("We'll call another function to view our watch list")
    else:
        print("GOODBYE!")

def addItem():
    url = input("What is the url? ")
    

def main():
    greeting()
    option = decision()
    path(option)

if __name__ == "__main__":
    main() 