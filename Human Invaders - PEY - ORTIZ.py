# -*- coding: utf-8 -*-
"""
Auteur : Arthur PEY - Juan REYES-ORTIZ
Que fait le programme : Jeu du Space Invaders
Date :  20/01/2022
Todo : Impossible de relancer une partie; Une erreur "TclError: image "pyimage59" doesn't exist" 
peut apparaitre, il faut relancer l'editeur de code/console.
"""
import time
from tkinter import *
from PIL import ImageTk
import random

#score initialisée
scoreint=0

#création de la classe alien
class alien: 
    def __init__(self,start,hauteur,limitG,limitD): 
        global imgalien
        self.start = start
        self.x = 10
        self.y = 0
        self.hauteur = hauteur
        self.rectangle = canevas.create_image( start, hauteur,anchor=NW,image=imgalien) 
        #on met en place les limites de déplacement des aliens
        self.limitD = limitD
        self.limitG = limitG
        

     #fonction qui définit le mouvement de l'alien   
    def movement(self):
        canevas.move(self.rectangle, self.x, self.y)  
        #on récupere les coordonnées
        coords = canevas.coords(self.rectangle)
        self.y=0
        if len(coords) == 0:  #///
            return()
        canevas.after(100,self.movement) #on relance la fonction tous les 0,1 s
        x0, y0 = coords
        if x0 + 25>self.limitD: #si les aliens n'ont pas atteint la limite, ils se deplacent de 10 pixels
            self.x=-10
            self.y=10
        if x0<self.limitG:
            self.x=10
            self.y=10
    
        
#on définit la classe du vaisseau
class vaisseau:
    def __init__(self,start):
        global imgvais
        self.x = 0
        self.y = 0
        self.vaisseau = canevas.create_image(start,370,anchor=NW,image=imgvais)
        self.vie = 3 #points de vie du vaisseau

    #fonction du déplacement vers la gauche
    def left(self, event):
        x0, y0 = canevas.coords(self.vaisseau)
        if x0 > 5: # 5 pixels étant la limite de déplacement vers la gauche
            self.x = -5
            self.y = 0
            canevas.move(self.vaisseau, self.x, self.y)
        
    #fonction du déplacement vers la droite     
    def right(self, event):
        x0, y0= canevas.coords(self.vaisseau)
        if x0 + 45 <595:
            self.x = 5
            self.y = 0
            canevas.move(self.vaisseau, self.x, self.y)
          
filetir=[] #création d'une file dont on va rentrer le nombre de tirs présents sur le jeu
  
#création de la balle lancée par le vaisseau
class balle:   
    def __init__(self):
        #on réupere les coordonnées du vaisseau 
        x0, y0 = canevas.coords(vaisseau.vaisseau)
        self.x = x0
        self.y = y0
        self.obu = canevas.create_oval( ((x0+x0+45)/2)-2, y0, ((x0+x0+45)/2)+2, y0+25, fill = "green")
 #fontion qui définit le comportement du tir lancé       
    def tir(self):
        breakcond=0
        global scoreint
        global score
        global filetir
        global blocs
        x0, y0, x1, y1 = canevas.coords(self.obu)
        
        for k in range(len(ennemis)): 
            x0alien, y0alien = canevas.coords(ennemis[k].rectangle) #on récupere les coordonnées du k-ieme alien
            #si les coordonnees de l'obus et de l'alien sont égales
            if canevas.find_overlapping(x0alien, y0alien, x0alien+25, y0alien+25) == (1,ennemis[k].rectangle,self.obu):
                a=canevas.find_overlapping(x0alien, y0alien, x0alien+25, y0alien+25)
                canevas.delete(a[1]) #on efface l'alien touché
                del ennemis[k]
                scoreint = scoreint + 10 #on augmente le score
                scoreCounter()
                canevas.delete(self.obu) #on efface l'obus
                filetir.pop(0) #on "pop" le tir qui a été lancé, de sa liste
                return(None)
        #la boucle for suivante a le meme fonctionnement que la précedente pour les murs de protection
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
                    
        #si le laser est hors de l'écran de jeu 
        if y1 < -10:
            filetir.pop(0) #on efface le laser
            del self.obu
            canevas.delete(self.obu)
            return()
        
        #on vérifie si le joueur a fini la partie
        checkend()
        traj=-10
        canevas.move(self.obu, 0, traj)
        canevas.after(10,self.tir)
        
#création des bases de protection
class base:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.bloc = canevas.create_rectangle( x, y, x+30, y+30, fill = "orange") 

