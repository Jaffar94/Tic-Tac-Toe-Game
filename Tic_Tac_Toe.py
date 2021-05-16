from time import sleep # For pausing in intervals to show the information

#it is true when game starts and false when game needs to stopped
game_still_going = True

#Basic UI
print("\t\tTic Tac Toe Game")
print("\t\t\t  Made by: Jaffar\n")


#Taking information so that when they play the game again the program should not ask for information again
playerName1 = input("Enter the name of player 1: ").strip() # strip()this will remove the unwanted spaces
playerName2 = input("Enter the name of player 2: ").strip()
playerName1 = playerName1.capitalize()
playerName2 = playerName2.capitalize()
#So that both the player don't get same name
while True:
    if playerName2 == playerName1:
        playerName2 = input("The name is already taken by player 1. Enter other name: ").strip()
        playerName2 = playerName2.capitalize()
    if playerName2 != playerName1:
        break


XorY1 = input(f"{playerName1} You Choose X or O: ").strip()
XorY1 = XorY1.upper()

#It will ask user to enter x or o only
while XorY1 != "X" and XorY1 != "O":
    XorY1 = input(f"{playerName1} you entered wrong input please choose X or O: ").upper()

# defining the variable
XorY2 = None


# Giving the players x or o
if XorY1 == 'X':
    XorY2 = 'O'
elif XorY1 == 'O':
    XorY2 = 'X'



def main():
    

    # Board. Board is inside the function because when user will try agian to play this will automaticly reset
    board = ['1', '2', '3',
            '4', '5', '6', 
            '7', '8', '9']



    def checkDraw():
        draw = False

        # This is to check if it is draw or not
        if (board[0] == '1' or board[1] == '2' or board[2] == '3' or board[3] == '4' or board[4] == '5' or\
            board[5] == '6' or board[6] == '7' or board[7] == '8' or board[8] == '9'):
            draw = False
        else:
            draw = True


        if (draw == True):
            printBoard()
            print("\nDraw!!")
            global game_still_going
            sleep(1)
            game_still_going = False # Defining false to stop the main game and close




    # Function to check win . WIN LOGIC
    def checkWin(x_y, name):
        # '\' is used to wrap python program
        if (board[0] == x_y and board[3]  == x_y and board[6] == x_y) or\
            (board[1] == x_y and board[4] == x_y and board[7] == x_y) or\
            (board[2] == x_y and board[5] == x_y and board[8] == x_y) or\
            (board[0] == x_y and board[1] == x_y and board[2] == x_y) or\
            (board[3] == x_y and board[4] == x_y and board[5] == x_y) or\
            (board[6] == x_y and board[7] == x_y and board[8] == x_y) or\
            (board[0] == x_y and board[4] == x_y and board[8] == x_y) or\
            (board[2] == x_y and board[4] == x_y and board[6] == x_y): 
            
            printBoard()
            print(f"\n{x_y} Wins!!! Congratulations {name}\n")
                        
            sleep(1)
            global game_still_going
            game_still_going = False # Defining false to stop the main game and close
        


    # This is to correct input given from user. It include overwriting x or o and valueError etc. This will slove all the bugs problems error
    def correctInput(name, nameOp, xory):
       
        while True: 

            try:
                number = int(input(f"\n{name} Enter the number from the board in which you want to assign {xory}: "))
            except ValueError:
                print(f"\nERROR {name} Please Enter Numeric value. Try Again")
                sleep(3)
                printBoard()
                print(f"{name} = {XorY1} and {nameOp} = {XorY2}")
            else:
                # If the number is not present in the board this will handle it
                if(number >= 1 and number <= 9):
                    break #It will break if there is no problem
                else:
                    print(f"\nERROR {name} The number {number} is not present in the Board")
                    sleep(2)
                    printBoard()
                    continue
            finally: # finally will run if there is continue statement before than too it will run

                #in python index starts from 0 that is why minusing it with one 
                try: # I am trying exception here because is the numbe ris string then is should continue to the next iteration which will ask him to enter corrct
                    number -= 1
                except Exception:
                    continue
                
                if(number < 0 or number > 8):#This is wrong so I am say it to continue
                    continue
                else:
                    if (board[number] == "X"):
                        print(f"\nERROR {name} There is already X in {number + 1}. Try again")
                        sleep(1.5)
                        printBoard()
                        continue
                    elif(board[number] == "O"):
                        print(f"\nERROR {name} There is already O in {number + 1}. Try again")
                        sleep(1.5)
                        printBoard()
                        continue
          
        return number



    # Function to update board
    def updateBoard(input, xory):
        
        #converting it to integer but it is optional it is already interger but for safer side
        int(input)

        #Assigning the value in board
        board[input] = xory
            


    # funtion to print board
    def printBoard():
        print("")
        print("--------------------\n")
        print(f" {board[0]}   |   {board[1]}   |   {board[2]}")
        print("-----|-------|------")
        print(f" {board[3]}   |   {board[4]}   |   {board[5]}")
        print("-----|-------|------")
        print(f" {board[6]}   |   {board[7]}   |   {board[8]}\n")
        print("--------------------")



    #main function
    def mainGame():

        #defining the the user choice
        print(f"\n{playerName1} = {XorY1} and {playerName2} = {XorY2}")

        #this will run till the game_still_going is true
        while (game_still_going):

            printBoard() # printing board
            print(f"{playerName1} = {XorY1} and {playerName2} = {XorY2}")
            
            # Correct user input
            whereNumber = correctInput(playerName1, playerName2, XorY1)

            updateBoard(whereNumber, XorY1)

            checkWin(XorY1,playerName1)
            
            if not game_still_going : #Checking if check win changes the value of game_still_going to false
                continue # I am continuing because if the value of game still going is false then it will automaticly stop the iteration by ignoring code after this line            
            checkDraw()
            
            printBoard()
            print(f"{playerName1} = {XorY1} and {playerName2} = {XorY2}")
            # Correct user input
            whereNumber2 = correctInput(playerName2, playerName1, XorY2)

            updateBoard(whereNumber2, XorY2)

            checkWin(XorY2,playerName2)
            if game_still_going :
                checkDraw()


    # Runnin Main Function
    mainGame()


#Running main function
main()


while True: # So when you run main() one more time in if statement then this will work

    want = input("Click 'Y' and click enter to play again! or click enter or any key to exit this program: ").strip()
    want = want.upper()

    if (want == 'Y'):
        game_still_going = True # This is beingdone so that when you want to play again it should be true
        main()
    else:
        break # To break while loop when not want to play
