import pygame, itertools,sys, random
import os
from pygame.locals import *
import Catur_Jawa as cj
import copy
import random
import time

BOARDWIDTH = 3  # number of columns in the board
BOARDHEIGHT = 3 # number of rows in the board

WINDOWWIDTH = 1080
WINDOWHEIGHT = 640

#XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
#YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
BGCOLOR = pygame.image.load(os.path.join("images","bg.jpg"))
BOARD = pygame.image.load(os.path.join("images","board.png"))

BLUE_PION = pygame.image.load(os.path.join("images","blue.png"))
PINK_PION = pygame.image.load(os.path.join("images","pink.png"))
YELLOW_SPOT = pygame.image.load(os.path.join("images","yellow_spot.png"))
PURPLE_SPOT = pygame.image.load(os.path.join("images","purple_spot.png"))
WIN = pygame.image.load(os.path.join("images","You_Win.png"))
LOSE = pygame.image.load(os.path.join("images","You_Lose.png"))
class BoardGUI:
	turn = 1
	def __init__(self,surface):
		self.game_over = False
		self.surface = surface
		self.surface.blit(BGCOLOR,(0,0))
		self.surface.blit(pygame.transform.scale(BOARD,(WINDOWHEIGHT-50,WINDOWHEIGHT-50)),(250,25))
		self.comeFrom = None
		self.Aboard = cj.Board()
		self.board = ""
		self.human = cj.Human()
		self.ai = cj.AI()
		self.setup()

	def getHuman(self):
		return self.human

	def getAI(self):
		return self.ai

	def getAboard(self):
		return self.Aboard

	def setup(self):
		self.Aboard.assign_pawn_to_board(self.human, self.ai)
		self.Aboard.set_player({'Human': self.human, 'AI': self.ai})
		pygame.display.set_caption('Catur Jawa by Tanpa Nama')
		self.board = self.Aboard.display_matrix()
		self.draw()

	def draw(self,highlightSquares=[]):
		#draw blank board
		boardSize = len(self.board)
		current_square = 0
		for r in range(boardSize):
			for c in range(boardSize):
				(screenX,screenY) = self.ConvertToScreenCoords((r,c))
				print((screenX,screenY))
				self.surface.blit(pygame.transform.scale(YELLOW_SPOT,(50,50)),(screenX,screenY))
				current_square = (current_square+1)%2

			current_square = (current_square+1)%2

		print(highlightSquares)

		for square in highlightSquares:
			(screenX,screenY) = self.ConvertToScreenCoords(square)
			self.surface.blit(pygame.transform.scale(PURPLE_SPOT,(50,50)),(screenX,screenY))

		for r in range(boardSize):
			for c in range(boardSize):
				(screenX,screenY) = self.ConvertToScreenCoords((r,c))
				if(self.board[r][c] == 'Human'):
					self.surface.blit(pygame.transform.scale(BLUE_PION,(50,50)),(screenX,screenY))
				elif(self.board[r][c] == 'AI'):
					self.surface.blit(pygame.transform.scale(PINK_PION,(50,50)),(screenX,screenY))
		print(self.board)
		print("cekin")

		pygame.display.flip()

	def convertMatrixToNode(self, node):
		(X,Y) = node
		if(X == 0 and Y == 0):
			return 6
		elif(X == 1 and Y == 0):
			return 7
		elif(X == 2 and Y == 0):
			return 0
		elif(X == 0 and Y == 1):
			return 5
		elif(X == 1 and Y == 1):
			return 8
		elif(X == 2 and Y == 1):
			return 1
		elif(X == 0 and Y == 2):
			return 4
		elif(X == 1 and Y == 2):
			return 3
		elif(X == 2 and Y == 2):
			return 2

	def checkValidMove(self,possible_move):
		print(possible_move)
		isValid= []
		for i in possible_move:
			isValid.append(i)
		print(isValid)
		self.draw(isValid)

	def fromNodeToMatrix(self, node):
		if(node == 0):
			return (2,0)
		elif(node == 1):
			return (2,1)
		elif(node == 2):
			return (2,2)
		elif(node == 3):
			return (1,2)
		elif(node == 4):
			return (0,2)
		elif(node == 5):
			return (0,1)
		elif(node == 6):
			return (0,0)
		elif(node == 7):
			return (1,0)
		elif(node == 8):
			return (1,1)

	def ConvertToScreenCoords(self,chessSquareTuple):
		#converts a (row,col) chessSquare into the pixel location of the upper-left corner of the square
		(row,col) = chessSquareTuple
		screenX = 300 + col*220
		screenY = 80 + row*220
		return (screenX,screenY)

	def ConvertToChessCoords(self,screenPositionTuple):
		#converts a screen pixel location (X,Y) into a chessSquare tuple (row,col)
		#x is horizontal, y is vertical
		#(x=0,y=0) is upper-left corner of the screen
		(X,Y) = screenPositionTuple
		row = int((Y-80) / 220)
		col = int((X-300) / 220)
		return (row,col)

	def move_by_mouse(self):
		clock = pygame.time.Clock()
		while True:
			for event in pygame.event.get():
				if(event.type == QUIT):
					pygame.quit()
					sys.exit()
				elif(event.type == MOUSEBUTTONUP):
					(mouseX,mouseY) = pygame.mouse.get_pos()
					matrixNode = self.ConvertToChessCoords((mouseX,mouseY))
					node = self.convertMatrixToNode(matrixNode)
					return node
			clock.tick(30)

