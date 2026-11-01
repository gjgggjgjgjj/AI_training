from game import TicTacToe
import pygame

class Vizuals:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((900, 900))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    def clear(self):
        self.screen.fill((0,0,0))

    def update(self):
        pygame.display.flip()

    def getPygame(self):
        return pygame

    def pyEvent(self):
        return pygame.event.get()

    def draw_grid(self):


        color = (255, 255, 255)
        width = 5

        # Vertical lines
        pygame.draw.line(
            self.screen,
            color,
            (300, 100),
            (300, 800),
            width
        )

        pygame.draw.line(
            self.screen,
            color,
            (600, 100),
            (600, 800),
            width
        )

        # Horizontal lines
        pygame.draw.line(
            self.screen,
            color,
            (100, 300),
            (800, 300),
            width
        )

        pygame.draw.line(
            self.screen,
            color,
            (100, 600),
            (800, 600),
            width
        )

    def draw_x(self, center_x: int, center_y: int):

        size = 30
        width = 5
        color = (255, 0, 0)

        pygame.draw.line(
            self.screen,
            color,
            (center_x - size, center_y - size),
            (center_x + size, center_y + size),
            width
        )

        pygame.draw.line(
            self.screen,
            color,
            (center_x - size, center_y + size),
            (center_x + size, center_y - size),
            width
        )

    def draw_o(self, center_x: int, center_y: int):

        pygame.draw.circle(
            self.screen,
            (0, 0, 255),
            (center_x, center_y),
            35,
            5
        )

    #will return list of x and y cooardinate of center x and y based on move
    #move can only be number 0-8
    def boardTranslator(self, move: int) ->tuple:
        if (move == 0):
            return (150,150)
        if (move == 1):
            return (450,150)
        if (move == 2):
            return (750,150)
        if (move == 3):
            return (150,450)
        if (move == 4):
            return (450,450)
        if (move == 5):
            return (750,450)
        if (move == 6):
            return (150,750)
        if (move == 7):
            return (450,750)
        if (move == 8):
            return (750,750)
        else:
            raise Exception("invalid move choice inserted")

    def updateGrid(self, ticBoard:TicTacToe):
        board = ticBoard.getBoard()

        for i in range(len(board)):
            coordinates = self.boardTranslator(i)
            if (board[i] == 0):
                continue
            elif (board[i] == 1):
                self.draw_o(coordinates[0], coordinates[1])
            elif (board[i] == -1):
                self.draw_x(coordinates[0], coordinates[1])
            else:
                raise Exception("update grid move out of range")




#for testing below
if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 0, 0))

        pygame.display.flip()

    pygame.quit()
