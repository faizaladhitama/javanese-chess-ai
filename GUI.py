import pygame, itertools,sys, random
import os
from pygame.locals import *

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

class Pion():
	def __init__(self, x, y,color):
		self.x = x
		self.y = y
		self.color = color

	def setColor(self):
		if(self.color == "blue"):
			self.pion = BLUE_PION
		elif(self.color == "pink"):
			self.pion = PINK_PION

class Board():
	turn = 1
	def __init__(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		self.surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
		self.game_over = False
		self.surface.blit(BGCOLOR,(0,0))
		self.surface.blit(pygame.transform.scale(BOARD,(WINDOWHEIGHT-50,WINDOWHEIGHT-50)),(250,25))
		self.clicked = 0
		self.comeFrom = None
		self.board = [['p','p','p'],['e','e','e'],['b','b','b']]
		self.setup()

	def setup(self):
		pygame.display.set_caption('Catur Jawa by Tanpa Nama')
		self.draw()

	def draw(self,highlightSquares=[(1,1)]):
		#draw blank board
		print(self.board)
		boardSize = len(self.board)
		current_square = 0
		for r in range(boardSize):
			for c in range(boardSize):
				(screenX,screenY) = self.ConvertToScreenCoords((r,c))
				print((screenX,screenY))
				self.surface.blit(pygame.transform.scale(YELLOW_SPOT,(50,50)),(screenX,screenY))
				current_square = (current_square+1)%2

			current_square = (current_square+1)%2

		for square in highlightSquares:
			(screenX,screenY) = self.ConvertToScreenCoords(square)
			self.surface.blit(pygame.transform.scale(PURPLE_SPOT,(50,50)),(screenX,screenY))

		for r in range(boardSize):
			for c in range(boardSize):
				(screenX,screenY) = self.ConvertToScreenCoords((r,c))
				if(self.board[r][c] == 'p'):
					self.surface.blit(pygame.transform.scale(PINK_PION,(50,50)),(screenX,screenY))
				elif(self.board[r][c] == 'b'):
					self.surface.blit(pygame.transform.scale(BLUE_PION,(50,50)),(screenX,screenY))

	def getPlayerInput(self,Clicked):
		squareClicked = self.ConvertToChessCoords(Clicked)
		(X,Y) = squareClicked
		print(self.clicked)
		
		if(self.clicked == 0):
			self.comeFrom = squareClicked
			self.clicked = 1
			print(self.board)
		elif(self.clicked == 1 and (self.board[X][Y] is 'p' or self.board[X][Y] is 'b')):
			self.comeFrom = None
			self.clicked = 0
			print(self.board)
		elif(self.clicked == 1 and (self.board[X][Y] is 'e')):
			self.movePion(self.comeFrom,squareClicked)
			self.clicked = 0

	def movePion(self,fromSquare,toSquare):
		(XFrom,YFrom) = fromSquare
		(XTo,YTo) = toSquare

		self.board[XTo][YTo] = self.board[XFrom][YFrom]
		self.board[XFrom][YFrom] = 'e'
		print(self.board)
		self.draw()

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

if __name__ == '__main__':
	pygame.init()
	clock = pygame.time.Clock()
	board = Board()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONUP:
				(mouseX,mouseY) = pygame.mouse.get_pos()
				board.getPlayerInput((mouseX,mouseY))
		pygame.display.update()
		clock.tick(30)

	




