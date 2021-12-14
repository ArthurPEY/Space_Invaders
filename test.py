# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:48:01 2021

@author: Arthur
"""
import time
from tkinter import *
from tkinter.ttk import * 
  
class testobj:
    def __init(self):
        self.x=x

class alien: 
    def __init__(self,start,limitG,limitD): 
        self.start = start
        self.x = 10
        self.y = 0
        self.rectangle = canevas.create_rectangle( start, 5, start+25, 25, fill = "black") 
        self.limitD = limitD
        self.limitG = limitG
        

        
    def movement(self):
        canevas.move(self.rectangle, self.x, self.y)  
        canevas.after(100,self.movement)
        x0, y0, x1, y1 = canevas.coords(self.rectangle)
        if x1>self.limitD:
            self.x=-10
        if x0<self.limitG:
            self.x=10
    
    def __del__(self):
        print ("deleted")
        

class vaisseau:
    def __init__(self,start): 
        self.x = 0
        self.y = 0
        self.vaisseau = canevas.create_rectangle( start, 370, start+45, 390, fill = "red")


    def left(self, event):
        x0, y0, x1, y1 = canevas.coords(self.vaisseau)
        if x0 > 5:
            self.x = -5
            self.y = 0
            canevas.move(self.vaisseau, self.x, self.y)
         
    def right(self, event):
        x0, y0, x1, y1 = canevas.coords(self.vaisseau)
        if x1<595:
            self.x = 5
            self.y = 0
            canevas.move(self.vaisseau, self.x, self.y)
            
class balle:   
    def __init__(self):
        x0, y0, x1, y1 = canevas.coords(vaisseau.vaisseau)
        self.x = x0
        self.y = y0
        self.rectangle = canevas.create_rectangle( x0, y0, x1, y1, fill = "black")
        
    def tir(self,event):
        x0, y0, x1, y1 = canevas.coords(self.rectangle)
        canevas.move(self.rectangle, self.x, self.y)  
        canevas.after(100,self.tir(event))
        
        self.y=-1
        
def fcttir(event):
    ballez=balle()
    ballez.tir(event)    
     

def kill():
    global alienz
    global alienzmov
    idobj=alienz.rectangle
    canevas.delete("{}".format(idobj))
    return()
  
largeur = 600
hauteur = 400
dif=8
    
    
mw = Tk() 

canevas=Canvas(mw, width=600, height=400, bg="ivory")
canevas.pack(padx=50, pady=50)
ennemis=[]
# for k in range(0,dif):
#     alienz=alien((dif-k)*50,(dif-k)*50,largeur-k*50).movement()
    
#     ennemis.append(alienz)
    
alienz=alien(50,50,500)
alienzmov=alienz.movement()




button=Button(mw, command=kill)
button.pack()

# alien1 = alien(0,0,450).movement()
# alien2 = alien(50,50,500).movement()
# alien3 = alien(100,100,550).movement()
# alien4 = alien(150,150,600).movement()


vaisseau = vaisseau(300)

mw.bind("<KeyPress-Left>", lambda e: vaisseau.left(e))
mw.bind("<KeyPress-Right>", lambda e: vaisseau.right(e))
mw.bind("<KeyPress-Up>", fcttir)


print(canevas.coords(vaisseau.vaisseau))

mainloop()


