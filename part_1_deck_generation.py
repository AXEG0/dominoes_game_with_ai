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


# show stock, player's and computer's pieces
print("Stock pieces:", stock_pieces)
print("Computer pieces:", computer_pieces)
print("Player pieces:", player_pieces)
print("Domino snake:", [snake])
# show who is first
print("Status:", "player" if len(player_pieces) > len(computer_pieces) else "computer")

# Stock pieces: [[5, 5], [0, 2], [3, 4], [0, 3], [3, 5], [6, 6], [1, 2], [0, 4], [2, 6], [1, 4], [3, 3], [1, 5], [3, 6], [0, 5]]
# Computer pieces: [[1, 1], [4, 5], [1, 6], [2, 3], [2, 2], [4, 6]]
# Player pieces: [[0, 1], [2, 5], [1, 3], [2, 4], [0, 0], [0, 6], [5, 6]]
# Domino snake: [[4, 4]]
# Status: player
