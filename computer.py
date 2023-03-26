import random


# Computer play function that uses random library to select bag and number of objects and making sure that the generated number is valid
def computerPlay(bags):
    bagSelection = random.randint(0, 2)
    if bags[bagSelection] == 0:
        return computerPlay(bags)
    elif bags[bagSelection] == 1:
        bags[bagSelection] -= 1
        print("The computer removed 1 from bag", bagSelection + 1)
        return bags
    else:
        while True:
            randomNumber = random.randint(1, 5)
            if randomNumber < bags[bagSelection]:
                bags[bagSelection] -= randomNumber
                print("The computer removed", randomNumber,
                      "from bag", bagSelection + 1)
                return bags
