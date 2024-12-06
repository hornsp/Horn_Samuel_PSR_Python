Paper, Scissors, Rock Game
This project implements a concurrent version of the "Paper, Scissors, Rock" game using Python, where two players interact with a referee program over sockets. The game runs in parallel, 
simulating multiple rounds where each player makes a move (Rock, Paper, or Scissors), and the referee determines the winner.

Written by
Samuel Horn

Overview
The project consists of four Python scripts that coordinate the execution of the game:
* play.py: The main coordinator that starts the game by spawning the referee and two player processes. It manages the flow of the game, ensuring that players and the referee interact as expected.
* referee.py: The referee program that listens for connections from the players and manages the game logic, including determining the winner for each round.
* player.py: Represents each player. Players connect to the referee, send their moves, and receive instructions from the referee.
* readstr.py: A utility module that defines a function (read_string) used to read messages from a socket connection. It is used by both the referee and players to handle incoming data.

How to Run
1. Ensure all Python scripts (play.py, referee.py, player.py, readstr.py) are in the same directory.
2. Open a terminal window and navigate to the directory containing the scripts.
3. Run the game by executing the following command:

python play.py <number_of_turns>

For example, to play 3 rounds:

python play.py 3

The program will start the game and output the results of each round, along with the final score.

Sample Output

> python play.py 3

Written by: Samuel Horn
Paper, Scissors, Rock: 3 iterations

Go Players 1
    Player 1: PAPER
    Player 2: PAPER
    Winner: Draw

Go Players 2
    Player 1: ROCK
    Player 2: SCISSORS
    Winner: Player 1 Wins

Go Players 3
    Player 1: PAPER
    Player 2: PAPER
    Winner: Draw


Final Score:
    Player 1: 1
    Player 2: 0

Player 1 Wins

Structure
* play.py: Starts the game, manages processes.
* referee.py: Listens for player connections and orchestrates the game logic.
* player.py: Represents the player logic (connects to the referee, makes moves).
* readstr.py: A utility to handle reading from socket connections.

Requirements
* Python 3.x
* A working environment with network support (local machine should suffice).

Dependencies
* socket library for network communication.
* random for selecting player moves.

How It Works
1. play.py starts the game by forking processes for the referee and the players.
2. referee.py listens for connections from both players. Once both players are ready, the referee sends them a "GO" message, prompting them to choose a move. After receiving the players' choices, the referee determines the winner and sends the result back to the players.
3. The game continues for the specified number of turns. Once the game ends, the referee sends a "STOP" message, and the players close their connections.
4. The results are displayed in the terminal.

Functions
* playCoordinator(): Handles the coordination of starting the referee and player processes and manages communication.
* gameLoop(): Controls the flow of the game in both the referee and player programs.
* makeChoice(): Randomly selects a move for the player (Rock, Paper, or Scissors).
* determineWinner(): Decides the winner based on the players' choices.
* read_string(): A utility function for reading data from socket connections.
