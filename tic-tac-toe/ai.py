import random

class AI:
    def __init__(self):
        wins = 0
        loses = 0

    def makeRandMove(self,moves:list):
        if (len(moves) == 0):
            raise Exception("Moves list is nonetype or zero")
        #will return index of move from possible moves
        leRange = len(moves)

        index = random.randint(0, leRange - 1)
        move = moves[index]
        return move
