import art



print(art.title)
print("Welcome to Tic Tac Toe \n")

# it is a list with three lists inside 
game_board=[[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

# printing the game_board
for x in game_board:
    print(x)


print("This is two player game (plus&minus) ")

def insert(choice, player_num):
    # checking for the position  in first row
    if choice == 1 or choice == 2 or choice== 3:
        # checking for the position is empty
        if game_board[0][(choice-1)] == 0:
            # inserting the player number into main list
            game_board[0][(choice-1)]=player_num
            # returning the main list
            return game_board
        else:
            return 0
    elif choice == 4 or choice == 5 or choice== 6:
        if  game_board[1][(choice-4)] == 0:
            game_board[1][(choice-4)]=player_num
            return game_board
        else:
            return 0
    elif choice == 7 or choice == 8 or choice== 9:
         if  game_board[2][(choice-7)] == 0:
            game_board[2][(choice-7)]=player_num
            return game_board
         else:
            return 0
    else:
        return 0


def ask_choice(num):
    """
    takes the player numvber and ask for inout position 
    """
    if num ==1:    
        return (input(f"Pulse choose a position "))
    else:
        return (input(f"Minus choose a position "))

player = 1

def game_over(matrix):
    score = 0
    for x in range(3):
        if matrix[x][0] != 0 and matrix[x][1] != 0 and matrix[x][2] != 0:
            score +=1
    # print(score)
    if score == 3:
        return False
    else:
        return True



def winner_check(matrix):
    
    for x in range(len(matrix)):
        # checking horizontal row
        if matrix[x][0] == 1 and matrix[x][1] == 1 and matrix[x][2] == 1:
            return 1
        # checking horizontal row
        elif matrix[x][0] == -1 and matrix[x][1] == -1 and matrix[x][2] == -1:
            return -1
        # checking vertical row
        elif matrix[0][x] == 1 and matrix[1][x] == 1 and matrix[2][x] == 1:
            return 1
        # checking vertical row
        elif matrix[0][x] == -1 and matrix[1][x] == -1 and matrix[2][x] == -1:
            return -1
        # checking diaganal row
        elif game_board[0][0] ==1 and game_board[1][1] == 1 and game_board[2][2] == 1:
            return 1   
        elif game_board[0][2] ==1 and game_board[1][1] == 1 and game_board[2][0] == 1:
            return 1
         # checking diaganal row
        elif game_board[0][0] ==-1 and game_board[1][1] == -1 and game_board[2][2] == -1:
            return -1      
        elif game_board[0][2] == -1 and game_board[1][1] == -1 and game_board[2][0] == -1:
            return -1

        else:
            return 0


def play_again():
    # if player wants to paly again it will restart the game
    # Below code rearrage the board
    for x in range(3):
        for y in range(3):
            game_board[x][y] = 0
    # calling recersive function
    main_game(player)


def main_game(player):
        is_on=True
        while is_on:
            # calling the asking question function
            play_choice=int(ask_choice(player))
             
            # player enter correct postion then function returns inserted board
            test=insert(play_choice, player)

            if test == 0:
                print("Invalid Position")
                main_game(player)
            else:  
                for x in test:
                    print(x)
            # it value changes for every  Iteration to give other player a chance 
            player *=-1

            if winner_check(game_board) == 0:
            # if no one won yet it skips
                pass
            elif  winner_check(game_board) == 1:
                print("Pulse is winner")
                is_on = False
            elif winner_check(game_board) == -1:
                print("Minus is winner")
                is_on = False

            if game_over(game_board) == False:
                print("Draw")
                is_on=False

        again=input("Want to playagain:(Y/N)")
        if again =="Y":
            play_again()


main_game(player)    





