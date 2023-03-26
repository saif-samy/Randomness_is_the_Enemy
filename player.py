# Function to get the player username and makes sure that he enters a name
def getUsername():
    while True:
        username = input("Enter username: ")
        if username:
            return username.strip()
        print("Enter a valid username")


# A function to make user choose a bag, check that the input is in correct format, and makes sure that the bag chosen is not empty
def chooseBag(bags):
    choice = 0
    try:
        choice = int(input("Select a bag: "))
    except (ValueError):
        print("Please enter number")
        return chooseBag(bags)
    if choice < 1 or choice > 3:
        print("Please select a correct number.\n")
        return chooseBag(bags)
    choice -= 1
    if bags[choice] == 0:
        print("The selected bag is empty, please choose another bag.\n")
        return chooseBag(bags)
    return choice


# A function to get number of objects, check that the input is in correct format and there is enough items in this bag
def getNumber(bags, choice):
    number = 0
    try:
        number = int(input("Select a number of objects: "))
    except (ValueError):
        print("Please enter a number.\n")
        return getNumber(bags, choice)
    if number < 1 or number > 5:
        print("You must remove 1 to 5 objects from the bag.\n")
        return getNumber(bags, choice)
    if number > bags[choice]:
        print("There are only ", bags[choice], " objects in the bag.\n")
        return getNumber(bags, choice)
    bags[choice] -= number
    print("You removed ", number, " from bag ", choice + 1)
    print(bags[0], " - ", bags[1], " - ", bags[2])
    return bags


def userPlay(bags):
    userChoice = chooseBag(bags)
    return getNumber(bags, userChoice)
