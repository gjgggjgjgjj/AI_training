import random
import torch
import torch.nn as nn

class AI(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(9,64),
            nn.ReLU(),

            nn.Linear(64,64),
            nn.ReLU(),

            nn.Linear(64, 9)
        )
        
        wins = 0
        loses = 0

    def forward(self, x):
        return self.network

    def makeRandMove(self,moves:list):
        if (len(moves) == 1):
            return moves[0]
        if (len(moves) == 0):
            raise Exception("Moves list is nonetype or zero")
        #will return index of move from possible moves
        leRange = len(moves)

        index = random.randint(0, leRange - 1)
        move = moves[index]
        return move
