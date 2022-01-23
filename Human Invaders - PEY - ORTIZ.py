# -*- coding: utf-8 -*-
"""
Auteurs : Arthur PEY - Juan REYES-ORTIZ
Que fait le programme : Jeu du Space Invaders
Date :  23/01/2022 (Rendu)
Todo : - Impossible de relancer une partie;
 - Une erreur "TclError: image "pyimage59" doesn't exist" peut apparaître, il faut relancer l'éditeur de code/console; 
 - Il faut parfois appuyer une dernière fois sur "flêche du haut" pour gagner la partie lorsqu'il n'y a plus d'ennemis;
 - Ennemis Bonus;
 - Des erreus de récupération de coordonnées apparaissent mais ne posent pas de problème;
"""

from tkinter import *
from random import randint

#score initialisé
scoreint=0

#création de la classe alien
class alien: 
    def __init__(self,start,hauteur,limitG,limitD): 
        """initiliasiation de l'objet alien"""
        global imgalien
        self.start = start
        self.x = 10 #vitesse latérale initiale
        self.y = 0  #vitesse horizontale initiale
        self.hauteur = hauteur
        self.rectangle = canevas.create_image( start, hauteur,anchor=NW,image=imgalien)  # sprite des aliens
        #on met en place les limites de déplacement des aliens
        self.limitD = limitD
        self.limitG = limitG
        


    def movement(self):
        """Définit les mouvements des aliens"""
        canevas.move(self.rectangle, self.x, self.y)  
        #on récupère les coordonnées
        coords = canevas.coords(self.rectangle)
        self.y=0
        if len(coords) == 0: #stop la boucle si l'alien est suprrimé
            return()
        canevas.after(100,self.movement) #on relance la fonction tous les 0,1s
        x0, y0 = coords
        if x0 + 25>self.limitD: #si les aliens atteignent la limite, ils changent de direction et descendent
            self.x=-10
            self.y=10
        if x0<self.limitG: #si les aliens atteignent la limite, ils changent de direction
            self.x=10
            self.y=10
    
        
class vaisseau:
    def __init__(self,start):
        """Initialisation de l'objet vaisseau"""
        global imgvais
        self.x = 0
        self.y = 0
        self.vaisseau = canevas.create_image(start,370,anchor=NW,image=imgvais)
        self.vie = 3 #points de vie du vaisseau

    #fonction du déplacement vers la gauche
    def left(self, event):
        """Déplacement du vaisseau vers la gauche aprés appuie sur la flêche gauche du clavier"""
        x0, y0 = canevas.coords(self.vaisseau)
        if x0 > 5: # 5 pixels étant la limite de déplacement vers la gauche (mur virtuel)
            self.x = -5 # vitesse laterale du vaisseau
            self.y = 0
            canevas.move(self.vaisseau, self.x, self.y) # déplacement du vaisseau
        
    #fonction du déplacement vers la droite     
    def right(self, event):
        """Déplacement du vaisseau vers la droite aprés appuie sur la flêche droite du clavier"""
        x0, y0= canevas.coords(self.vaisseau)
        if x0 + 45 <595:    # 595 pixels étant la limite de déplacement vers la droite (mur virtuel)
            self.x = 5  # vitesse laterale du vaisseau
            self.y = 0
            canevas.move(self.vaisseau, self.x, self.y)
          
filetir=[] #création d'une FILE dont on va rentrer le nombre de tirs présents sur le jeu
  
#création de la balle lancée par le vaisseau
class balle:   
    def __init__(self):
        """Initialisation de l'objet balle (obu du vaisseau)"""
        x0, y0 = canevas.coords(vaisseau.vaisseau)  #on réupère les coordonnées du vaisseau 
        self.x = x0
        self.y = y0
        self.obu = canevas.create_oval( ((x0+x0+45)/2)-2, y0, ((x0+x0+45)/2)+2, y0+25, fill = "green")  #sprite de l'obu
     
    def tir(self):
        """Définit le comportement du tir lancé"""
        global scoreint
        global score
        global filetir
        global blocs
        x0, y0, x1, y1 = canevas.coords(self.obu) #récupération des coordonnées de la balle
        for k in range(len(ennemis)):  #boucle pour colision sur tous les ennemis
            x0alien, y0alien = canevas.coords(ennemis[k].rectangle) #on récupere les coordonnées du k-ieme alien
            if canevas.find_overlapping(x0alien, y0alien, x0alien+25, y0alien+25) == (1,ennemis[k].rectangle,self.obu): #si les coordonnees de l'obus et de l'alien sont égales
                a=canevas.find_overlapping(x0alien, y0alien, x0alien+25, y0alien+25)
                canevas.delete(a[1]) #on efface l'alien touché (sur canvas)
                del ennemis[k] #on supprime l'alien touché (de la LISTE des ennemis)
                scoreint = scoreint + 10 #on augmente le score
                scoreCounter() #actualisation graphique du score
                canevas.delete(self.obu) #on efface l'obus (sur canvas)
                filetir.pop(0) #on "pop" le tir qui a été lancé de sa PILE
                return(None)
        #la boucle for suivante à le même fonctionnement que la précedente pour les murs de protection
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
                    
        
        if y1 < -10:  #si le laser est hors de l'écran de jeu 
            filetir.pop(0) #on retire le laser de la PILE
            canevas.delete(self.obu) #efface l'obu du canvas
            del self.obu #suppresion de l'objet
            return()
        
        #on vérifie si le joueur a fini la partie
        checkend()
        traj=-10
        canevas.move(self.obu, 0, traj) #Déplcaement de l'obu
        canevas.after(10,self.tir) #On boucle la fonction
        
