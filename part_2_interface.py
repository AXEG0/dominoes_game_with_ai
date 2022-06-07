from random import shuffle
from itertools import combinations_with_replacement
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
snake = max([[x, y] for x, y in computer_pieces + player_pieces if x == y])
# remove snake from computer's or player's pieces
computer_pieces.remove(snake) if snake in computer_pieces else player_pieces.remove(snake)
# define massages for player
player_turn = "It's your turn to make a move. Enter your command."
computer_turn = "Computer is about to make a move. Press Enter to continue..."
# show stock, player's and computer's pieces
print('=' * 70)
print('Stock size:', len(stock_pieces))
print('Computer pieces:', len(computer_pieces), '\n')
print(snake, '\n')
# show plauer's pieces
print("Your pieces:")
for num, piece in enumerate(player_pieces):
    print(f"{num + 1}: {piece}")
# show who is first
print("\nStatus:", player_turn if len(player_pieces) > len(computer_pieces) else computer_turn)

# ======================================================================
# Stock size: 14
# Computer pieces: 6
#
# [3, 3]
#
# Your pieces:
# 1: [1, 1]
# 2: [0, 6]
# 3: [0, 4]
# 4: [2, 6]
# 5: [4, 6]
# 6: [3, 5]
# 7: [0, 2]
#
# Status: It's your turn to make a move. Enter your command.
