from random import randint
import time
from tkinter import *
from tkinter.ttk import * 

run=True

class alien:
    def __init__(self, mw = None):
        self.mw = mw
          
        
        self.x = 1
        
        self.y = 0
  
        
        self.canvas = Canvas(mw) 
        
        self.rectangle = self.canvas.create_rectangle( 
                         5, 5, 25, 25, fill = "black") 
        self.canvas.pack() 
  
        
        
        self.deplace()

    def deplace(self): 
  
        
        
        self.canvas.move(self.rectangle, self.x, self.y) 
  
        self.canvas.after(100, self.deplace) 



mw=Tk()
canevas=Canvas(mw, width=600, height=400, bg="ivory")
canevas.pack(padx=50, pady=50)
test=alien()
alien.deplace(mw)
mw.mainloop()
