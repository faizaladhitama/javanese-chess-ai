import os
import random
import sys
import time

import pygame

import Catur_Jawa as cj

BOARDWIDTH = 3  # number of columns in the board
BOARDHEIGHT = 3  # number of rows in the board

WINDOWWIDTH = 1080
WINDOWHEIGHT = 640

# XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
# YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
BGCOLOR = pygame.image.load(os.path.join("images", "bg.png"))
BOARD = pygame.image.load(os.path.join("images", "board.png"))

BLUE_PION = pygame.image.load(os.path.join("images", "blue.png"))
PINK_PION = pygame.image.load(os.path.join("images", "pink.png"))
YELLOW_SPOT = pygame.image.load(os.path.join("images", "yellow_spot.png"))
GREEN_SPOT = pygame.image.load(os.path.join("images", "green_spot.png"))
WIN = pygame.image.load(os.path.join("images", "You_Win.png"))
WIN_YES = pygame.image.load(os.path.join("images", "You_Win.png"))
WIN_NO = pygame.image.load(os.path.join("images", "You_Win.png"))
LOSE = pygame.image.load(os.path.join("images", "You_Lose.png"))
LOSE_YES = pygame.image.load(os.path.join("images", "You_Lose_YES.png"))
LOSE_NO = pygame.image.load(os.path.join("images", "You_Lose_NO.png"))
YOUR_TURN = pygame.image.load(os.path.join("images", "your_turn.png"))
AI_TURN = pygame.image.load(os.path.join("images", "ai_turn.png"))
SELECTED = pygame.image.load(os.path.join("images", "selected_spot.png"))
DIFFICULT = pygame.image.load(os.path.join("images", "difficult.png"))
EASY = pygame.image.load(os.path.join("images", "difficult_EASY.png"))
MEDIUM = pygame.image.load(os.path.join("images", "difficult_MEDIUM.png"))
HARD = pygame.image.load(os.path.join("images", "difficult_HARD.png"))
CREDIT = pygame.image.load(os.path.join("images", "credit.png"))
HOVER_CREDIT = pygame.image.load(os.path.join("images", "credit_clicked.png"))
CREDIT_SOUND = pygame.image.load(os.path.join("images", "credit_is.png"))


