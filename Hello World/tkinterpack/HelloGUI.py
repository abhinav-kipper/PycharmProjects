__author__ = 'Manoj'
#Using Python 2.7
#imported tkinter GUI Builtin

from Tkinter import *
#root is object which creates blank window
root=Tk()
# text is label in tkinter
#theLabel = Label(root, text = "This is easy")
#theLabel.pack()

topFrame=Frame(root)
#need to pack thing to display
topFrame.pack()
bottomFrame=Frame(root)
#parameter to pack as where to put it
bottomFrame.pack(side=BOTTOM)

#Create Widgets
button1=Button(topFrame,text="Button1",fg="red") # Para1 where u wanna put it and Para2 for text, para3 is for color
button2=Button(topFrame,text="Button2",fg="blue")
button3=Button(topFrame,text="Button3",fg="green")
button4=Button(bottomFrame,text="Button4",fg="purple")
#fg is foreground and bg is background colors
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)


#Fitting widgets in Layout
one = Label(root, text="one",bg="red" ,fg="white")
one.pack()
two = Label(root, text="two",bg="green" ,fg="black")
two.pack(fill=X) #one wont grow with window but not the other one X is X direction
three = Label(root, text="three",bg="blue" ,fg="black")
three.pack(side=LEFT,fill=Y)


#GRID Layout

root.mainloop()