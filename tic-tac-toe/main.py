# import torch
from game import TicTacToe

def testTicBoard():
    board00 = TicTacToe()
    board00.printBoard()
    board00.drawChar(1,8)
    board00.drawChar(-1,7)
    print()
    board00.printBoard()
    print()
    board00.drawChar(1,0)
    board00.drawChar(1,1)
    board00.drawChar(1,2)
    board00.printBoard()
    print(board00.playerWon(-1))
    print(board00.playerWon(1))




def main():
    # print(torch.__version__)
    # print(torch.cuda.is_available())  # Returns True if you have a usable NVIDIA GPU
    testTicBoard()
    return


if __name__ == "__main__":
    main()
