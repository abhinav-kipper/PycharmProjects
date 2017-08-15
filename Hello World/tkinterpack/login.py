__author__ = 'Manoj'

from Tkinter import *

root=Tk()

Label1=Label(root, text="Name")
entry1=Entry(root) #FIELD
Label2=Label(root,text="Password")
entry2=Entry(root)
#GRID
Label1.grid(row=0,sticky=E) #sticky is for alignment in it . It has N E W S . E is Right alligned.
Label2.grid(row=1,sticky=E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c= Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

#Binding funtions to Layouts

#def printName():
 #   print "Welcome..."

#button=Button(root,text="LogIn Man!", command=printName)
#button.grid(row=3, column=1)

#other way

button=Button(root,text="LogIn Man!",)
button.grid(row=3, column=1)
def printName(event): #event shows refer to some event
    print "Welcome..."
button.bind("<Button-1>",printName) # <Button-1> refers to left mouse click


#menu
loginmenu=Menu(root)
root.config(menu=loginmenu)
submenu=Menu(loginmenu) #menu in loginmenu
loginmenu.add_cascade(label="file",menu=submenu) #Cascading ---Drop down menu

submenu.add_command(label="New",command=printName)
submenu.add_command(label="Open",command=printName)
#Seperator
submenu.add_separator()
submenu.add_command(label="Exit",command=root.quit)

editmenu=Menu(loginmenu)
loginmenu.add_cascade(label="edit",menu=editmenu)
#add command to edit menu
editmenu.add_command(label="View",command=printName)

#----Toolbar

toolbar=Frame(root,bg="blue")
insertBut=Button(toolbar,text="INSERT",command=printName)
insertBut.pack(side=LEFT,padx=2,pady=2) #pixel x and y axis arepadx and y
printBut=Button(toolbar,text="PRINT",command=printName)
printBut.pack(side=LEFT)
toolbar.pack(side=TOP,fill=X)

root.mainloop()