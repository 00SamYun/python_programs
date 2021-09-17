### Simple Command Line Hangman

This is a traditional 1 player hangman game.

It keeps track of each player's points which determines the type of hints they can get. 

This, along with other user information is stored in an SQL Database.

The game is meant to be played in the command line but can be played in an interactive shell as well.

Run the `main.py` file to play the game!

### Prerequisites

Please download the [DB Browser for SQLite](https://sqlitebrowser.org/dl/) or any other applications 
compatible for use with `sqlite3`. 

Please also create a [RapidApi](https://rapidapi.com/hub) account in order to use [WordsApi](https://www.wordsapi.com/). 
Or use other word APIs (and change the corresponding code in the `funcs.py` file).

### Variations

Creating a simple user interface with Python's [Turtle Graphics](https://docs.python.org/3/library/turtle.html).

Control the target word by allowing users to choose the categories/difficulties of the words.
