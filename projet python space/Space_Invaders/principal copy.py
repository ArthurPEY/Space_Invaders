from _typeshed import StrPath
from abc import abstractproperty
from tkinter import *

def scoreCounter():
    global score
    score.set('Votre score ' + str(0))

mw = Tk()
mw.title('Space invaders')



mw.geometry("{0}x{1}+0+0".format(mw.winfo_screenwidth(), mw.winfo_screenheight()))


score = StringVar()
scoreCounter()
labelScore = Label (mw, textvariable = score, fg = 'red')

#position du recta,ngle
posyRec = 230
posxRec = 150

#mouvement rectangle
def clavier(event):
    global posxRec, posyRec
    touche = event.keysym
    print(touche)
    if touche =='d':
        posxRec +=20
    if touche =='q':
        posxRec -=20
    if touche == 'm':
        tir()
    canevas.coords(canvas_rect, posxRec - 10, posyRec -10,posxRec +10, posyRec +10)

class tirRect:
    def __init__(self,posxRec, posyRec):
        self.x0 = posxRec - 10
        self.y0 = posyRec -10
        self.x1 = posxRec + 10
        self.y1 = posyRec +10
        self.rectangle = canevas.create_rectangle( posxRec - 10, posyRec -10,posxRec +10, posyRec +10) 
    
    def tir():
        global Arret
        x0 = posxRec
        y0 = posyRec
        x1 = posxRec
        y1 = posyRec
        tirRec = canevas.create_rectangle(x0, y0,x1, y1, fill = 'blue')
        if Arret == False:
            movement()
    def Arreter():
        global Arret
        Arret = True
    def Demarrer():
        global Arret
        canevas.delete('all')
        if Arret == True:
            Arret = False
            tir()
def movement(self):
        canevas.move(self.tirRec, self.x, self.y)
        canevas.after(100,self.movement)
        x0, y0, x1, y1 = canevas.coords(self.tirRec)
        

buttonLaunch = Button (mw, text = "Lancer la partie", fg = 'blue')

buttonQuit = Button (mw, text = 'Quitter la partie', fg = 'red', command = mw.destroy)

largeur = 700
hauteur = 700
canevas = Canvas(mw , width = largeur, height = hauteur)

photo = PhotoImage(file = "photo.gif") 
item =canevas.create_image(20, 20, anchor = NW, image = photo)
canvas_rect = canevas.create_rectangle(posxRec-10, posyRec-10, posxRec+10, posyRec+10, fill = "red")
canevas.focus_set()
canevas.bind('<Key>',clavier)



canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
labelScore.grid(row = 1, column = 2,sticky = 'ns' )
buttonLaunch.grid(row = 4, column = 2, sticky = 'ns')
buttonLaunch.grid(row = 2, column = 2, sticky = 'ns')
buttonQuit.grid(row = 3, column = 2, sticky = 'ns')


mw.mainloop()

