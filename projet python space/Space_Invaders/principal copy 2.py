# imports every file form tkinter and tkinter.ttk
from tkinter import *
from tkinter.ttk import *

global x
x=0
class GFG:
	def __init__(self, master = None):
		self.master = master
		
		# to take care movement in x direction
		
		# to take care movement in y direction
		self.y = 0
		
		# canvas object to create shape
		self.canvas = Canvas(master)
		# creating rectangle
		self.rectangle = self.canvas.create_rectangle(
						75, 105, 75, 105, fill = "black")
        
		self.canvas.pack()

		# calling class's movement method to
		# move the rectangle
		self.movement()
	

  
	def movement(self):

		# This is where the move() method is called
		# This moves the rectangle to x, y coordinates
		self.canvas.move(self.rectangle,x, self.y)

		self.canvas.after(100, self.movement)
	
	
	# for motion in positive y direction
	def up(self, event):
		print(event.keysym)
		x = 0
		self.y = -5

		touche = event.keysym
		print(touche)
		if touche =='q':
			x -=1
		if touche =='d':
			x +=1

if __name__ == "__main__":

	# object of class Tk, responsible for creating
	# a tkinter toplevel window
	master = Tk()
	gfg = GFG(master)

	# This will bind arrow keys to the tkinter
	# toplevel which will navigate the image or drawing
	master.bind("d", lambda e: gfg.clavier(e))
	master.bind("q", lambda e: gfg.clavier(e))
	master.bind("<KeyPress-Up>", lambda e: gfg.up(e))

	
	# Infinite loop breaks only by interrupt
	mainloop()