#création des bases de protection
class base:
    def __init__(self,x,y):
        """Initialisation de l'objet base"""
        self.x = x #postion x de l'objet
        self.y = y #postion y de l'objet
        self.bloc = canevas.create_rectangle( x, y, x+30, y+30, fill = "orange") #affichage du bloc sur le canvas


class laseralien:   
    def __init__(self,idalien):
        """Initialisation du laser des aliens"""
        x0, y0 = canevas.coords(ennemis[idalien].rectangle) #récupère les coordonnées des aliens
        x0vaisseau, y0vaisseau = canevas.coords(vaisseau.vaisseau) #récupère les coordonnées du vaisseau
        self.x = x0
        self.y = y0
        self.laser = canevas.create_oval( ((x0+x0+25)/2)-2, y0+25, ((x0+x0+25)/2)+2, y0+50, fill = "red") #affichage du laser sur le canvas
    
    #comportement du laser des aliens
    def tir(self):
        """Définit le comportement du laser des aliens"""
        global blocs
        x0, y0, x1, y1 = canevas.coords(self.laser)  #coordonnées du laser
        x0vaisseau, y0vaisseau= canevas.coords(vaisseau.vaisseau)
        if canevas.find_overlapping(x0vaisseau, y0vaisseau, x0vaisseau+45, y0vaisseau+25) == (1,2,self.laser):  #si le laser alien se superpose au vaisseau
            vaisseau.vie=vaisseau.vie-1 #enlève une vie 
            vievaisseau.set(vaisseau.vie)   #relance la fontion vieCounter pour actualiser le nombre de vies de l'objet
            vieCounter() #actualisation de l'affichage des vies
            checkend() #vérifie que le joueur n'a plus de vies
            canevas.delete(self.laser) #efface le laser (du canvas)
            del self.laser #suppression de l'objet
            return(None)
        elif y1 > 800: #si le laser est hors de l'écran on l'efface
            canevas.delete(self.laser) #efface le laser (du canvas)
            del self.laser #suppression de l'objet laser
            return()
        
        #cette boucle for sert à déterminer si le laser alien touche un mur de protection (même foncionnement que pour le vaisseau)
        for k in range(len(blocs)):
            for p in range(len(blocs[k])):
                x0bloc, y0bloc, x1bloc, y1bloc = canevas.coords(blocs[k][p].bloc)
                if canevas.find_overlapping(x0bloc, y0bloc, x1bloc, y1bloc) == (1,blocs[k][p].bloc,self.laser):
                    print(canevas.find_overlapping(x0bloc, y0bloc, x1bloc, y1bloc))
                    a=canevas.find_overlapping(x0bloc, y0bloc, x1bloc, y1bloc)
                    canevas.delete(a[1])
                    canevas.delete(self.laser)
                    blocs[k].pop() #Utilisation de la PILE (colonnes de bloc comme PILE d'objet)
                    print(blocs[k])
                    del self.laser
                    
        traj=4
        canevas.move(self.laser, 0, traj)
        canevas.after(10,self.tir)
     
        
numtir=10 #initialisation du nombre de tirs 

#cette fontion sert a ajouter du "delay", il ne peut y avoir que 3 tirs sur le canvas
def bridetir(event):
    """bloque le nombres maximal de tir à l'écran (3 tirs)"""
    global filetir #on utilise la FILE définie précedenment
    if len(filetir)<3:
        filetir.append("OBU") #ajout l'obu à la FILE
        balle().tir() #tir l'obu
        return()
 

largeur = 600 #largeur du canvas
hauteur = 400 #hauteur du canvas
 

#puis on sélectionne aléatoirement l'alien en question
def boucle_tir_alien():
    """définit aléatoirement à quel instant un des aliens tire entre 2s et 3s"""
    delay=randint(2000,3000) #délai de 2 à 3s
    canevas.after(delay,boucle_tir_alien) #relance la fonction de délai de tir
    idalien=randint(0,len(ennemis)) #choisi un alien aléatoirement
    laser=laseralien(idalien) #crée l'objet laser alien sur l'alien sélectionné
    laser.tir() #lance le laser de l'alien

    #Cette boucle permet de supprimer des tirs parasites
    #qui apparaissent au lancement du programme
    for k in range(0,dif):
        canevas.delete(3*dif + 30 + k) #supprimer les tirs parasites
    return()

