import torch
from game import TicTacToe
from vizuals import Vizuals
from ai import AI
import time
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
    return board00

def renderBoard(screen:Vizuals, boardData:TicTacToe):
    pass


def playerTurn(player):
    pass


def gameLoop(vizuals:Vizuals, board:TicTacToe, ai_O:AI, ai_X:AI,  ticRender=False):
    running = True
    board.resetBoard()
    while running:
        if ticRender:
            time.sleep(0.125)
            for event in vizuals.pyEvent():
                if event.type == pygame.QUIT:
                    running = False
            vizuals.clear()
            vizuals.draw_grid()
            vizuals.updateGrid(board)
            vizuals.update()
            if (board.gameOver()):
                time.sleep(.5)
                vizuals.clear()
            # print("=================")
            # board.printBoard()




        if (board.gameOver()):
            board.resetBoard()
            board.changeTurn(1)
            continue

        #to see if moves are even possible
        legalMovesListLen = len(board.getLegalMoves())
        if (legalMovesListLen == 0):
            board.resetBoard()
            continue

        #moves happen here
        if (board.getWhosTurn() == 1): 
            turn = ai_O.makeRandMove(board.getLegalMoves())
            
        #it's negative one then
        elif (board.getWhosTurn() == -1): 
                turn = ai_X.makeRandMove(board.getLegalMoves())

        #change whos turn for next time
        player = board.getWhosTurn()
        board.makeMove(player, turn)
        board.changeTurn()
        

        


        



def main():
    vizuals = Vizuals()
    ai_X = AI()
    ai_Y = AI()
    print(torch.__version__)
    print(torch.cuda.is_available())  # Returns True if you have a usable NVIDIA GPU
    ticTest = testTicBoard()
    gameLoop(vizuals, ticTest, ai_X, ai_Y, True)
    return


if __name__ == "__main__":
    main()
