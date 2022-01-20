# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:48:01 2021

@author: Arthur
"""
import time
from tkinter import *
from PIL import ImageTk
import random

scoreint=0


class alien: 
    def __init__(self,start,hauteur,limitG,limitD): 
        global imgalien
        self.start = start
        self.x = 10
        self.y = 0
        self.hauteur = hauteur
        self.rectangle = canevas.create_image( start, hauteur,anchor=NW,image=imgalien) 
        self.limitD = limitD
        self.limitG = limitG
        

        
    def movement(self):
        canevas.move(self.rectangle, self.x, self.y)  
        coords = canevas.coords(self.rectangle)
        self.y=0
        if len(coords) == 0:
            return()
        canevas.after(100,self.movement)
        x0, y0 = coords
        if x0 + 25>self.limitD:
            self.x=-10
            self.y=10
        if x0<self.limitG:
            self.x=10
            self.y=10
    
        

class vaisseau:
    def __init__(self,start):
        global imgvais
        self.x = 0
        self.y = 0
        self.vaisseau = canevas.create_image(start,370,anchor=NW,image=imgvais)
        self.vie = 3


    def left(self, event):
        x0, y0 = canevas.coords(self.vaisseau)
        if x0 > 5:
            self.x = -5
            self.y = 0
            canevas.move(self.vaisseau, self.x, self.y)
        
         
    def right(self, event):
        x0, y0= canevas.coords(self.vaisseau)
        if x0 + 45 <595:
            self.x = 5
            self.y = 0
            canevas.move(self.vaisseau, self.x, self.y)
          
filetir=[]
            
class balle:   
    def __init__(self):
        x0, y0 = canevas.coords(vaisseau.vaisseau)
        self.x = x0
        self.y = y0
        self.obu = canevas.create_oval( ((x0+x0+45)/2)-2, y0, ((x0+x0+45)/2)+2, y0+25, fill = "green")
        
    def tir(self):
        breakcond=0
        global scoreint
        global score
        global filetir
        global blocs
        x0, y0, x1, y1 = canevas.coords(self.obu)
        
        for k in range(len(ennemis)):
            x0alien, y0alien = canevas.coords(ennemis[k].rectangle)
            if canevas.find_overlapping(x0alien, y0alien, x0alien+25, y0alien+25) == (1,ennemis[k].rectangle,self.obu):
                a=canevas.find_overlapping(x0alien, y0alien, x0alien+25, y0alien+25)
                canevas.delete(a[1])
                del ennemis[k]
                scoreint = scoreint + 10
                scoreCounter()
                canevas.delete(self.obu)
                filetir.pop(0)
                return(None)
        
        for k in range(len(blocs)):
            for p in range(len(blocs[k])):
                x0bloc, y0bloc, x1bloc, y1bloc = canevas.coords(blocs[k][p].bloc)
                if canevas.find_overlapping(x0bloc, y0bloc, x1bloc, y1bloc) == (1,blocs[k][p].bloc,self.obu):
                    print(canevas.find_overlapping(x0bloc, y0bloc, x1bloc, y1bloc))
                    a=canevas.find_overlapping(x0bloc, y0bloc, x1bloc, y1bloc)
                    canevas.delete(self.obu)
                    filetir.pop(0)
                    canevas.delete(a[1])
                    blocs[k].pop(0)
                    del self.obu
        if y1 < -10:
            filetir.pop(0)
            del self.obu
            canevas.delete(self.obu)
            return() 
        
        
        traj=-10
        canevas.move(self.obu, 0, traj)
        canevas.after(10,self.tir)
        

class base:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.bloc = canevas.create_rectangle( x, y, x+30, y+30, fill = "orange") 


class laseralien:   
    def __init__(self,idalien):
        x0, y0 = canevas.coords(ennemis[idalien].rectangle)
        x0vaisseau, y0vaisseau = canevas.coords(vaisseau.vaisseau)
        self.x = x0
        self.y = y0
        self.laser = canevas.create_oval( ((x0+x0+25)/2)-2, y0+25, ((x0+x0+25)/2)+2, y0+50, fill = "red")
    
    def tir(self):
        breakcond=0
        global blocs
        x0, y0, x1, y1 = canevas.coords(self.laser)
        x0vaisseau, y0vaisseau= canevas.coords(vaisseau.vaisseau)
        if canevas.find_overlapping(x0vaisseau, y0vaisseau, x0vaisseau+45, y0vaisseau+25) == (1,2,self.laser):
            vaisseau.vie=vaisseau.vie-1
            vievaisseau.set(vaisseau.vie)
            vieCounter()
            checkend()
            canevas.delete(self.laser)
            del self.laser
            print("touche")
            return(None)
        elif y1 > 800:
            del self.laser
            return()
        for k in range(len(blocs)):
            for p in range(len(blocs[k])):
                x0bloc, y0bloc, x1bloc, y1bloc = canevas.coords(blocs[k][p].bloc)
                if canevas.find_overlapping(x0bloc, y0bloc, x1bloc, y1bloc) == (1,blocs[k][p].bloc,self.laser):
                    print(canevas.find_overlapping(x0bloc, y0bloc, x1bloc, y1bloc))
                    a=canevas.find_overlapping(x0bloc, y0bloc, x1bloc, y1bloc)
                    canevas.delete(a[1])
                    canevas.delete(self.laser)
                    blocs[k].pop()
                    print(blocs[k])
                    del self.laser
                    
        traj=4
        canevas.move(self.laser, 0, traj)
        canevas.after(10,self.tir)
     
        
numtir=10

# def fcttir(event):
#     global numtir
#     ballez=balle()
#     ballez.tir() 
#     x0alien, y0alien, x1alien, y1alien = canevas.coords(ennemis[1].rectangle)
#     x0, y0, x1, y1 = canevas.coords(ballez.obu)
#     #if canevas.find_overlapping(x0alien, y0alien, x1alien, y1alien) != (2,):
#     if canevas.find_overlapping(x0alien, y0alien, x1alien, y1alien) != (2,):

#         a=canevas.find_overlapping(x0alien, y0alien, x1alien, y1alien)
#         print(a)
#         canevas.delete(a[0])
#     return()

def bridetir(event):
    global filetir
    if len(filetir)<3:
        filetir.append("OBU")
        balle().tir()
        return()

def kill(k,event):
    global alienz
    global alienzmov
    idobj=ennemis[k].rectangle
    canevas.delete("{}".format(idobj))
    return()

def colision():
    global ballez
    x0, y0, x1, y1 = canevas.coords(ballez.obu)
    print(x0, y0, x1, y1)
    return()
  
largeur = 600
hauteur = 400
    
def boucle_tir_alien():
    delay=random.randint(2000,3000)
    canevas.after(delay,boucle_tir_alien)
    idalien=random.randint(0,len(ennemis))
    laser=laseralien(idalien)
    laser.tir()

    for k in range(0,dif):
        canevas.delete(3*dif + 30 + k)
    return()
    
def checkend():
    global gameover
    vie=vievaisseau.get()
    if int(vie)==0:
        canevas=Canvas(mw, width=600, height=400, bg="ivory")
        canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
        canevas.create_image(0,0,anchor=NW,image=gameover)
        
        
def identite():
    """Affichage de l'identité du créateur du programme"""
    messagebox.showinfo("A propos", "programme crée par Arthur PEY et Juan REYES-ORTIZ")
    return()

