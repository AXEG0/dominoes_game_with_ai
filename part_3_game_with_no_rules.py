from random import shuffle, choice
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
    if len(func_input) == 1:
        snake.append(func_pieces[int(func_input) - 1])
        func_pieces.remove(func_pieces[int(func_input) - 1])
    # place piece left after snake
    else:
        snake.insert(0, func_pieces[-int(func_input) - 1])
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
        print("\nStatus: The game is over. You won!")
        break
    # condition for computer's win if there is no pieces
    if len(computer_pieces) == 0:
        print("\nStatus: The game is over. The computer won!")
        break
    # condition for player's win if snake is winning
    if win_snake(snake) and turn_num == 0:
        print("\nStatus: The game is over. You won!")
        break
    # condition for computer's win if snake is winning
    if win_snake(snake) and turn_num == 1:
        print("\nStatus: The game is over. The computer won!")
        break
    # define player's turn
    if turn_num % 2 == 0:
        # count turn number
        turn_num += 1
        # show message for player's turn
        print("\nStatus:", player_turn)
        # get player's input
        user_input = input()
        # check if player's input is valid
        if user_input.isdigit() and int(user_input) in range(-len(player_pieces), len(player_pieces) + 1):
            turn_func(user_input, player_pieces)
        else:
            print("Invalid input. Please try again.")
            turn_num -= 1
            continue
    # define computer's turn
    else:
        # count turn number
        turn_num += 1
        # show message for computer's turn
        print("\nStatus:", computer_turn)
        # wait for player's input
        input()
        # get computer's input
        computer_choice = str(choice(range(-len(computer_pieces), len(computer_pieces) + 1)))
        # make computer's move
        turn_func(computer_choice, computer_pieces)


# ======================================================================
# Stock size: 14
# Computer pieces: 7 
# 
# [4, 4]
# 
# Your pieces:
# 1: [4, 6]
# 2: [3, 4]
# 3: [4, 5]
# 4: [2, 5]
# 5: [1, 3]
# 6: [5, 6]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 14
# Computer pieces: 6 
# 
# [1, 1][4, 4]
# 
# Your pieces:
# 1: [4, 6]
# 2: [3, 4]
# 3: [4, 5]
# 4: [2, 5]
# 5: [1, 3]
# 6: [5, 6]
# 
# Status: It's your turn to make a move. Enter your command.
# 1
# ======================================================================
# Stock size: 14
# Computer pieces: 6 
# 
# [1, 1][4, 4][4, 6]
# 
# Your pieces:
# 1: [3, 4]
# 2: [4, 5]
# 3: [2, 5]
# 4: [1, 3]
# 5: [5, 6]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 14
# Computer pieces: 5 
# 
# [0, 6][1, 1][4, 4][4, 6]
# 
# Your pieces:
# 1: [3, 4]
# 2: [4, 5]
# 3: [2, 5]
# 4: [1, 3]
# 5: [5, 6]
# 
# Status: It's your turn to make a move. Enter your command.
# 3
# ======================================================================
# Stock size: 14
# Computer pieces: 5 
# 
# [0, 6][1, 1][4, 4][4, 6][2, 5]
# 
# Your pieces:
# 1: [3, 4]
# 2: [4, 5]
# 3: [1, 3]
# 4: [5, 6]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 14
# Computer pieces: 4 
# 
# [0, 6][1, 1][4, 4][4, 6][2, 5][1, 5]
# 
# Your pieces:
# 1: [3, 4]
# 2: [4, 5]
# 3: [1, 3]
# 4: [5, 6]
# 
# Status: It's your turn to make a move. Enter your command.
# 5
# Invalid input. Please try again.
# ======================================================================
# Stock size: 14
# Computer pieces: 4 
# 
# [0, 6][1, 1][4, 4][4, 6][2, 5][1, 5]
# 
# Your pieces:
# 1: [3, 4]
# 2: [4, 5]
# 3: [1, 3]
# 4: [5, 6]
# 
# Status: It's your turn to make a move. Enter your command.
# 4
# ======================================================================
# Stock size: 14
# Computer pieces: 4 
# 
# [0, 6][1, 1][4, 4]...[2, 5][1, 5][5, 6]
# 
# Your pieces:
# 1: [3, 4]
# 2: [4, 5]
# 3: [1, 3]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 14
# Computer pieces: 3 
# 
# [2, 6][0, 6][1, 1]...[2, 5][1, 5][5, 6]
# 
# Your pieces:
# 1: [3, 4]
# 2: [4, 5]
# 3: [1, 3]
# 
# Status: It's your turn to make a move. Enter your command.
# 2
# ======================================================================
# Stock size: 14
# Computer pieces: 3 
# 
# [2, 6][0, 6][1, 1]...[1, 5][5, 6][4, 5]
# 
# Your pieces:
# 1: [3, 4]
# 2: [1, 3]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 14
# Computer pieces: 2 
# 
# [2, 6][0, 6][1, 1]...[5, 6][4, 5][2, 3]
# 
# Your pieces:
# 1: [3, 4]
# 2: [1, 3]
# 
# Status: It's your turn to make a move. Enter your command.
# 1
# ======================================================================
# Stock size: 14
# Computer pieces: 2 
# 
# [2, 6][0, 6][1, 1]...[4, 5][2, 3][3, 4]
# 
# Your pieces:
# 1: [1, 3]
# 
# Status: Computer is about to make a move. Press Enter to continue...
# 
# ======================================================================
# Stock size: 14
# Computer pieces: 1 
# 
# [2, 6][0, 6][1, 1]...[2, 3][3, 4][0, 0]
# 
# Your pieces:
# 1: [1, 3]
# 
# Status: It's your turn to make a move. Enter your command.
# 1
# ======================================================================
# Stock size: 14
# Computer pieces: 1 
# 
# [2, 6][0, 6][1, 1]...[3, 4][0, 0][1, 3]
# 
# Your pieces:
# 
# Status: The game is over. You won!
