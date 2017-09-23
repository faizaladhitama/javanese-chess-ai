from tkinter import *
from PIL import Image,ImageTk
import os

class GUI : 
	def __init__(self, master):
		self.frame = Canvas(master, bg = "#7BC5DA", width = master.winfo_screenwidth(), height = master.winfo_screenheight())
		self.master = master

	def initiateItems(self):
		theBoard = Board(self.frame)
		theLine = Line(self.frame)
		theBoard.create_board()
		theNode = Node(self.frame)
		PinkPion = Pion(self.frame,"pink")
		BluePion = Pion(self.frame,"blue")

		edge1 = theLine.create_line(390,70,670,350) #\ atas ke tengah
		edge2 = theLine.create_line(670,350,950,630) #\ tengah ke bawah

		edge3 = theLine.create_line(670,70,670,350) #| atas ke tengah
		edge4 = theLine.create_line(670,350,670,630) #| tengah ke bawah

		edge5 = theLine.create_line(950,70,670,350) #/ atas ke tengah
		edge6 = theLine.create_line(670,350,390,630) #/ tengah ke bawah

		edge7 = theLine.create_line(390,350,670,350) # - kiri ke tengah
		edge8 = theLine.create_line(670,350,950,350) #- tengah ke kanan

		node1 = theNode.create_node(375,55,405,85) #node kiri atas
		node2 = theNode.create_node(655,55,685,85) #node tengah atas
		node3 = theNode.create_node(935,55,965,85) #node kanan atas

		node4 = theNode.create_node(375,335,405,365) #node kiri tengah 
		node5 = theNode.create_node(655,335,685,365) #node tengah tengah
		node6 = theNode.create_node(935,335,965,365) #node kanan tengah 

		node7 = theNode.create_node(375,615,405,645) #node kiri bawah 
		node8 = theNode.create_node(655,615,685,645) #node tengah bawah
		node9 = theNode.create_node(935,615,965,645) #node kanan bawah

		pinkPion1 = PinkPion.create_pion(370,50,410,90)
		pinkPion2 = PinkPion.create_pion(650,50,690,90)
		pinkPion3 = PinkPion.create_pion(930,50,970,90)

		bluePion1 = BluePion.create_pion(370,610,410,650)
		bluePion2 = BluePion.create_pion(650,610,690,650)
		bluePion3 = BluePion.create_pion(930,610,970,650)

	def packed(self):
		self.master.minsize(width=self.master.winfo_screenwidth(), height=self.master.winfo_screenheight())
		self.master.maxsize(width=self.master.winfo_screenwidth(), height=self.master.winfo_screenheight())
		self.initiateItems()
		self.frame.pack()

class Board : 
	def __init__(self,frame):
		self.frame = frame

	def create_board(self):
		self.frame.create_rectangle(350, 30, 990, 670, fill="#BA927F", width = 20, outline = "#392316")
		self.frame.create_rectangle(390, 70, 950, 630, fill="#BA927F", width = 10, outline = "#392316")

class Line : 
	def __init__(self,frame):
		self.frame = frame
	def create_line(self,x0,y0,x1,y1):
		self.frame.create_line(x0, y0, x1, y1, width = 10, fill = "#392316")

class Node : 
	def __init__(self,frame):
		self.frame = frame
	def create_node(self,x0,y0,x1,y1):
		self.frame.create_oval(x0, y0, x1, y1, fill = "#FBE9AD", outline = "#FBE9AD")

class Pion :
	def __init__(self,frame,color):
		self.frame = frame
		self.color = color

	def create_pion(self, x0, y0, x1, y1):
		if(self.color == "blue"):
			self.frame.create_oval(x0, y0, x1, y1, fill = "#8799CB", outline = "#4E586C", width = 5)
		elif(self.color == "pink"):
			self.frame.create_oval(x0, y0, x1, y1, fill = "#E3ADC5", outline = "#66525B", width = 5)

if __name__ == '__main__':
	root = Tk()
	theGUI = GUI(root)
	theGUI.packed()

	root.title("Catur Jawa")
	root.wm_state('zoomed')
	root.mainloop()
	