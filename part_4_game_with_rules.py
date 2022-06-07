from random import shuffle
from itertools import combinations_with_replacement
# define turn function
def turn_func(func_input, func_pieces):
    # stop if there is no pieces
    if int(func_input) == 0 and len(stock_pieces) == 0:
        return None
    # give piece to player
    elif int(func_input) == 0 and len(stock_pieces) > 0:
        func_pieces.append(stock_pieces[-1])
        stock_pieces.remove(stock_pieces[-1])
        return None
    # place piece right after snake
    if int(func_input) > 0:
        # get piece from player or computer
        piece_to_end = func_pieces[int(func_input) - 1]
        # reverse piece
        if piece_to_end[1] == snake[-1][-1]:
            piece_to_end.reverse()
        # place piece
        snake.append(piece_to_end)
        # remove piece from player or computer
        func_pieces.remove(func_pieces[int(func_input) - 1])
    # place piece left after snake
    else:
        # get piece from player or computer
        piece_to_start = func_pieces[-int(func_input) - 1]
        # reverse piece
        if piece_to_start[0] == snake[0][0]:
            piece_to_start.reverse()
        # place piece
        snake.insert(0, piece_to_start)
        # remove piece from player or computer
        func_pieces.remove(func_pieces[-int(func_input) - 1])
# Check if this snake is winning
def win_snake(func_snake):
    if func_snake[0][0] == func_snake[-1][-1] and sum(x.count(func_snake[0][0]) for x in func_snake) == 8:
        return True
# define list of dominoes
dominoes = list(combinations_with_replacement(range(0, 7), 2))
# convert list of tuples to list of lists
dominoes = [list(x) for x in dominoes]
# shuffle dominoes
shuffle(dominoes)
# define coefficient equal to half of the number of dominoes
coefficient = len(dominoes) // 2
# get first half of the dominoes
stock_pieces = dominoes[:coefficient]
# get computer's and player's pieces
computer_pieces = dominoes[coefficient:int(coefficient * 1.5)]
player_pieces = dominoes[int(coefficient * 1.5):]
# find snake
snake = [max([[x, y] for x, y in computer_pieces + player_pieces if x == y])]
# remove snake from computer's or player's pieces
computer_pieces.remove(snake[0]) if snake[0] in computer_pieces else player_pieces.remove(snake[0])
# define massages for player
player_turn = "It's your turn to make a move. Enter your command."
computer_turn = "Computer is about to make a move. Press Enter to continue..."
player_won = 'The game is over. You won!'
computer_won = 'The game is over. The computer won!'
# define who is first
turn_num = 0 if len(player_pieces) > len(computer_pieces) else 1
# start game
while True:
    # show stock, player's and computer's pieces
    print('=' * 70)
    print('Stock size:', len(stock_pieces))
    print('Computer pieces:', len(computer_pieces), '\n')
    print(*snake, '\n', sep='') if len(snake) <= 6 else print(*snake[:3], '...', *snake[-3:], '\n', sep='')
    print("Your pieces:")
    for num, piece in enumerate(player_pieces):
        print(f"{num + 1}: {piece}")
    # condition for player's win if there is no pieces
    if len(player_pieces) == 0:
        print("\nStatus:", player_won)
        break
    # condition for computer's win if there is no pieces
    if len(computer_pieces) == 0:
        print("\nStatus:", computer_won)
        break
    # condition for player's win if snake is winning
    if win_snake(snake) and turn_num == 0:
        print("\nStatus:", player_won)
        break
    # condition for computer's win if snake is winning
    if win_snake(snake) and turn_num == 1:
        print("\nStatus:", computer_won)
        break
    # define snake ends
    connection_keys = [snake[0][0], snake[-1][-1]]
    # condition for draw
    if len(stock_pieces) == 0 and \
            any([verb[1] for verb in player_pieces + computer_pieces if verb[0] in connection_keys]):
        print("\nStatus: The game is over. It's a draw!")
        break
    # player's turn
    if turn_num % 2 == 0:
        # count turn number
        turn_num += 1
        # show message
        print("\nStatus:", player_turn)
        # get player's input
        user_input = input()
        # check if player's input is valid
        if user_input.lstrip("-").isdigit() and int(user_input) in range(-len(player_pieces), len(player_pieces) + 1):
            # provide piece to player
            if int(user_input) == 0:
                turn_func(user_input, player_pieces)
                continue
            # define current piece
            current_piece = player_pieces[int(user_input) - 1] if int(user_input) > 0 \
                else player_pieces[-int(user_input) - 1]
            # check if piece is valid
            if connection_keys[-1] in current_piece and int(user_input) > 0 or \
                    connection_keys[0] in current_piece and int(user_input) < 0:
                turn_func(user_input, player_pieces)
            else:
                print("Illegal move. Please try again.")
                turn_num -= 1
                continue
        else:
            print("Invalid input. Please try again.")
            turn_num -= 1
            continue
    # computer's turn
    else:
        # count turn number
        turn_num += 1
        # show message
        print("\nStatus:", computer_turn)
        # wait for player's input
        input()
        # make computer's move
        for piece in computer_pieces:
            # check how to connect snake
            if piece[0] == connection_keys[-1]:
                turn_func(str(computer_pieces.index(piece) + 1), computer_pieces)
                break
            elif piece[1] == connection_keys[0]:
                turn_func(str(-computer_pieces.index(piece) - 1), computer_pieces)
                break
        # provide piece to computer
        else:
            turn_func('0', computer_pieces)
            
            
