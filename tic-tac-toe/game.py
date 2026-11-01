
class TicTacToe:
    def __init__(self):
        self.board = [0,0,0,
                      0,0,0,
                      0,0,0]
        self.winStat =[
            #left to right
            [0,1,2],
            [3,4,5],
            [6,7,8],
            #cols
            [0,3,6],
            [1,4,7],
            [2,5,8],
            #diagonals
            [0,4,8],
            [2,4,6]
        ]
        self.whosTurn = 1

    def getBoard(self):
        return self.board

    def changeTurn(self):
        self.whosTurn *= -1

    def getWhosTurn(self):
        return self.whosTurn

    def resetBoard(self):
        for i in range(len(self.board)):
            self.board[i] = 0

    def playerWon(self,player):
        for wins in self.winStat:
            weWon = True
            for i in range(3):
                if self.board[wins[i]] != player:
                    weWon = False
                    # print("for testing here is win: ",wins)
                    # print("---------now here is win[i] when evaluated false",wins[i])
                    break
            if weWon:
                # print("we made it as true!!!")
                return weWon
        return weWon  #should be false at this point

    #we will also tell if there is a draw by if there are no more legal moves
    def getLegalMoves(self):
        retList = []
        for spot in range(len(self.board)):
            if self.board[spot] == 0:
                retList.append(spot)
        if retList == None:
            return False
        return retList

    def gameTie(self):
        if (self.getLegalMoves() == False):
            return True
        return False

    def gameOver(self):
        if (self.playerWon(1) or self.playerWon(-1) or self.gameTie()):
            return True

    #player is 1 or -1
    #will only allow if the move is legal otherwise error
    def makeMove(self,player,pos):
        if not (player == 1 or player == -1):
            raise Exception("Player is not 1 or -1: ", player)
        #pos can be 0-8   (so 9 places)
        if (self.board[pos] != 0):
            raise Exception("Illegal move made attempted for player", player, "tried to play on", pos, "item:",self.board[pos])
        self.board[pos] = int(player)

    #returns string
    def XorO(self,num):
        if num == 0:
            return "_"
        if num == 1:
            return "X"
        if num == -1:
            return "O"
        raise Exception("Error some board number wasn't 0,1,-1 result of error: ", num)
        
    #terminal testing to print the board into the terminal into Xs Os or _ 
    def printBoard(self):
        rows = 3
        cols = 3
        for row in range(rows):
            printRow = ["_","_","_"]
            for col in range(cols):
                index = (row * 3) + col
                character = self.XorO(self.board[index])
                printRow[col] = character
            print(printRow)

