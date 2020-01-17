import os
from ttt_pkg.ttt import TTT_Board

def main():
    game = TTT_Board()
    game.runGame()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()