# ======================================================================
# Stock size: 14
# Computer pieces: 7 
# 
# [6, 6]
# 
# Your pieces:
# 1: [2, 2]
# 2: [2, 3]
# 3: [0, 0]
# 4: [1, 6]
# 5: [4, 4]
# 6: [1, 3]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 14
# Computer pieces: 6 
# 
# [2, 6][6, 6]
# 
# Your pieces:
# 1: [2, 2]
# 2: [2, 3]
# 3: [0, 0]
# 4: [1, 6]
# 5: [4, 4]
# 6: [1, 3]
# 
# Status: It's your turn to make a move. Enter your command.
# -1
# ======================================================================
# Stock size: 14
# Computer pieces: 6 
# 
# [2, 2][2, 6][6, 6]
# 
# Your pieces:
# 1: [2, 3]
# 2: [0, 0]
# 3: [1, 6]
# 4: [4, 4]
# 5: [1, 3]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 14
# Computer pieces: 5 
# 
# [1, 2][2, 2][2, 6][6, 6]
# 
# Your pieces:
# 1: [2, 3]
# 2: [0, 0]
# 3: [1, 6]
# 4: [4, 4]
# 5: [1, 3]
# 
# Status: It's your turn to make a move. Enter your command.
# 3
# ======================================================================
# Stock size: 14
# Computer pieces: 5 
# 
# [1, 2][2, 2][2, 6][6, 6][6, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [0, 0]
# 3: [4, 4]
# 4: [1, 3]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 14
# Computer pieces: 4 
# 
# [1, 2][2, 2][2, 6][6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [0, 0]
# 3: [4, 4]
# 4: [1, 3]
# 
# Status: It's your turn to make a move. Enter your command.
# -4
# ======================================================================
# Stock size: 14
# Computer pieces: 4 
# 
# [3, 1][1, 2][2, 2]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [0, 0]
# 3: [4, 4]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 14
# Computer pieces: 3 
# 
# [0, 3][3, 1][1, 2]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [0, 0]
# 3: [4, 4]
# 
# Status: It's your turn to make a move. Enter your command.
# 0
# ======================================================================
# Stock size: 13
# Computer pieces: 3 
# 
# [0, 3][3, 1][1, 2]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [0, 0]
# 3: [4, 4]
# 4: [4, 5]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 12
# Computer pieces: 4 
# 
# [0, 3][3, 1][1, 2]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [0, 0]
# 3: [4, 4]
# 4: [4, 5]
# 
# Status: It's your turn to make a move. Enter your command.
# -2
# ======================================================================
# Stock size: 12
# Computer pieces: 4 
# 
# [0, 0][0, 3][3, 1]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [4, 4]
# 3: [4, 5]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 11
# Computer pieces: 5 
# 
# [0, 0][0, 3][3, 1]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [4, 4]
# 3: [4, 5]
# 
# Status: It's your turn to make a move. Enter your command.
# 0
# ======================================================================
# Stock size: 10
# Computer pieces: 5 
# 
# [0, 0][0, 3][3, 1]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [4, 4]
# 3: [4, 5]
# 4: [0, 2]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 9
# Computer pieces: 6 
# 
# [0, 0][0, 3][3, 1]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [4, 4]
# 3: [4, 5]
# 4: [0, 2]
# 
# Status: It's your turn to make a move. Enter your command.
# -4
# ======================================================================
# Stock size: 9
# Computer pieces: 6 
# 
# [2, 0][0, 0][0, 3]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [4, 4]
# 3: [4, 5]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 8
# Computer pieces: 7 
# 
# [2, 0][0, 0][0, 3]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [2, 3]
# 2: [4, 4]
# 3: [4, 5]
# 
# Status: It's your turn to make a move. Enter your command.
# -1
# ======================================================================
# Stock size: 8
# Computer pieces: 7 
# 
# [3, 2][2, 0][0, 0]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [4, 4]
# 2: [4, 5]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 8
# Computer pieces: 6 
# 
# [3, 3][3, 2][2, 0]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [4, 4]
# 2: [4, 5]
# 
# Status: It's your turn to make a move. Enter your command.
# 0
# ======================================================================
# Stock size: 7
# Computer pieces: 6 
# 
# [3, 3][3, 2][2, 0]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [4, 4]
# 2: [4, 5]
# 3: [0, 1]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 6
# Computer pieces: 7 
# 
# [3, 3][3, 2][2, 0]...[6, 6][6, 1][1, 1]
# 
# Your pieces:
# 1: [4, 4]
# 2: [4, 5]
# 3: [0, 1]
# 
# Status: It's your turn to make a move. Enter your command.
# 3
# ======================================================================
# Stock size: 6
# Computer pieces: 7 
# 
# [3, 3][3, 2][2, 0]...[6, 1][1, 1][1, 0]
# 
# Your pieces:
# 1: [4, 4]
# 2: [4, 5]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 6
# Computer pieces: 6 
# 
# [3, 3][3, 2][2, 0]...[1, 1][1, 0][0, 4]
# 
# Your pieces:
# 1: [4, 4]
# 2: [4, 5]
# 
# Status: It's your turn to make a move. Enter your command.
# 1
# ======================================================================
# Stock size: 6
# Computer pieces: 6 
# 
# [3, 3][3, 2][2, 0]...[1, 0][0, 4][4, 4]
# 
# Your pieces:
# 1: [4, 5]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 6
# Computer pieces: 5 
# 
# [3, 3][3, 2][2, 0]...[0, 4][4, 4][4, 6]
# 
# Your pieces:
# 1: [4, 5]
# 
# Status: It's your turn to make a move. Enter your command.
# 
# Invalid input. Please try again.
# ======================================================================
# Stock size: 6
# Computer pieces: 5 
# 
# [3, 3][3, 2][2, 0]...[0, 4][4, 4][4, 6]
# 
# Your pieces:
# 1: [4, 5]
# 
# Status: It's your turn to make a move. Enter your command.
# 0
# ======================================================================
# Stock size: 5
# Computer pieces: 5 
# 
# [3, 3][3, 2][2, 0]...[0, 4][4, 4][4, 6]
# 
# Your pieces:
# 1: [4, 5]
# 2: [2, 4]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 4
# Computer pieces: 6 
# 
# [3, 3][3, 2][2, 0]...[0, 4][4, 4][4, 6]
# 
# Your pieces:
# 1: [4, 5]
# 2: [2, 4]
# 
# Status: It's your turn to make a move. Enter your command.
# 0
# ======================================================================
# Stock size: 3
# Computer pieces: 6 
# 
# [3, 3][3, 2][2, 0]...[0, 4][4, 4][4, 6]
# 
# Your pieces:
# 1: [4, 5]
# 2: [2, 4]
# 3: [2, 5]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 2
# Computer pieces: 7 
# 
# [3, 3][3, 2][2, 0]...[0, 4][4, 4][4, 6]
# 
# Your pieces:
# 1: [4, 5]
# 2: [2, 4]
# 3: [2, 5]
# 
# Status: It's your turn to make a move. Enter your command.
# 0
# ======================================================================
# Stock size: 1
# Computer pieces: 7 
# 
# [3, 3][3, 2][2, 0]...[0, 4][4, 4][4, 6]
# 
# Your pieces:
# 1: [4, 5]
# 2: [2, 4]
# 3: [2, 5]
# 4: [3, 6]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 0
# Computer pieces: 8 
# 
# [3, 3][3, 2][2, 0]...[0, 4][4, 4][4, 6]
# 
# Your pieces:
# 1: [4, 5]
# 2: [2, 4]
# 3: [2, 5]
# 4: [3, 6]
# 
# Status: The game is over. It's a draw!
