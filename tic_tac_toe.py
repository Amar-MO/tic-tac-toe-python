import os

board_list = [1,2,3,4,5,6,7,8,9]

def board_display():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(board_list[6],'|' ,board_list[7] ,'|' ,board_list[8])
    print('---------')
    print(board_list[3],'|' ,board_list[4] ,'|' ,board_list[5])
    print('---------')
    print(board_list[0],'|', board_list[1], '|' ,board_list[2])


def player_choice():
    print('Welcome to the tic-tac-toa game!')
    print("Player 1 starts.")
    choice = input("Player 1, Pick X or O")
    switch = False
    
    
    
    while not switch:
        if choice == 'o' or choice == 'O' or choice == 'x' or choice == 'X':
            switch = True
            
        else:
            choice = input("Player 1, Pick X or O")

    return choice


def index_choice():
    
    choice = input("Please pick a position from the board (1-9): ")
    switch = False
    
    
    
    while not switch:
        while not choice.isdigit():
            choice = input("Sorry, this is an invalid input, please pick a position from the board (1-9): ")
        while choice.isdigit():
            if int(choice) in range(1,10):
                switch = True
                break
            else:
                choice = input("Position is out of range, please pick a position from the board (1-9)")
        
    return int(choice)


def place_symbol(position, symbol):
    board_list[position] = symbol
    return board_display()


def win_check():
    if board_list[0] == board_list[1] == board_list[2]:
        return True
    if board_list[3] == board_list[4] == board_list[5]:
        return True
    if board_list[6] == board_list[7] == board_list[8]:
        return True
    if board_list[0] == board_list[3] == board_list[6]:
        return True
    if board_list[0] == board_list[4] == board_list[8]:
        return True
    if board_list[1] == board_list[4] == board_list[7]:
        return True
    if board_list[2] == board_list[5] == board_list[8]:
        return True
    if board_list[2] == board_list[4] == board_list[6]:
        return True
        
    return False


def full_board_check():
    # Loop through every spot on the board
    for spot in board_list:
        # If any spot is still an integer (like 1, 2, 3...), the board is NOT full
        if type(spot) == int:
            return False
            
    # If the loop finishes without finding any numbers, all spots are 'X' or 'O'
    return True


board_list = [1,2,3,4,5,6,7,8,9]
p1_symbol = player_choice().upper()
p2_symbol = 'O' if p1_symbol == 'X' else 'X'

current_player = 'Player1'
current_symbol = p1_symbol
game_on = True

board_display()

while game_on:
    print(f"{current_player}'s turn {current_symbol}: ")

    position = (index_choice() - 1)

    while board_list[position] in ['X','O']:
        print("That position is taken! pick another")
        position = (index_choice() - 1)

    place_symbol(position, current_symbol)

    if win_check():
        print(f"Congrats! {current_player} won the game!!")
        game_on = False
    elif full_board_check():
        print("The game is a tie!")
        game_on = False
    else:

        if current_player == 'Player1':
            current_player = 'Player2'
            current_symbol = p2_symbol
        else:
            current_player = 'Player1'
            current_symbol = p1_symbol