def scoreCounter():
    global scoreint
    score.set('Votre score :' + str(scoreint))
    
def vieCounter():
    vie = vaisseau.vie
    vievaisseau.set('Vie :' + str(vie))

mw = Tk()
mw.title('Space invaders')
mw.geometry("{0}x{1}+0+0".format(mw.winfo_screenwidth(), mw.winfo_screenheight()))


score = StringVar()
scoreCounter()
labelScore = Label (mw, textvariable = score, fg = 'red')

dif = 5

def hard():
    global dif
    dif=9

def easy():
    global dif
    dif=5
    
canevas=Canvas(mw, width=600, height=400, bg="ivory")
canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
imgvais = PhotoImage(file = 'vaisseau.gif')
imgalien = PhotoImage(file = 'alien.gif')
imgback = PhotoImage(file = 'back.gif')
imgindex = PhotoImage(file = 'index.gif')
gameover = PhotoImage(file = 'over.gif')
canevas.create_image(0,0,anchor=NW,image=imgindex)



def demarrer():
    global vaisseau
    global canevas
    global ennemis
    global dif
    global blocs
    global scoreint
    canevas.delete('all')
    
    canevas=Canvas(mw, width=600, height=400, bg="ivory")
    canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
    canevas.create_image(0,0,anchor=NW,image=imgback)
    vaisseau = vaisseau(300)
    print(canevas.coords(vaisseau.vaisseau))
    vievaisseau.set(3)
    scoreint = 0
    ennemis=[]
    vieCounter()
    
    for n in range (0,3):
        for k in range(0,dif):
            alienz=alien((dif-k)*50,5+(n*40),(dif-k-1)*50,largeur-k*50)
            ennemis.append(alienz)
            alienz.movement()
            
    blocs=[]
    colonne=[]
    for k in range(0,3):
        for p in range(0,3):
            colonne=[]
            for i in range(0,3):
                colonne.append(base(70+(p*31)+k*185,300-(i*31)))
            blocs.append(colonne)
                
        
    for k in range(dif):
        laseralien(k)    

    boucle_tir_alien()


    mw.bind("<KeyPress-Left>", lambda e: vaisseau.left(e))
    mw.bind("<KeyPress-Right>", lambda e: vaisseau.right(e))
    mw.bind("<KeyPress-Up>", lambda e: bridetir(e))
    mw.bind("<KeyPress-Down>", lambda e: boucle_tir_alien())

    return()

buttonLaunch = Button (mw, text = "Lancer la partie", fg = 'blue', command = demarrer)


buttonQuit = Button (mw, text = 'Quitter la partie', fg = 'red', command = mw.destroy)

FrameBot = Frame(mw, borderwidth=2, relief=GROOVE)

largeur = 600
hauteur = 400

vievaisseau = StringVar()

labelVie = Label (mw, textvariable = vievaisseau, fg = 'red')

buttonFacile = Button(FrameBot, text = "Facile", anchor = NW)
buttonFacile.configure(width = 10, height = 2, activebackground = "#33B5E5", relief = FLAT,command = easy)


buttonHard = Button(FrameBot, text = "Difficile", anchor = NW)
buttonHard.configure(width = 10, height = 2, activebackground = "#33B5E5", relief = FLAT, command = hard)


menubar=Menu(mw) # Creation du menu

menuglobal=Menu(menubar,tearoff=0)


menuaide = Menu(menubar,tearoff = 0)
menuaide.add_command(label= "Auteurs",command=identite)

menubar.add_cascade(label="A propos",menu=menuaide)

mw.config(menu=menubar)


labelVie.grid(row=7,column=2)


labelScore.grid(row = 1, column = 2,sticky = 'ns' )

buttonLaunch.grid(row = 2, column = 2, sticky = 'ns')
buttonQuit.grid(row = 3, column = 2, sticky = 'ns')
FrameBot.grid(row = 8,column = 1)
buttonFacile.grid(row = 1, column = 1)
buttonHard.grid(row = 1, column = 2)



mw.mainloop()