def main() :
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	gui = BoardGUI(surface)
	first_turn = "Human"
	if random.random() > 0.5:
		first_turn = "AI"
	if first_turn == "Human":
		turn = ["Human", "AI"]
	else:
		turn = ["AI", "Human"]

	now = turn[0]
	while not gui.getAboard().win_cond():
		gui.getAboard().set_turn(now)
		print("Now is {} turn\n".format(now))
		gui.getAboard().display_matrix()
		gui.draw()
		if now == "Human":
			pawn = gui.getAboard().moveable_pawn(gui.getHuman())
		else:
			pawn = gui.getAboard().moveable_pawn(gui.getAI())

		if now == "AI":
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
			now_time = time.time()
			current_tile, next_tile = gui.getAI().test_alpha_beta_pruning(gui.getAboard(), 5)
			after_time = time.time()
			print(after_time - now_time)
			print()
			# """
		else:
			current_tile = gui.move_by_mouse()
			print("Choose your tile to move :\n {}".format(current_tile))

		notNone = gui.getAboard().checkEmptyNode(int(current_tile), now)
		if(notNone == "Good!"):
			print("cek")
			possible_move = gui.getAboard().pawn_moves(gui.getAboard().select_node(int(current_tile)))
			print("\nYou can move your pawn to node:\n {} \n".format(gui.getAboard().print_list(possible_move)))
			print(possible_move)

			list_possible_move_matrix = []
			for i in possible_move:
				i_inMatrix = gui.fromNodeToMatrix(int(i))
				list_possible_move_matrix.append(i_inMatrix)
			print(list_possible_move_matrix)
			gui.checkValidMove(list_possible_move_matrix)

			if now == "AI":
				print("Choose your next tile :\n {}".format(next_tile))
			else:
				next_tile = gui.move_by_mouse()
			transition = gui.getAboard().pawn_transition(gui.getAboard().select_node(int(current_tile)), gui.getAboard().select_node(int(next_tile)), now)
			print(transition)

			if now == "Human":
				if(transition == "Good!"):
					now = "AI"
				else:
					now = "Human"
			else:
				now = "Human"
		else:
			now = "Human"

		print()
	gui.getAboard().display_matrix()
	gui.draw()
	while(True):
		if now == "Human":
			winner = "AI"
			surface.blit(pygame.transform.scale(LOSE,(WINDOWHEIGHT-100,WINDOWHEIGHT-347)),(277,180))
		else:
			winner = "Human"
			surface.blit(pygame.transform.scale(WIN,(WINDOWHEIGHT-100,WINDOWHEIGHT-347)),(277,180))
		for event in pygame.event.get():
				if(event.type == QUIT):
					pygame.quit()
					sys.exit()

		pygame.display.update()


main()