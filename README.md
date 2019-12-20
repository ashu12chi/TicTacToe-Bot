# TicTacToe-Bot
This is a classical Tic Tac Toe game, you can play it with a Bot. But, remember advance bot is pro enough to prove you a Noob.
### Link to site:
 https://ashu12chi.github.io/TicTacToe-Bot/.
### In case you only want to play
https://github.com/ashu12chi/TicTacToe-Bot/blob/master/TicTacToe-Best.exe

### Python module required
   1. [gtts](https://pypi.org/project/gTTS/)
   2. [tkinter](https://docs.python.org/2/library/tkinter.html)
   3. [copy](https://docs.python.org/3/library/copy.html)
   4. [os](https://docs.python.org/3/library/os.html)
   5. [playsound](https://pypi.org/project/playsound/) 

This code is written for python3 but with very few changes it will work with python2 also.

## Game Rules
  http://web.cecs.pdx.edu/~bart/cs541-fall2001/homework/tictactoe-rules.html
  
## How to play
When you start the game, it will ask you to choose among two options: <br>
  1. Beginner <br>
  2. Advance <br>
Choose any one of the above two options, and play it with a Bot. <br>
Remember!!! It is very difficult to win at advance level.
## Algorithm explanation
1. Beginner: <br>
    It is using a very simple algorithm that follows following steps: <br>
        1. Check if AI can win in this step. <br>
        2. Check if player can win at next step. <br>
        3. Check if no moves left, game is a tie. <br>
        4. Find the first empty space and select it as a chance. <br>
2. Advance: <br>
    This is one of the basic algorithm used in game theory, Minimax algorithm. This algorithm is very effective when game is played between two players. <br>
    It recursively check all possible moves, and can select a move which will result in maximising its chance of victory.
 ### Problems
      Game may run little slow, based on your device performance due to text to speech library.
 ### Future Plans
      1. Currently, game supports only beginner and advance levels, however medium level is also necessary
      2. Improvement in GUI.
      3. Introduction of series of games with improvement in algorithm, on the basis if it is required to play in attacking way or defensive way.
