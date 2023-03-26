import player as P
import computer as C
import cv2


# Check winning condition
def checkWinning(bags):
    if bags[0] == 0 and bags[1] == 0 and bags[2] == 0:
        return True
    return False


# Ask the user if he wants to restart of exit the game, check that the input is in correct format
def restartGame():
    restart = 0
    try:
        restart = int(input("Enter 1 to restart or 2 to exit the game: "))
    except (ValueError):
        print("Please enter a number.\n")
    if restart != 1 and restart != 2:
        print("Please enter a correct number.\n")
        return restartGame()
    if restart == 1:
        return True
    return False


# Function that displays an image, wait til user press any key before destroying the image window
def showImage(image, caption):
    cv2.imshow(caption, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # Array that represents the three bags, each contains 10 items
    bags = [10, 10, 10]
    # Read image using cv2 library
    winnerImage = cv2.imread("assets/winner.jpg")
    loserImage = cv2.imread("assets/loser.jpg")
    # select font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # select position for text
    org = (50, 150)
    # font scale
    fontScale = 1
    # font color black
    color = (0, 0, 0)
    # font thickness
    thickness = 2
    # get player username
    username = P.getUsername()
    # winner and loser statements
    winnerStatement = "Congratulations " + username + ", you won!!"
    loserStatement = "Unlucky, the computer won!!"
    # write statements on the image
    winnerImage = cv2.putText(winnerImage, winnerStatement, org, font,
                              fontScale, color, thickness, cv2.LINE_AA)
    loserImage = cv2.putText(loserImage, loserStatement, org, font,
                             fontScale, color, thickness, cv2.LINE_AA)
    print("---------------------------------")
    win = 0
    while True:
        print(bags[0], " - ", bags[1], " - ", bags[2])
        # player playing
        bags = P.userPlay(bags)
        if checkWinning(bags):
            print(winnerStatement)
            win = 1
            showImage(winnerImage, "Winner")
        if win != 1:
            # computer playing
            bags = C.computerPlay(bags)
            if checkWinning(bags):
                print(loserStatement)
                win = 1
                showImage(loserImage, "Loser")
            print("-----------------------------")
        # if someone wins it asks the user whether to exit or restart the game
        if win == 1:
            if restartGame():
                # reset the game
                win = 0
                bags = [10, 10, 10]
            else:
                print("Goodbye!")
                exit()


main()
