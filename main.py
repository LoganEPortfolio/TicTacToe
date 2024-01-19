

is_gameover = False

game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]


def display_board():
    print(f"{game_board[0]} | {game_board[1]} | {game_board[2]}")
    print("---------")
    print(f"{game_board[3]} | {game_board[4]} | {game_board[5]}")
    print("---------")
    print(f"{game_board[6]} | {game_board[7]} | {game_board[8]}")


def is_taken(location):
    if location != '-':
        return True
    else:
        return False
    

def check_winner():
    global is_gameover
    if (game_board[0] == game_board[1] == game_board[2] != '-'):
        is_gameover = True
        print(f"{game_board[0]} Wins!")
    elif (game_board[0] == game_board[4] == game_board[8] != '-'):
        is_gameover = True
        print(f"{game_board[0]} Wins!")
    elif (game_board[0] == game_board[3] == game_board[6] != '-'):
        is_gameover = True
        print(f"{game_board[0]} Wins!")
    elif (game_board[1] == game_board[4] == game_board[7] != '-'):
        is_gameover = True
        print(f"{game_board[1]} Wins!")
    elif (game_board[2] == game_board[5] == game_board[8] != '-'):
        is_gameover = True
        print(f"{game_board[2]} Wins!")
    elif (game_board[3] == game_board[4] == game_board[5] != '-'):
        is_gameover = True
        print(f"{game_board[3]} Wins!")
    elif (game_board[6] == game_board[7] == game_board[8] != '-'):
        is_gameover = True
        print(f"{game_board[6]} Wins!")
    elif (game_board[2] == game_board[4] == game_board[6] != '-'):
        is_gameover = True
        print(f"{game_board[2]} Wins!")
    
    
# def take_square(player, location):
#     if not is_taken(game_board[location-1]):
#         game_board[location-1] = player
#         display_board()
#         return False
#     else:
#         print("Thats already taken, select again.")
#         return True
        

def player_move(player_shape):
    player_input = int(input(f'\n\n{player_shape}: Select which spot you want to place your choice. Type 1-9: '))
    while is_taken(game_board[player_input-1]):
        print("Thats already taken, select again.")
        display_board()
        player_input = int(input(f'\n\n{player_shape}: Select which spot you want to place your choice. Type 1-9: '))
    return player_input


def take_square(player, location):
    game_board[location-1] = player
    display_board()

display_board()

# player1_shape = input("Do you want to be X or O? Type 'X' or 'O': ")

# if player1_shape == 'X':
#     player2_shape = 'O'
# else:
#     player2_shape = 'X'



#num_players = int(input("How many players? Type 1 or 2: "))
player1_shape = input("Do you want to be X or O? Type 'X' or 'O': ")
if player1_shape == 'X':
    player2_shape = 'O'
else:
    player2_shape = 'X'




while not is_gameover:
    player1_input = player_move(player1_shape)
    take_square(player1_shape, player1_input)
    check_winner()
    if is_gameover == True:
        break
    player2_input = player_move(player2_shape)
    take_square(player2_shape, player2_input)
    check_winner()






# while not is_gameover:
#     player1_input = int(input('\n\nPlayer 1: Select which spot you want to place your choice. Type 1-9: '))

#     take_square(player1_shape, player1_input)

#     check_winner()

#     if is_gameover == True:
#         break
    
#     player2_input = int(input('\n\nPlayer 2: Select which spot you want to place your choice. Type 1-9: '))

#     take_square(player2_shape, player2_input)

#     check_winner()
    



