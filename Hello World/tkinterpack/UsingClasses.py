__author__ = 'Manoj'
#Always make classes Not only for tkinter but for everything

from Tkinter import *
root=Tk()

class abhiButtons:
    def __init__(self, master): #para 2 extra for gui
        frame=Frame(master) #root is now the master
        frame.pack()

        self.printButton = Button(frame,text="print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton=Button(frame,text="Quit",command=frame.quit) #uit is builtin which ends the main loop
        self.quitButton.pack(side=LEFT)
    def printMessage(self):
        print "Wow , this actually works."

object1=abhiButtons(root)
root.mainloop()