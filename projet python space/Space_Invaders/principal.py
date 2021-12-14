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

def demarrer():
    demarrer()
buttonLaunch = Button (mw, text = "Lancer la partie", fg = 'blue', command = demarrer)



buttonQuit = Button (mw, text = 'Quitter la partie', fg = 'red', command = mw.destroy)


largeur = 700
hauteur = 700
canevas = Canvas(mw , width = largeur, height = hauteur)

buttonFacile = Button(mw, text = "Facile", anchor = NW)
buttonFacile.configure(width = 10, height = 2, activebackground = "#33B5E5", relief = FLAT)
button1_window = canevas.create_window(200, 250, anchor=NW, window=buttonFacile) #il manque l'attribut command

buttonHard = Button(mw, text = "Hardcore", anchor = NW)
buttonHard.configure(width = 10, height = 2, activebackground = "#33B5E5", relief = FLAT)
button2_window = canevas.create_window(400, 250, anchor=NW, window=buttonHard)#il manque l'attribut command

photo = PhotoImage(file = "photo.gif") 
item =canevas.create_image(20, 20, anchor = NW, image = photo)

canevas.grid(row = 1, column = 1, rowspan = 7, sticky = 'nesw')
labelScore.grid(row = 1, column = 2,sticky = 'ns' )
buttonLaunch.grid(row = 4, column = 2, sticky = 'ns')
buttonLaunch.grid(row = 2, column = 2, sticky = 'ns')
buttonQuit.grid(row = 3, column = 2, sticky = 'ns')


mw.mainloop()