class BoardGUI:
    turn = 1

    def __init__(self, surface):
        self.game_over = False
        self.surface = surface
        self.surface.blit(BGCOLOR, (0, 0))
        self.comeFrom = None
        self.Aboard = cj.Board()
        self.board = ""
        self.human = cj.Human()
        self.ai = cj.AI()

    def getHuman(self):
        return self.human

    def getAI(self):
        return self.ai

    def getAboard(self):
        return self.Aboard

    def setup(self):
        self.surface.blit(BGCOLOR, (0, 0))
        self.surface.blit(pygame.transform.scale(BOARD, (WINDOWHEIGHT - 50, WINDOWHEIGHT - 50)), (250, 25))
        self.Aboard.assign_pawn_to_board(self.human, self.ai)
        self.Aboard.set_player({'Human': self.human, 'AI': self.ai})
        pygame.display.set_caption('Catur Jawa by Tanpa Nama')
        self.board = self.Aboard.display_matrix()
        self.draw()

    def draw(self, highlightSquares=[],selectedNode=None):
        # draw blank board
        boardSize = len(self.board)
        current_square = 0
        for r in range(boardSize):
            for c in range(boardSize):
                (screenX, screenY) = self.ConvertToScreenCoords((r, c))
                print((screenX, screenY))
                self.surface.blit(pygame.transform.scale(YELLOW_SPOT, (50, 50)), (screenX, screenY))
                current_square = (current_square + 1) % 2

            current_square = (current_square + 1) % 2

        print(highlightSquares)
        

        for square in highlightSquares:
            (screenX, screenY) = self.ConvertToScreenCoords(square)
            self.surface.blit(pygame.transform.scale(GREEN_SPOT, (50, 50)), (screenX, screenY))

        for r in range(boardSize):
            for c in range(boardSize):
                (screenX, screenY) = self.ConvertToScreenCoords((r, c))
                if self.board[r][c] == 'Human':
                    self.surface.blit(pygame.transform.scale(BLUE_PION, (50, 50)), (screenX, screenY))
                elif self.board[r][c] == 'AI':
                    self.surface.blit(pygame.transform.scale(PINK_PION, (50, 50)), (screenX, screenY))
        print(self.board)
        print("cekin")
        if(selectedNode is not None):
            (selectedTupplex, selectedTuppley)=self.fromNodeToMatrix(selectedNode)
            (selectedRow, selectedColumn) = self.ConvertToScreenCoords((selectedTupplex,selectedTuppley))
            self.surface.blit(pygame.transform.scale(SELECTED, (50, 50)), (selectedRow, selectedColumn))
        pygame.display.flip()

    def convertMatrixToNode(self, node):
        (X, Y) = node
        for i in range(3):
            for j in range(3):
                print(i, j)
                if X == i and Y == j:
                    print("masuk")
                    return (6 - (i * 3)) + j

        """
        if X == 0 and Y == 0:
            return 6
        elif X == 1 and Y == 0:
            return 3
        elif X == 2 and Y == 0:
            return 0
        elif X == 0 and Y == 1:
            return 7
        elif X == 1 and Y == 1:
            return 4
        elif X == 2 and Y == 1:
            return 1
        elif X == 0 and Y == 2:
            return 8
        elif X == 1 and Y == 2:
            return 5
        elif X == 2 and Y == 2:
            return 2
        """

    def checkValidMove(self, possible_move,node):
        print(possible_move)
        isValid = []
        for i in possible_move:
            isValid.append(i)
        print(isValid)
        self.draw(isValid,node)

    def fromNodeToMatrix(self, node):
        for i in range(9):
            if i == node:
                return (2 - int(i / 3), i % 3)
        """
        if (node == 0):
            return (2, 0)
        elif (node == 1):
            return (2, 1)
        elif (node == 2):
            return (2, 2)
        elif (node == 3):
            return (1, 0)
        elif (node == 4):
            return (1, 1)
        elif (node == 5):
            return (1, 2)
        elif (node == 6):
            return (0, 0)
        elif (node == 7):
            return (0, 1)
        elif (node == 8):
            return (0, 2)
        """

    def ConvertToScreenCoords(self, chessSquareTuple):
        # converts a (row,col) chessSquare into the pixel location of the upper-left corner of the square
        (row, col) = chessSquareTuple
        screenX = 300 + col * 220
        screenY = 80 + row * 220
        return (screenX, screenY)

    def ConvertToChessCoords(self, screenPositionTuple):
        # converts a screen pixel location (X,Y) into a chessSquare tuple (row,col)
        # x is horizontal, y is vertical
        # (x=0,y=0) is upper-left corner of the screen
        (X, Y) = screenPositionTuple
        row = int((Y - 80) / 220)
        col = int((X - 300) / 220)
        return (row, col)

    def move_by_mouse(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pion_put = pygame.mixer.Sound(os.path.join("music","put_pion.wav"))
                    pion_put.play()
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    print(mouseX, mouseY)
                    matrixNode = self.ConvertToChessCoords((mouseX, mouseY))
                    print("Matrix node :", matrixNode)
                    node = self.convertMatrixToNode(matrixNode)
                    print("Node :", node)
                    return node
            clock.tick(30)
    def getTurn(self):
        first_turn = "Human"
        turn = []
        if random.random() > 0.5:
            first_turn = "AI"
        if first_turn == "Human":
            turn = ["Human", "AI"]
        else:
            turn = ["AI", "Human"]
        print(turn)
        return turn
    def get_winner(self,now):
        winner = ""
        if now == "Human":
            winner = "AI"
        else:
            winner = "Human"
        return winner

    def choose_difficult(self,diff):
        choices = {'Easy': 2, 'Normal': 4, 'Hard': 6}
        return choices.get(diff, 4)

    def debugMenu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEMOTION:
                        x, y = event.pos
                        print("x",x)
                        print("y",y)
                        if(x in range(256,452) and y in range(352,420)):
                            self.surface.blit(pygame.transform.scale(CREDIT, (200, 100)), (WINDOWWIDTH-200, 0))
                            self.surface.blit(pygame.transform.scale(EASY, (605, 330)), (243, 160))
                            pygame.display.update()
                        elif(x in range(462,658) and y in range(352,420)):
                            self.surface.blit(pygame.transform.scale(CREDIT, (200, 100)), (WINDOWWIDTH-200, 0))
                            self.surface.blit(pygame.transform.scale(MEDIUM, (605, 330)), (243, 160)) 
                            pygame.display.update()
                        elif(x in range(668,864) and y in range(352,420)):
                            self.surface.blit(pygame.transform.scale(CREDIT, (200, 100)), (WINDOWWIDTH-200, 0))
                            self.surface.blit(pygame.transform.scale(HARD, (605, 330)), (243, 160)) 
                            pygame.display.update()
                        elif(x in range(883,1076) and y in range(0,100)):
                            self.surface.blit(pygame.transform.scale(HOVER_CREDIT, (200, 100)), (WINDOWWIDTH-200, 0))
                            self.surface.blit(pygame.transform.scale(DIFFICULT, (605, 330)), (243, 160)) 
                            self.surface.blit(pygame.transform.scale(CREDIT_SOUND, (900, 600)), (0, 20)) 
                            pygame.display.update()
                        else:
                            self.surface.blit(BGCOLOR, (0, 0))
                            self.surface.blit(pygame.transform.scale(CREDIT, (200, 100)), (WINDOWWIDTH-200, 0))
                            self.surface.blit(pygame.transform.scale(DIFFICULT, (605, 330)), (243, 160)) 
                            pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP:
                        x, y = event.pos
                        print("x",x)
                        print("y",y)
                        if(x in range(256,452) and y in range(352,420)):
                            pion_put = pygame.mixer.Sound(os.path.join("music","put_pion.wav"))
                            pion_put.play()
                            return 'Easy'
                        elif(x in range(462,658) and y in range(352,420)):
                            pion_put = pygame.mixer.Sound(os.path.join("music","put_pion.wav"))
                            pion_put.play()
                            return 'Normal'
                        elif(x in range(668,864) and y in range(352,420)):
                            pion_put = pygame.mixer.Sound(os.path.join("music","put_pion.wav"))
                            pion_put.play()
                            return 'Hard'
                     
    def quit(self,winner):
        time.sleep(1)
        if(winner == "AI"):
            self.surface.blit(pygame.transform.scale(LOSE, (605, 330)), (243, 160))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEMOTION:
                        x, y = event.pos
                        print("x",x)
                        print("y",y)
                        if (x in range(340,472) and y in range(337,447)):
                            self.surface.blit(pygame.transform.scale(LOSE_YES, (605, 330)), (243, 160))
                            pygame.display.update()
                            print("x",x)
                            print("y",y)
                            print("Y")
                        
                        elif(x in range(619,750) and y in range(337,447)):
                            self.surface.blit(pygame.transform.scale(LOSE_NO, (605, 330)), (243, 160))
                            pygame.display.update()
                            print("x",x)
                            print("y",y)
                            print("N")
                        else:
                            self.surface.blit(pygame.transform.scale(LOSE, (605, 330)), (243, 160))
                            pygame.display.update()
                            print("x",x)
                            print("y",y)
                            print("Not N or Y?")
                    if event.type == pygame.MOUSEBUTTONUP:
                        if (x in range(340,472) and y in range(337,447)):
                            pion_put = pygame.mixer.Sound(os.path.join("music","put_pion.wav"))
                            pion_put.play()
                            return "Y"
                        
                        elif(x in range(619,750) and y in range(337,447)):
                            pion_put = pygame.mixer.Sound(os.path.join("music","put_pion.wav"))
                            pion_put.play()
                            return "N"
                    print("no even?")
        elif(winner == "Human"):
            self.surface.blit(pygame.transform.scale(WIN, (605, 330)), (243, 160))
            pygame.display.update()
            print("x",x)
            print("y",y)
            print("Not N or Y?")
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEMOTION:
                        x, y = event.pos
                        chose = False
                        print("x",x)
                        print("y",y)
                        if (x in range(341,377) and y in range(447,471)):
                            self.surface.blit(pygame.transform.scale(WIN_YES, (605, 330)), (243, 160))
                            pygame.display.update()
                            print("x",x)
                            print("y",y)
                            print("Y")
                        
                        elif(x in range(620,750) and y in range(447,471)):
                            self.surface.blit(pygame.transform.scale(WIN_NO, (605, 330)), (243, 160))
                            pygame.display.update()
                            print("x",x)
                            print("y",y)
                            print("N")
                        else:
                            self.surface.blit(pygame.transform.scale(WIN, (605, 330)), (243, 160))
                            pygame.display.update()
                            print("x",x)
                            print("y",y)
                            print("Not N or Y?")
                    if event.type == pygame.MOUSEBUTTONUP:
                        if (x in range(340,472) and y in range(337,447)):
                            pion_put = pygame.mixer.Sound(os.path.join("music","put_pion.wav"))
                            pion_put.play()
                            return "Y"
                        
                        elif(x in range(619,750) and y in range(337,447)):
                            pion_put = pygame.mixer.Sound(os.path.join("music","put_pion.wav"))
                            pion_put.play()
                            return "N"
                        else:
                            print("Not N or Y?")
                    print("no even?")
            print("out of loop?")

def play(has_play,difficult=None):
    winner = ""
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.mixer.pre_init(22050,-16,2,4096)
    pygame.HWSURFACE
    surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    gui = BoardGUI(surface)
    now = gui.getTurn()[0]
    print(now)

    #BACKSOUND = pygame.mixer.music.load(os.path.join("music", "backsound.mp3"))

    if(has_play == 0):
        difficult_sound = pygame.mixer.Sound(os.path.join("music","difficult_backsound.wav"))
        difficult_sound.play(-1)
        difficult_sound.set_volume(0.2)
        chosen_difficult = gui.debugMenu()
        print(chosen_difficult)
        difficult= gui.choose_difficult(chosen_difficult)
        difficult_sound.stop()
        has_play += 1
    if(has_play > 0):
        print(has_play)
        backsound = pygame.mixer.Sound(os.path.join("music","backsound.wav"))
        backsound.play(-1)
        backsound.set_volume(0.2)
        gui.setup()
        while not gui.getAboard().win_cond():
            gui.getAboard().set_turn(now)
            print("Now is {} turn\n".format(now))
            gui.getAboard().display_matrix()
            gui.draw()
            if (winner == ""):
                if (now == "Human"):
                    print("cek HU")
                    surface.blit(pygame.transform.scale(YOUR_TURN, (296, 96)), (0, 0))
                elif (now == "AI"):
                    surface.blit(pygame.transform.scale(AI_TURN, (296, 96)), (0, 0))
            gui.draw()
            if now == "Human":
                pawn = gui.getAboard().moveable_pawn(gui.getHuman())
                print("\nYour moveable pawns are on node :\n {} \n".format(gui.getAboard().print_list(pawn, True)))
            else:
                pawn = gui.getAboard().moveable_pawn(gui.getAI())

            if now == "AI":
                ai_sound = pygame.mixer.Sound(os.path.join("music","ai_sound.wav"))
                ai_sound.play(-1)
                # current_tile = int(pawn[int(math.floor(random.random() * len(pawn)))].get_coordinate())
 
                """
                print("Test Minimax :")
                now_time = time.time()
                current_tile, next_tile = ai.test_minimax(board, 6)
                after_time = time.time()
                print(after_time - now_time)
                print()
                """

                # """
                print("Test Alpha Beta Pruning :")
                print(has_play)
                print(difficult)
                now_time = time.time()
                current_tile, next_tile = gui.getAI().test_alpha_beta_pruning(gui.getAboard(), difficult)
                after_time = time.time()
                print("Running time :",after_time - now_time)
                print()
                ai_sound.stop()
                pion_put = pygame.mixer.Sound(os.path.join("music","put_pion.wav"))
                pion_put.play()
                # """

                """
                print("Test Iterative Deepning Alpha Beta Pruning :")
                now_time = time.time()
                current_tile, next_tile = gui.getAI().test_iterative_deepning_alpha_beta_pruning(gui.getAboard(), 6)
                after_time = time.time()
                print(after_time - now_time)
                print()
                """

            else:
                current_tile = gui.move_by_mouse()
                print("Choose your tile to move :\n {}".format(current_tile))

            notNone = gui.getAboard().checkEmptyNode(int(current_tile), now)
            if (notNone == "Good!"):
                print("cek")
                possible_move = gui.getAboard().pawn_moves(gui.getAboard().select_node(int(current_tile)))
                print("\nYou can move your pawn to node:\n {} \n".format(gui.getAboard().print_list(possible_move)))
                print(possible_move)

                list_possible_move_matrix = []
                for i in possible_move:
                    i_inMatrix = gui.fromNodeToMatrix(int(i))
                    list_possible_move_matrix.append(i_inMatrix)
                print(list_possible_move_matrix)
                gui.checkValidMove(list_possible_move_matrix,int(current_tile))

                if now == "AI":
                    print("Choose your next tile :\n {}".format(next_tile))
                else:
                    next_tile = gui.move_by_mouse()
                transition = gui.getAboard().pawn_transition(gui.getAboard().select_node(int(current_tile)),
                                                         gui.getAboard().select_node(int(next_tile)), now)
                print(transition)

                if now == "Human":
                    if (transition == "Good!"):
                        now = "AI"
                    else:
                        now = "Human"
                else:
                    now = "Human"
            else:
                now = "Human"
            print()

        gui.getAboard().display_matrix()
        print(gui.getAboard().get_node_list()[1])
        gui.draw()
        pygame.display.update()
        backsound.stop()
        winner = gui.get_winner(now)
        quit_response = gui.quit(winner)
        return quit_response, difficult

    """
    while (True):
        if now == "Human":
            winner = "AI"
            surface.blit(pygame.transform.scale(LOSE, (WINDOWHEIGHT - 100, WINDOWHEIGHT - 347)), (277, 180))
        else:
            winner = "Human"
            surface.blit(pygame.transform.scale(WIN, (WINDOWHEIGHT - 100, WINDOWHEIGHT - 347)), (277, 180))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()



        pygame.display.update()
    """