#classe qui définit le laser des aliens
class laseralien:   
    def __init__(self,idalien):
        x0, y0 = canevas.coords(ennemis[idalien].rectangle) #on récupere les coordonnées des aliens
        x0vaisseau, y0vaisseau = canevas.coords(vaisseau.vaisseau) #on récupère les coordonnées du vaisseau
        self.x = x0
        self.y = y0
        self.laser = canevas.create_oval( ((x0+x0+25)/2)-2, y0+25, ((x0+x0+25)/2)+2, y0+50, fill = "red")
    
    #comportement du laser des aliens
    def tir(self):
        breakcond=0
        global blocs
        #coordonnées du laser
        x0, y0, x1, y1 = canevas.coords(self.laser)
        x0vaisseau, y0vaisseau= canevas.coords(vaisseau.vaisseau)
        #si le laser alien se superpose au vaisseau
        if canevas.find_overlapping(x0vaisseau, y0vaisseau, x0vaisseau+45, y0vaisseau+25) == (1,2,self.laser):
            vaisseau.vie=vaisseau.vie-1 #on enleve une vie 
            vievaisseau.set(vaisseau.vie)
             #on relance la fontion vieCounter pour sauvegarder le nombre de vies dans le jeu
            vieCounter()
            #on vérifie que le joueur si n'a plus de vies
            checkend() 
            canevas.delete(self.laser) #on efface le laser
            del self.laser
            print("touche") #////
            return(None)
        elif y1 > 800: #si le laser est hors de l'écran on l'efface
            del self.laser 
            return()
        
        #cette boucle for , sert a déterminer si le laser alien touche un mur de protection
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
     
        
numtir=10 #initialisation du nombre de tirs 

#cette fontion sert a ajouter du "delay" chaque 3 tir pour eviter le tir répétitif
def bridetir(event):
    global filetir
    #on utilise la file définie précedenment
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
 
#hauteur du canvas
largeur = 600
hauteur = 400
 
#cette fontion définit aléatoirement à quel instant un des aliens tire entre 2s et 3s, 
#puis on sélectionne aléatoirement l'alien en question
def boucle_tir_alien():
    delay=random.randint(2000,3000)
    canevas.after(delay,boucle_tir_alien)
    idalien=random.randint(0,len(ennemis))
    laser=laseralien(idalien)
    laser.tir()

    #///
    for k in range(0,dif):
        canevas.delete(3*dif + 30 + k)
    return()

#fontion de fin de partie    
def checkend():
    global gameover
    global ennemis
    global win
    #on récupère les points de vie du joueur
    vie=vaisseau.vie
    if int(vie)==0: #si le joueur n'a plus de vies
        canevas=Canvas(mw, width=600, height=400, bg="ivory")
        canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
        canevas.create_image(0,0,anchor=NW,image=gameover)
    elif len(ennemis) == 0: #s'il n'y a plus d'ennemis
        canevas=Canvas(mw, width=600, height=400, bg="ivory")
        canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
        canevas.create_image(0,0,anchor=NW,image=win)
        
        
def identite():
    """Affichage de l'identité du créateur du programme"""
    messagebox.showinfo("A propos", "programme crée par Arthur PEY et Juan REYES-ORTIZ")
    return()
#compteur de score
def scoreCounter():
    global scoreint
    score.set('Votre score :' + str(scoreint))
    
#conteur de points de vies    
def vieCounter():
    vie = vaisseau.vie
    vievaisseau.set('Vie :' + str(vie))

#création de la fenetre tkinter
mw = Tk()
mw.title('Space invaders')
mw.geometry("{0}x{1}+0+0".format(mw.winfo_screenwidth(), mw.winfo_screenheight()))

#affichage du label du score
score = StringVar()
scoreCounter()
labelScore = Label (mw, textvariable = score, fg = 'red')

#difficultée predeterminée
dif = 5

#difficulté "hard"
def hard():
    global dif
    dif=9
#difficultée "easy"
def easy():
    global dif
    dif=5
#création du canvas du menu du jeu   
canevas=Canvas(mw, width=600, height=400, bg="ivory")
canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
#chargment des images
imgvais = PhotoImage(file = 'vaisseau.gif')
imgalien = PhotoImage(file = 'alien.gif')
imgback = PhotoImage(file = 'back.gif')
imgindex = PhotoImage(file = 'index.gif')
win = PhotoImage(file = 'win.gif')
gameover = PhotoImage(file = 'over.gif')
canevas.create_image(0,0,anchor=NW,image=imgindex)


#fonction qui sert à démarrer le jeu
def demarrer():
    global vaisseau
    global canevas
    global ennemis
    global dif
    global blocs
    global scoreint
    canevas.delete('all')
    
    #création de la zone de jeu
    canevas=Canvas(mw, width=600, height=400, bg="ivory")
    canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
    canevas.create_image(0,0,anchor=NW,image=imgback)
    vaisseau = vaisseau(300)
    print(canevas.coords(vaisseau.vaisseau))
    vievaisseau.set(3)
    scoreint = 0
    ennemis=[]
    vieCounter()
    
    #boucle for qui sert à la création des aliens selon la difficultée choissi
    for n in range (0,3):
        for k in range(0,dif):
            alienz=alien((dif-k)*50,5+(n*40),(dif-k-1)*50,largeur-k*50)
            ennemis.append(alienz)
            alienz.movement()
            
    #creation des listes vides pour la mise en place des mur de protection        
    blocs=[]
    colonne=[]
    for k in range(0,3):
        for p in range(0,3):
            colonne=[]
            for i in range(0,3):
                colonne.append(base(70+(p*31)+k*185,300-(i*31)))
            blocs.append(colonne)
                
    #///   
    for k in range(dif):
        laseralien(k)    
        
    #on relance la boucle des tirs alien
    boucle_tir_alien()

    #ici on code la détection des touches du clavier
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