def checkend():
    """Vérifie si la partie est finie"""
    global gameover
    global ennemis
    global win
    vie=vaisseau.vie #on récupère les points de vie du joueur
    if int(vie)==0: #si le joueur n'a plus de vies
        canevas=Canvas(mw, width=600, height=400, bg="ivory")
        canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
        canevas.create_image(0,0,anchor=NW,image=gameover) #affichage de l'écran de défaite
    elif len(ennemis) == 0: #s'il n'y a plus d'ennemis
        canevas=Canvas(mw, width=600, height=400, bg="ivory")
        canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
        canevas.create_image(0,0,anchor=NW,image=win) #affichage de l'écran de victoire
        
        
def identite():
    """Affichage de l'identité des créateurs du programme"""
    messagebox.showinfo("A propos", "programme créé par Arthur PEY et Juan REYES-ORTIZ")
    return()

def scoreCounter():
    """Affiche le score sur le canvas"""
    global scoreint
    score.set('Votre score :' + str(scoreint)) #actualisation du score
    
    
def vieCounter():
    """Affiche la vie sur le canvas"""
    vie = vaisseau.vie
    vievaisseau.set('Vie :' + str(vie)) #actualisation de la vie


mw = Tk() #création de la fenetre tkinter
mw.title('Space invaders') #titre de la fenêtre
mw.geometry("{0}x{1}+0+0".format(mw.winfo_screenwidth(), mw.winfo_screenheight()))

#affichage du label du score
score = StringVar()
scoreCounter()
labelScore = Label (mw, textvariable = score, fg = 'red')

#difficulté prédeterminée (si le joueur n'en choisi pas, le mode facile est activé)
dif = 5

#difficulté "hard"
def hard():
    global dif
    dif=9
#difficulté "easy"
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



def demarrer():
    """Initialise les variables nécessaires au fonctionnement du jeu et démarre la partie"""
    global vaisseau
    global canevas
    global ennemis
    global dif
    global blocs
    global scoreint
    canevas.delete('all') # Canvas vide
    
    #création de la zone de jeu
    canevas=Canvas(mw, width=600, height=400, bg="ivory")
    canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
    canevas.create_image(0,0,anchor=NW,image=imgback)
    vaisseau = vaisseau(300) #création du vaisseau
    vievaisseau.set(3) #initialisation des vies du vaisseau
    scoreint = 0 #initialisation du score
    ennemis=[] # LISTE des ennemis
    vieCounter() #affichage initial des vies
    
    #boucle for qui sert à la création des aliens selon la difficulté choisie
    for n in range (0,3):
        for k in range(0,dif):
            alientemp=alien((dif-k)*50,5+(n*40),(dif-k-1)*50,largeur-k*50)
            ennemis.append(alientemp)
            alientemp.movement()
            
    #création des LISTES vides pour la mise en place des murs de protection        
    blocs=[]
    colonne=[]
    for k in range(0,3):
        for p in range(0,3):
            colonne=[] # PILE de blocs
            for i in range(0,3):
                colonne.append(base(70+(p*31)+k*185,300-(i*31)))
            blocs.append(colonne)
                
    boucle_tir_alien() #on lance la boucle des tirs alien

    #Détection des touches du clavier et lancement des fonctions en conséquence
    mw.bind("<KeyPress-Left>", lambda e: vaisseau.left(e))
    mw.bind("<KeyPress-Right>", lambda e: vaisseau.right(e))
    mw.bind("<KeyPress-Up>", lambda e: bridetir(e))
    mw.bind("<KeyPress-Down>", lambda e: boucle_tir_alien())

    return()

buttonLaunch = Button (mw, text = "Lancer la partie", fg = 'blue', command = demarrer) #bouton 'demarrer' sur canvas

buttonQuit = Button (mw, text = 'Quitter la partie', fg = 'red', command = mw.destroy)  #bouton 'quitter' sur canvas

vievaisseau = StringVar() #variable de vie

labelVie = Label (mw, textvariable = vievaisseau, fg = 'red') #affichage de la vie

FrameBot = Frame(mw, borderwidth=2, relief=GROOVE) #frame des bouton de difficulter

buttonFacile = Button(FrameBot, text = "Facile", anchor = NW) #bouton 'facile'
buttonFacile.configure(width = 10, height = 2, activebackground = "#33B5E5", relief = FLAT,command = easy)


buttonHard = Button(FrameBot, text = "Difficile", anchor = NW) #bouton 'difficile'
buttonHard.configure(width = 10, height = 2, activebackground = "#33B5E5", relief = FLAT, command = hard)


menubar=Menu(mw) # Creation du menu

menuglobal=Menu(menubar,tearoff=0)
menuaide = Menu(menubar,tearoff = 0)
menuaide.add_command(label= "Auteurs",command=identite) #bouton 'Auteurs' du menu

menubar.add_cascade(label="A propos",menu=menuaide) #cascade 'A propos' du menu

mw.config(menu=menubar)

#disposition des differents élements sur le canvas
labelVie.grid(row=7,column=2)
labelScore.grid(row = 1, column = 2,sticky = 'ns' )
buttonLaunch.grid(row = 2, column = 2, sticky = 'ns')
buttonQuit.grid(row = 3, column = 2, sticky = 'ns')
FrameBot.grid(row = 8,column = 1)
buttonFacile.grid(row = 1, column = 1)
buttonHard.grid(row = 1, column = 2)


mw.mainloop()



