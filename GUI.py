from tkinter import *
from PIL import Image,ImageTk
import os

class GUI : 
	def __init__(self, master):
		self.frame = Canvas(master, bg = "#7BC5DA", width = master.winfo_screenwidth(), height = master.winfo_screenheight())
		self.master = master

	"""
	Menginisiasikan Items2 pada GUI
	"""
	def initiateItems(self):
		
		theBoard = Board(self.frame)

		theLine = Line(self.frame)

		#Bikin Boardnya
		theBoard.create_board()

		theNode = Node(self.frame)
		PinkPion = Pion(self.frame,"pink")
		BluePion = Pion(self.frame,"blue")

		#bikin Edgenya
		edge1 = theLine.create_line(390,70,670,350) #\ atas ke tengah
		edge2 = theLine.create_line(670,350,950,630) #\ tengah ke bawah

		edge3 = theLine.create_line(670,70,670,350) #| atas ke tengah
		edge4 = theLine.create_line(670,350,670,630) #| tengah ke bawah

		edge5 = theLine.create_line(950,70,670,350) #/ atas ke tengah
		edge6 = theLine.create_line(670,350,390,630) #/ tengah ke bawah

		edge7 = theLine.create_line(390,350,670,350) # - kiri ke tengah
		edge8 = theLine.create_line(670,350,950,350) #- tengah ke kanan

		#Bikin Node (yang lingkaran kuning kecil)
		node1 = theNode.create_node(375,55,405,85) #node kiri atas
		node2 = theNode.create_node(655,55,685,85) #node tengah atas
		node3 = theNode.create_node(935,55,965,85) #node kanan atas

		node4 = theNode.create_node(375,335,405,365) #node kiri tengah 
		node5 = theNode.create_node(655,335,685,365) #node tengah tengah
		node6 = theNode.create_node(935,335,965,365) #node kanan tengah 

		node7 = theNode.create_node(375,615,405,645) #node kiri bawah 
		node8 = theNode.create_node(655,615,685,645) #node tengah bawah
		node9 = theNode.create_node(935,615,965,645) #node kanan bawah

		#bikin pion2nya
		pinkPion1 = PinkPion.create_pion(370,50,410,90)
		pinkPion2 = PinkPion.create_pion(650,50,690,90)
		pinkPion3 = PinkPion.create_pion(930,50,970,90)

		bluePion1 = BluePion.create_pion(370,610,410,650)
		bluePion2 = BluePion.create_pion(650,610,690,650)
		bluePion3 = BluePion.create_pion(930,610,970,650)

	#buat ngepack frame
	def packed(self):
		self.master.minsize(width=self.master.winfo_screenwidth(), height=self.master.winfo_screenheight())
		self.master.maxsize(width=self.master.winfo_screenwidth(), height=self.master.winfo_screenheight())
		self.initiateItems()
		self.frame.pack()

#class board
class Board : 
	def __init__(self,frame):
		self.frame = frame

	def create_board(self):
		self.frame.create_rectangle(350, 30, 990, 670, fill="#BA927F", width = 20, outline = "#392316")
		self.frame.create_rectangle(390, 70, 950, 630, fill="#BA927F", width = 10, outline = "#392316")

#class edge
class Line : 
	def __init__(self,frame):
		self.frame = frame
	def create_line(self,x0,y0,x1,y1):
		self.frame.create_line(x0, y0, x1, y1, width = 10, fill = "#392316")

#class Node
class Node : 
	def __init__(self,frame):
		self.frame = frame
	def create_node(self,x0,y0,x1,y1):
		self.frame.create_oval(x0, y0, x1, y1, fill = "#FBE9AD", outline = "#FBE9AD")

