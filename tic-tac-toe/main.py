# import torch
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
            time.sleep(0.5)
            for event in vizuals.pyEvent():
                if event.type == pygame.QUIT:
                    running = False
            vizuals.draw_grid()
            vizuals.updateGrid(board)
            vizuals.update()
            if (board.gameOver()):
                time.sleep(2)
                vizuals.clear()



        if (board.gameOver()):
            board.resetBoard()


        #moves will happen here
        legalMovesListLen = len(board.getLegalMoves())
        if (board.getWhosTurn() == 1 and legalMovesListLen > 0):
            turn = ai_O.makeRandMove(board.getLegalMoves())
            
        #it's negative one then
        elif (legalMovesListLen > 0):
                turn = ai_X.makeRandMove(board.getLegalMoves())

        #change whos turn for next time
        player = board.getWhosTurn()
        board.makeMove(player, turn)
        board.changeTurn()
        

        


        



def main():
    vizuals = Vizuals()
    ai_X = AI()
    ai_Y = AI()
    # print(torch.__version__)
    # print(torch.cuda.is_available())  # Returns True if you have a usable NVIDIA GPU
    ticTest = testTicBoard()
    gameLoop(vizuals, ticTest, ai_X, ai_Y, True)
    return


if __name__ == "__main__":
    main()
