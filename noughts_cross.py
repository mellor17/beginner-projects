# Noughts and Crosses game

# created using guidance from this site: https://realpython.com/tic-tac-toe-python/#step-4-process-players-moves-on-the-game-board


'''NOTES ON CLASSES and objects ---just fucking notes:
Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg.: My class.Myattribute

Generators:

A generator is a function that returns an iterator that produces a sequence of values when iterated over.

'''


import tkinter as tk # import tkinter library This is defining tkinter as TK in the global namespace of the program
from tkinter import font # import font module from TK lib
from typing import NamedTuple # imports NamedTuple module from typing lib
from itertools import cycle # Allows us to create an iterator which returns elements and saves it or returns it


class Players(NamedTuple): # Defines our Players class equal to =  Players = collections.namedtuple('label', ['name', 'color'])

     label: str # Will store player X or O
     color: str #  Holds a string of a tkinter colour, used to identify the players

class Move(NamedTuple): # Defines our movement class
     rows: int 
     cols: int # ^ this and the above line store their relative coordinate of where the player has clicked
     label: str = '' # stores our player as either X or O

BOARD_SIZE = 3 # constant defines our board size
DEFAULT_PLAYERS = ( # two-item tuple which defines ou players
     Player(label='X', colour="blue"),
     Player(label="O", colour="red")
)

class GameLogic: # IN this intialiser/constructor we define all attributes which make up the game # board_size determines n
 
     def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE): # p2layers arg will hold tuple of two str either X OR O our players
          self._players = cycle(players) # Iterators from itertools which will iterate over the tuple players so basically choosing the terms
          self._board_size = board_size # size of board
          self._current_player = next(players) # calls the next item from player iterable  but defines current player during runtime                                                                   
          self._winner = False # whether a player has won or not
          self._winner_combo = [] # the combination of cells that define a win 
          self._winning_combinations = [] # defines all? winning combos                                                                    
          self._player_moves = [] # current moves in the game, so int + list of game coordinates
          self._setup_game_board = []


     def _setup_game_board(self):
          self._player_moves = [ # makes a list comprehension to provide intial values for current moves [list of a list]
               [Move(row, col) for col in range(self._board_size)] # empty move object will store players move
               for row in range(self._board_size)
          ]
          self._winning_combinations = self._get_winning_combos() # assigns the get_W_combos function to winning combos                                                                                                


     def _get_winning_combos(self):  # this is the function for calculating all of the possible winning outcome 8 in total
          rows = [[(move.row, move.col) for move in row] # list which contains the coordinates of each postion on board
                 for row in self._player_moves
            ]       # the below creates a list called columns which transposes rows by using the zip basically turn rows into columns
          columns = [list(col) for col in zip(*rows)] #Yield tuples until an input is exhausted at n length, where n is the number of positional arguments
          first_diagonal = [row[i] for i, row in enumerate(rows)]
          second_diagonal = [row[j] for j, row in enumerate(reversed(rows))]
          return rows + columns + [first_diagonal + second_diagonal]
     

     def _is_valid_move(self, move):
          """Return True if move is valid and follows therse parameters there is no winner, and current move has not been played"""
          row, col = move.row, move.col # collects .row and .col coordinated from input move
          move_was_not_played = self._current_moves[row][col].label == "" #  checks if current move is still empty so no move has been played
          no_winner = not self._winner # checks to ensure there is no winner
          return no_winner and move_was_not_played # will return a boolean vaule dependent on the output from the two variables
     

     def process_move(self, move): # defines our moving function taking the move object as an arg from THE MOVE class
          # process current player move to see if it is a win
          row, col = move.row, move.col  # collects .row and .col coordinated from input move
          self._player_moves[row][col] = move # assigns current rows and column to the current move objec
          for combo in self._winning_combinations: # iterates over each winning combination until it matches
               results = set(
                    self._player_moves[n][m].label
                    for n, m in combo
               )
               # the above is a  generator expression that retrieves all the labels from the moves in the current winning combination. The result is then converted into a set.
               is_win = (len(results) == 1) and ("" not in results) # boolean expression which checks whether the current move is determined  a win
               if is_win: # checks whether a win is present and the values which define it, will then terminate function
                    self._winner =  True
                    self._winner_combo
                    break


class NoughtsandCrossBoard(tk.Tk): # Defines the games GUI and (Derived Class)class which inherits its data from the previously defined Tk class
    def __init__(self): # Initialiser class for code calls all of the defined functions/variables in 
        super().__init__()
        self.title("Noughts and Crosses Game")
        self._cells = {} # provides dictonary where we store each row and column
        self._create_board_grid() # adds rows and cols
        self._create_board_display() # creates backgorund display for game


    def _create_board_display(self):
        display_frame = tk.Frame(master=self,) # Creates a frame object for the GUI, master args are set to self meaning the main window will be the frame's parent
        display_frame.pack(fill=tk.X) # this will resize window to whatever the user moves it to and ensure the frame fills it's width
        self.display = tk.Label(
            master=display_frame,
            text="Ready you maggot?",
            font=font.Font(size=28, weight='bold',),
        )
        self.display.pack() 

    def _create_board_grid(self): #Creates tk Frame to hold each of the games cells (where x and o are located)
        grid_frame = tk.Frame(master=self) # master is self so the frames parent wll be the game window
        grid_frame.pack()
        for row in range(3):   # for loop which iterates from 0 to 2, (so 3) determines number of cells/rows on grid
            grid_frame.rowconfigure(row, weight=1, minsize=50) # changed from self to grid_frame 
            grid_frame.columnconfigure(row, weight=1, minsize=75)  # ^ configures min size and width of each cell on the grid
            for col in range (3): # same as line 26 but determines number of columns
                button = tk.Button( # Creates button tk object for every cell, setting several attributes like the master, foreground colour etc
                    master=grid_frame,
                    text="",
                    fg="black",
                    font=font.Font(size=36, weight='bold'),
                    width=3,
                    height=3,
                    #background='blue',
                    #activebackground='lightblue',
                    
                )


                self._cells[button] = (row, col) # adds each button to the Dictionary [_cells] on line 11, buttons are they keys whilst the rows and cols are values
                button.grid( # adds eacn button to our game by using .grid (Tkinter geomety manager)
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky='nsnew')
                


def main():
        board = NoughtsandCrossBoard()
        board.mainloop()

if __name__ == "__main__":
    main()

