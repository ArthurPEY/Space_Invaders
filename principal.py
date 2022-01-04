from tkinter import *

import time



def scoreCounter():
    global score
    score.set('Votre score ' + str(0))

mw = Tk()
mw.title('Space invaders')
mw.geometry("{0}x{1}+0+0".format(mw.winfo_screenwidth(), mw.winfo_screenheight()))


score = StringVar()
scoreCounter()
labelScore = Label (mw, textvariable = score, fg = 'red')




def demarrer():


  
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
            coords = canevas.coords(self.rectangle)
            if len(coords) == 0:
                return()
            canevas.after(100,self.movement)
            x0, y0, x1, y1 = coords
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
            self.vie=100
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
            self.obu = canevas.create_oval( ((x0+x1)/2)-2, y0, ((x0+x1)/2)+2, y1, fill = "black")
            
        def tir(self):
            x0, y0, x1, y1 = canevas.coords(self.obu)
            for k in range(len(ennemis)):
                x0alien, y0alien, x1alien, y1alien = canevas.coords(ennemis[k].rectangle)
                if canevas.find_overlapping(x0alien, y0alien, x1alien, y1alien) != (ennemis[k].rectangle,):
                    a=canevas.find_overlapping(x0alien, y0alien, x1alien, y1alien)
                    print(a)
                    canevas.delete(a[0])
                    del ennemis[k]
                    canevas.delete(self.obu)
                    print(len(ennemis))
                    return(None)
            traj=-10
            canevas.move(self.obu, 0, traj)
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
    dif=6
        
        

    canevas = Canvas(mw, width=600, height=400, bg="white",)
    canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
    ennemis=[]
    for k in range(0,dif):
        alienz=alien((dif-k)*50,(dif-k)*50,largeur-k*50)
        ennemis.append(alienz)
        alienz.movement()
        
    # alienz=alien(50,50,500)
    # alienzmov=alienz.movement()




    button=Button(mw, command=kill)
    button.pack()

    # alien1 = alien(0,0,450).movement()
    # alien2 = alien(50,50,500).movement()
    # alien3 = alien(100,100,550).movement()
    # alien4 = alien(150,150,600).movement()


    vaisseau = vaisseau(300)

    mw.bind("<KeyPress-Left>", lambda e: vaisseau.left(e))
    mw.bind("<KeyPress-Right>", lambda e: vaisseau.right(e))
    mw.bind("<KeyPress-Up>", lambda e: balle().tir())
    mw.bind("<KeyPress-Down>", kill)


    print(canevas.coords(vaisseau.vaisseau))
    print(ennemis)

    mainloop()

    

    

buttonLaunch = Button (mw, text = "Lancer la partie", fg = 'blue', command = demarrer)



buttonQuit = Button (mw, text = 'Quitter la partie', fg = 'red', command = mw.destroy)


largeur = 600
hauteur = 400
canevas = Canvas(mw , width = largeur, height = hauteur)

buttonFacile = Button(mw, text = "Facile", anchor = NW)
buttonFacile.configure(width = 10, height = 2, activebackground = "#33B5E5", relief = FLAT)
button1_window = canevas.create_window(200, 250, anchor=NW, window=buttonFacile) #il manque l'attribut command

buttonHard = Button(mw, text = "Difficile", anchor = NW)
buttonHard.configure(width = 10, height = 2, activebackground = "#33B5E5", relief = FLAT)
button2_window = canevas.create_window(400, 250, anchor=NW, window=buttonHard)#il manque l'attribut command

photo = PhotoImage(file = "H:\projet python space\Space_Invaders\photo.gif") 
item =canevas.create_image(20, 20, anchor = NW, image = photo)

canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
labelScore.grid(row = 1, column = 2,sticky = 'ns' )

buttonLaunch.grid(row = 2, column = 2, sticky = 'ns')
buttonQuit.grid(row = 3, column = 2, sticky = 'ns')


mw.mainloop()

