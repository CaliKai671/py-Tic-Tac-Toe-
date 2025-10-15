##############################################################################
# This is the main code where I make the actual rules and conditions of code #
##############################################################################



import matplotlib.pyplot as plt
import random
game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]
player = "x"
winner = None
gameRunning = True


#Score#
user_score = 0
bot_score = 0
tie_score = 0
games_played = 0


quit_game = False




def print_scores():
    print("\nSCOREBOARD:")
    print(f"Player   (x):{user_score}")
    print(f"Bot      (o):{bot_score}")
    print(f"Ties        :{tie_score}")
    print(f"Games played:{games_played}")




#allows game to have new empty board#
def reset_board():
    global game_board, player, winner, gameRunning
    game_board = ["-", "-", "-",
                  "-", "-", "-",
                  "-", "-", "-"]
    player = "x"
    winner = None
    gameRunning = True






#create a game board#                                                    
def printBoard(game_board):
    colored_board = []
    for cell in game_board:
        if cell == "x":
            colored_board.append("\033[31mx\033[0m")#makes x colred red
        elif cell == "o":
            colored_board.append("\033[36mo\033[0m")#makes o colored blue
        else:
            colored_board.append("-")#dosn't change color of empty spot


    print(colored_board[0] + "|" + colored_board[1] + "|" + colored_board[2])
    print("-----")
    print(colored_board[3] + "|" + colored_board[4] + "|" + colored_board[5])
    print("-----")
    print(colored_board[6] + "|" + colored_board[7] + "|" + colored_board[8])






#have player input#                                                          
def playerInput(game_board):
    global player
    while True:
        user = input("Enter a position 1-9 or press q to quit:").strip()
        if user.strip() == "q":
            return "q"
        if user == "":
            print("Please pick a position 1-9 or press q.")
            continue
        if not user.isdigit():
            print("Please pick a position 1-9 or press q.")
            continue
        pos = int(user)
        if pos < 1 and pos > 9:
            print("Must be 1-9.")
            continue
        if game_board[pos - 1] != "-":
            print("Can't play there. Choose another spot.")
            continue


        game_board[pos - 1] = player
        print(f"TURN ON LED for {player} at position{str(pos)}")
        other = "o" if player == "x" else "x"
        print(f"Turn OFF LED for {other} at position{str(pos)}")
        return None








#check for a tie or win#
def checkRows(game_board):
    global winner
    if game_board[0] == game_board[1] == game_board[2] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != "-":
        winner = game_board[3]
        return True
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != "-":
        winner = game_board[6]
        return True
    return False


def checkCol(game_board):
    global winner
    if game_board[0] == game_board[3] == game_board[6] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif game_board[1] == game_board[4] == game_board[7] and game_board[1] != "-":
        winner = game_board[1]
        return True
    elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != "-":
        winner = game_board[2]
        return True
    return False
   
def checkAcross(game_board):
    global winner
    if game_board[0] == game_board[4] == game_board[8] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif game_board[2] == game_board[4] == game_board[6] and game_board[2] != "-":
        winner = game_board[2]
        return True
    return False


def winning_cells(game_board, who):
    if game_board[0] == who and game_board[1] == who and game_board[2] == who:
        return [1,2,3]
    if game_board[3] == who and game_board[4] == who and game_board[5] == who:
        return [4,5,6]
    if game_board[6] == who and game_board[7] == who and game_board[8] == who:
        return [7,8,9]
    if game_board[0] == who and game_board[3] == who and game_board[6] == who:
        return [1,4,7]
    if game_board[1] == who and game_board[4] == who and game_board[7] == who:
        return [2,5,8]
    if game_board[2] == who and game_board[5] == who and game_board[8] == who:
        return [3,6,9]
    if game_board[0] == who and game_board[4] == who and game_board[8] == who:
        return [1,5,9]
    if game_board[2] == who and game_board[4] == who and game_board[6] == who:
        return [3,5,7]
    return[]
   
def checkTie(game_board):
    global gameRunning
    if "-" not in game_board:
        printBoard(game_board)
        print("\033[32mThe game is a TIE!!!\033[0m")
        gameRunning  = False
        return True
    return False


def checkWin():                                                
    global gameRunning
    if checkRows(game_board) or checkCol(game_board) or checkAcross(game_board):
        printBoard(game_board)
        print(f"\033[33mThe Winner is {winner}\033[0m")
        cells = winning_cells(game_board , winner)
        if cells:
            print("Brighten these LEDs for player" , winner , ":" , cells)
        gameRunning =False
        return True
    return False


       


#switch players#COMPLETED#
def switchPlayer():
    global player
    if player == "x":
        player ="o"
    else:
        player = "x"


#Bot
def bot(game_board):
    empty = []
    i = 0
    while i < 9:
        if game_board[i] == "-":
            empty.append(i)
        i += 1
    if len(empty) > 0:
        pos1 = random.choice(empty)
        game_board[pos1] = "o"
        print("Bot plays in position", pos1 + 1)
        print("Turn LED on for o at position"  + str(pos1 + 1))
        print("Turn LED off for x at position"  + str(pos1 + 1))




def showWinRate(player_score, bot_score, tie_score):


    labels = ["Players Wins", "Bot Wins", "Ties"]
    sizes = [user_score, bot_score, tie_score]
    colors = ["green", "red", "blue"]
    plt.pie(sizes, labels = labels, colors = colors, autopct = "%1.1f%%")
    plt.title("Tic-Tac-Toe Win Rate")
    plt.show()










#Main LOOP#  


printBoard(game_board)


while True:
    while gameRunning:
        if player == "x":
            res = playerInput(game_board)
            if res == "q":
                print("GAME QUIT")
                break
            if checkWin():
                break
            if checkTie(game_board):
                break
            switchPlayer()
        else:
            bot(game_board)
            if checkWin():
                break
            if checkTie(game_board):
                break
            switchPlayer()
        printBoard(game_board)


    if quit_game:
        print("User quit the game.")
        print_scores()
        break


    games_played += 1
    if winner == "x":
        user_score += 1
        print("\033[32mYou won this round!!!\033[0m")
    elif winner =="o":
        bot_score += 1
        print("\033[31mThe Bot won this Round!!!\033[0m")
    else:
        tie_score += 1
        print("\033[33mThis round was a tie.\033[0m")
   
    print_scores()


    while True:
        again = input("Would you like to play again? (y/n):")
        if again in ("y"):
            reset_board()
            printBoard(game_board)
            break
        if again in ("n"):
            print("Thanks for playing.")
            print("\nFinal Results:")
            print_scores()
            quit_game = True
            break
        print("Please answer 'y' or 'n'.")
    if quit_game:
        break


showWinRate(user_score, bot_score, tie_score)
print("Thanks for playing!!!")
