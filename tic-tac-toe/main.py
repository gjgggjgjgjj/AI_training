# import torch
from game import TicTacToe
from vizuals import Vizuals
import pygame

def testTicBoard():
    board00 = TicTacToe()
    board00.printBoard()
    board00.makeMove(1,8)
    board00.makeMove(-1,7)
    print()
    board00.printBoard()
    print()
    board00.makeMove(1,0)
    board00.makeMove(1,1)
    board00.makeMove(1,2)
    board00.printBoard()
    # print(board00.playerWon(-1))
    # print(board00.playerWon(1))
    # board00.makeMove(-1,0)
    board00.printBoard()

def renderBoard(screen:Vizuals, boardData:TicTacToe):
    pass


def playerTurn(player):
    pass


def gameLoop(vizuals:Vizuals, render=False):
    running = True
    while running:
        if render:
            for event in vizuals.pyEvent():
                if event.type == pygame.QUIT:
                    running = False
            vizuals.draw_grid()
            vizuals.update()

        

    pass


def main():
    vizuals = Vizuals()
    # print(torch.__version__)
    # print(torch.cuda.is_available())  # Returns True if you have a usable NVIDIA GPU
    testTicBoard()
    gameLoop(vizuals, True)
    return


if __name__ == "__main__":
    main()
