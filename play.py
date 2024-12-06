import sys
import subprocess

def playCoordinator():
    if len(sys.argv) != 2:
        print("Usage: python play.py <# of turns>")
        sys.exit(1)

    turns_arg = sys.argv[1]
    turns = int(turns_arg)

    print(f'''
Written by: Samuel Horn
Paper, Scissors, Rock: {turns} iterations
    ''')

    # Start referee process
    referee_process = subprocess.Popen(["python", "referee.py", str(turns)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Start player 1 process
    player1_process = subprocess.Popen(["python", "player.py", "1", "8080"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Start player 2 process
    player2_process = subprocess.Popen(["python", "player.py", "2", "8080"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Wait for all processes to finish execution
    referee_output, referee_error = referee_process.communicate()
    player1_output, player1_error = player1_process.communicate()
    player2_output, player2_error = player2_process.communicate()

    # Print referee output
    if referee_output:
        print(referee_output.decode())

    # Print player 1 output
    if player1_output:
        print(player1_output.decode())

    # Print player 2 output
    if player2_output:
        print(player2_output.decode())

def main():
    playCoordinator()

if __name__ == "__main__":
    main()
