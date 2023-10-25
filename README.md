## Python Guessing Game
---------------------------------------------------------------------------------------------------------------------
- Python guessing game is a simple project that will allow you to utilise the basic sections of the python programming language.
Just as the name sounds, its a guessing game, built on python, where the  program will generate a random number, and the user will be required to guess a number.
----------------------------------------------------------------------------------------------------------------------
#### Features
- A simple guessing game
- High score view board
----------------------------------------------------------------------------------------------------------------------
#### User story
- User A starts the python guessing game program, and is greeted with a menu, asking to choose an action (Similar to a ussd response.)
- The menu actions expected are (a) play (b) score (c) exit
- User A is now prompted to input a value corresponding to his/her desired action.
- Inputting a wrong value should display a message and ask for a new action to be selected.
-----------------------------------------------------------------------------------------------------------------------
#### Case (a) play
- If user A selects the option (a), he should be prompted to input his/her name.
- After this, the system generates a random number between 0-30 and the user will try to guess this number.
- Each play is allowed 10 tries, after which the game prints a failed attempt message, and returns to the welcome page.
- If user successfully guesses the number, within 10 tries, the user information, along with the number of tries used should be saved to a list.
---------------------------------------------------------------------------------------------------------------------- 
#### Optional goals
- Persist all high score information through program runs, using files.
- Sort the high score information based on tries.
- Limit high scoreboard list to 10 entries.
-----------------------------------------------------------------------------------------------------------------------

#### Case (b) board
- If user A chooses the option (b), he/she should be able to see the last 10 high scores, including names and tries used.
-----------------------------------------------------------------------------------------------------------------------

#### Case (c) Exit

- If user A selects the option (c), print a goodbye message, and proceed to exit the program.
-----------------------------------------------------------------------------------------------------------------------

**Note:** Program must not exit, except forecfully closed or user exits following the exit process. In order words, this is a continous running program
