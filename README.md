## What:
Python Dominoes game in 5 parts:
- Deck generation
- Interface
- The game with no rules
- The game with rules
- The game with AI

## Why:
This code was prepared for this article: https://medium.com/@axegggl/dominoes-game-with-simple-ai-in-python-df7f62feab4

## Example:

```
======================================================================
Stock size: 14
Computer pieces: 6
[1, 1]
Your pieces:
1: [3, 4]
2: [0, 1]
3: [5, 6]
4: [4, 6]
5: [1, 6]
6: [1, 5]
7: [1, 4]
Status: It's your turn to make a move. Enter your command.
> 2
======================================================================
Stock size: 14
Computer pieces: 6
[1, 1][1, 0]
Your pieces:
1: [3, 4]
2: [5, 6]
3: [4, 6]
4: [1, 6]
5: [1, 5]
6: [1, 4]
Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 14
Computer pieces: 5
[1, 1][1, 0][0, 0]
Your pieces:
1: [3, 4]
2: [5, 6]
3: [4, 6]
4: [1, 6]
5: [1, 5]
6: [1, 4]
Status: It's your turn to make a move. Enter your command.
> 6
Illegal move. Please try again.
======================================================================
Stock size: 14
Computer pieces: 5
[1, 1][1, 0][0, 0]
Your pieces:
1: [3, 4]
2: [5, 6]
3: [4, 6]
4: [1, 6]
5: [1, 5]
6: [1, 4]
Status: It's your turn to make a move. Enter your command.
>
Invalid input. Please try again.
======================================================================
Stock size: 14
Computer pieces: 5
[1, 1][1, 0][0, 0]
Your pieces:
1: [3, 4]
2: [5, 6]
3: [4, 6]
4: [1, 6]
5: [1, 5]
6: [1, 4]
Status: It's your turn to make a move. Enter your command.
> -5
======================================================================
Stock size: 14
Computer pieces: 5
[5, 1][1, 1][1, 0][0, 0]
Your pieces:
1: [3, 4]
2: [5, 6]
3: [4, 6]
4: [1, 6]
5: [1, 4]
Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 14
Computer pieces: 4
[5, 1][1, 1][1, 0][0, 0][0, 2]
Your pieces:
1: [3, 4]
2: [5, 6]
3: [4, 6]
4: [1, 6]
5: [1, 4]
Status: It's your turn to make a move. Enter your command.
> 2
Illegal move. Please try again.
======================================================================
Stock size: 14
Computer pieces: 4
[5, 1][1, 1][1, 0][0, 0][0, 2]
Your pieces:
1: [3, 4]
2: [5, 6]
3: [4, 6]
4: [1, 6]
5: [1, 4]
Status: It's your turn to make a move. Enter your command.
> -2
======================================================================
Stock size: 14
Computer pieces: 4
[6, 5][5, 1][1, 1][1, 0][0, 0][0, 2]
Your pieces:
1: [3, 4]
2: [4, 6]
3: [1, 6]
4: [1, 4]
Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 14
Computer pieces: 3
[6, 5][5, 1][1, 1]...[0, 0][0, 2][2, 6]
Your pieces:
1: [3, 4]
2: [4, 6]
3: [1, 6]
4: [1, 4]
Status: It's your turn to make a move. Enter your command.
> 2
======================================================================
Stock size: 14
Computer pieces: 3
[6, 5][5, 1][1, 1]...[0, 2][2, 6][6, 4]
Your pieces:
1: [3, 4]
2: [1, 6]
3: [1, 4]
Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 14
Computer pieces: 2
[6, 5][5, 1][1, 1]...[2, 6][6, 4][4, 5]
Your pieces:
1: [3, 4]
2: [1, 6]
3: [1, 4]
Status: It's your turn to make a move. Enter your command.
> -2
======================================================================
Stock size: 14
Computer pieces: 2
[1, 6][6, 5][5, 1]...[2, 6][6, 4][4, 5]
Your pieces:
1: [3, 4]
2: [1, 4]
Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 14
Computer pieces: 1
[3, 1][1, 6][6, 5]...[2, 6][6, 4][4, 5]
Your pieces:
1: [3, 4]
2: [1, 4]
Status: It's your turn to make a move. Enter your command.
> 1
Illegal move. Please try again.
======================================================================
Stock size: 14
Computer pieces: 1
[3, 1][1, 6][6, 5]...[2, 6][6, 4][4, 5]
Your pieces:
1: [3, 4]
2: [1, 4]
Status: It's your turn to make a move. Enter your command.
> -1
======================================================================
Stock size: 14
Computer pieces: 1
[4, 3][3, 1][1, 6]...[2, 6][6, 4][4, 5]
Your pieces:
1: [1, 4]
Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 14
Computer pieces: 0
[4, 3][3, 1][1, 6]...[6, 4][4, 5][5, 3]
Your pieces:
1: [1, 4]
Status: The game is over. The computer won!
```

-------------------------------------------------------------------------------

Python 3.10.4
numpy 1.22.4
pandas 1.4.2
scikit-learn 1.1.1