#class pion
class Pion :
	def __init__(self,frame,color):
		self.frame = frame
		self.color = color
		self.x0 = 0
		self.y0 = 0
		self.x1 = 0
		self.y1 = 0

	def pionOnClick(event):
		print("terklik")

	def create_pion(self, x0, y0, x1, y1):
		self.set_initialPlace(x0, y0, x1, y1)
		#kondisi warna kalo biru warna pionnya biru
		if(self.color == "blue"):
			self.frame.create_oval(x0, y0, x1, y1, fill = "#8799CB", outline = "#4E586C", width = 5).bind(pionOnClick)
		elif(self.color == "pink"):
			self.frame.create_oval(x0, y0, x1, y1, fill = "#E3ADC5", outline = "#66525B", width = 5).bind(pionOnClick)

	#buat ganti posisi awal (defaultnya kan 0)
	def set_initialPlace(self, x0, y0, x1, y1):
		self.x0 = x0
		self.y0 = y0
		self.x1 = x1
		self.y1 = y1

	#jalan keatas
	def move_Up(self):
		up_Y0 = self.y0 - 280
		up_Y1 = self.y1 - 280
		if(up_Y0 < 50):
			print("Unable to move")
		else:
			self.y0 = up_Y0
			self.y1 = up_Y1

	#jalan ke bawah
	def move_Down(self):
		down_Y0 = self.y0 + 280
		down_Y1 = self.y1 + 280
		if(down_Y1 > 640):
			print("Unable to move")
		else:
			self.y0 = down_Y0
			self.y1 = down_Y1

	#jalan ke kiri
	def move_Left(self):
		left_X0 = self.x0 - 280
		left_X1 = self.x1 - 280
		if(left_X0 < 370):
			print("Unable to move")
		else:
			self.x0 = left_x0
			self.x1 = left_x1

	#jalan ke kanan
	def move_Right(self):
		right_X0 = self.x0 + 280
		right_X1 = self.x1 + 280
		if(right_X1 > 960):
			print("Unable to move")
		else:
			self.x0 = right_x0
			self.x1 = right_x1

	#jalan diagonal atas kiri
	def move_DiagonalUpLeft(self):
		diagonalUpLeft_X0 = self.x0 - 280
		diagonalUpLeft_X1 = self.x1 - 280
		diagonalUpLeft_Y0 = self.y0 - 280
		diagonalUpLeft_Y1 = self.y1 - 280

		if(diagonalUpLeft_X0 < 370 or diagonalUpLeft_Y0 < 50):
			print("Unable to move")
		else:
			self.x0 = diagonalUpLeft_X0
			self.x1 = diagonalUpLeft_X1
			self.y0 = diagonalUpLeft_Y0
			self.y1 = diagonalUpLeft_Y1

	#jalan diagonal atas kanan
	def move_DiagonalUpRight(self):
		diagonalUpRight_X0 = self.x0 + 280
		diagonalUpRight_X1 = self.x1 + 280
		diagonalUpRight_Y0 = self.y0 - 280
		diagonalUpRight_Y1 = self.y1 - 280

		if(diagonalUpRight_X1 > 960 or diagonalUpRight_Y0 < 50):
			print("Unable to move")
		else:
			self.x0 = diagonalUpRight_X0
			self.x1 = diagonalUpRight_X1
			self.y0 = diagonalUpRight_Y0
			self.y1 = diagonalUpRight_Y1

	#jalan diagonal bawah kiri
	def move_DiagonalDownLeft(self):
		diagonalDownLeft_X0 = self.x0 - 280
		diagonalDownLeft_X1 = self.x1 - 280
		diagonalDownLeft_Y0 = self.y0 + 280
		diagonalDownLeft_Y1 = self.y1 + 280

		if(diagonalDownLeft_X0 < 370 or diagonalDownLeft_Y0 > 640):
			print("Unable to move")
		else:
			self.x0 = diagonalUpLeft_X0
			self.x1 = diagonalUpLeft_X1
			self.y0 = diagonalUpLeft_Y0
			self.y1 = diagonalUpLeft_Y1

	#jalan diagonal bawah kanan
	def move_DiagonalDownRight(self):
		diagonalDownRight_X0 = self.x0 + 280
		diagonalDownRight_X1 = self.x1 + 280
		diagonalDownRight_Y0 = self.y0 + 280
		diagonalDownRight_Y1 = self.y1 + 280

		if(diagonalDownRight_X1 > 960 or diagonalDownRight_Y1 > 640):
			print("Unable to move")
		else:
			self.x0 = diagonalUpRight_X0
			self.x1 = diagonalUpRight_X1
			self.y0 = diagonalUpRight_Y0
			self.y1 = diagonalUpRight_Y1

if __name__ == '__main__':
	root = Tk()
	theGUI = GUI(root)
	theGUI.packed()

	root.title("Catur Jawa")
	root.wm_state('zoomed')
	root.mainloop()
	