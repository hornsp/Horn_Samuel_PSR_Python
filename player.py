import socket
import sys
import random
from readstr import read_string

HOST = "127.0.0.1"
PORT = 8080
BACKLOG = 2

def connectToRef(player_id, referee_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as player_socket:
        player_socket.connect((HOST, referee_port))

def gameLoop(player_id, player_socket):
    try:
        while True:
            instruction = read_string(player_socket)
            if instruction == "GO":
                choice = makeChoice()
                player_socket.sendall(choice.encode() + b"\n")
                result = read_string(player_socket)

            elif instruction == "STOP":
                break
    except Exception as e:
        sys.exit(1)

def makeChoice():
    choices = ["SCISSORS", "ROCK", "PAPER"]
    return random.choice(choices)

def main():
    if len(sys.argv) != 3:
        print("Usage: python player.py <player_id> <referee_port>")
        sys.exit(1)

    player_id = int(sys.argv[1])
    referee_port = int(sys.argv[2])

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as player_socket:
            player_socket.connect((HOST, referee_port))
            player_socket.sendall(b"READY\n")

            gameLoop(player_id, player_socket)
    except Exception as e:
        print(f"An error occurred in main for player {player_id}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
