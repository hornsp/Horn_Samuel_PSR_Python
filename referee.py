import socket
import sys
from readstr import read_string

HOST = "127.0.0.1"
PORT = 8080
BACKLOG = 2

def connectPlayers():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.bind((HOST, PORT))
            server_socket.listen(BACKLOG)
            
            player1_socket, _ = server_socket.accept()
            player2_socket, _ = server_socket.accept()

            player1_socket.sendall(b"READY\n")
            player2_socket.sendall(b"READY\n") 

            return player1_socket, player2_socket
        except Exception as e:
            print("An error has occurred while connecting players:", e)
            sys.exit(1)

def gameLoop(turns, player1_socket, player2_socket):    
    scorePlayer1 = 0
    scorePlayer2 = 0

    for turn in range(1, turns + 2):
        if turn != turns + 2:

            player1_socket.sendall(b"GO\n")
            player2_socket.sendall(b"GO\n")

            choice1 = read_string(player1_socket)
            choice2 = read_string(player2_socket)

            winner = determineWinner(choice1, choice2)

            if choice1 != "READY":
                
                printWinner(choice1, choice2, winner)

            if winner == "Player 1 Wins":
                scorePlayer1 += 1
            elif winner == "Player 2 Wins":
                scorePlayer2 += 1

            if turn != turns + 1:

                print(f"Go Players {turn}")

            player1_socket.sendall(winner.encode() + b"\n")
            player2_socket.sendall(winner.encode() + b"\n")


    print(f'''
Final Score:
    Player 1: {scorePlayer1}
    Player 2: {scorePlayer2}
''')
    if scorePlayer1 == scorePlayer2:
        print("Players Draw")
    elif scorePlayer1 > scorePlayer2:
        print("Player 1 Wins")
    else:
        print("Player 2 Wins")

def determineWinner(choice1, choice2):
    if choice1 == choice2:
        return "Draw"
    elif (choice1 == "ROCK" and choice2 == "SCISSORS") or \
         (choice1 == "SCISSORS" and choice2 == "PAPER") or \
         (choice1 == "PAPER" and choice2 == "ROCK"):
        return "Player 1 Wins"
    else:
        return "Player 2 Wins"

def printWinner(choice1, choice2, winner):
    print(f"    Player 1: {choice1}")
    print(f"    Player 2: {choice2}")
    print(f"    Winner: {winner}\n")

def score(winner, scorePlayer1, scorePlayer2):
    if winner == "Draw":
        pass
    elif winner == "Player 1 Wins":
        scorePlayer1 += 1
    else:
        scorePlayer2 += 1

    return scorePlayer1, scorePlayer2

def main(turns):
    player1_socket, player2_socket = connectPlayers()

    gameLoop(turns, player1_socket, player2_socket)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python referee.py <# of turns>")
        sys.exit(1)
    
    turns = int(sys.argv[1])
    main(turns)
