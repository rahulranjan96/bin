from tkinter import *


"""class rahulbutton:
 def __init__(self,master):
  frame=Frame(master)
  frame.grid()
  self.printButton = Button(frame,text="Print Message",command=self.printMessage)
  self.printButton.grid()
  self.quitButton = Button(frame,text="Quit",command=frame.quit)
  self.quitButton.grid()
 def printMessage(self):
  print("Hello Everyone!!") 

root = Tk()
r = rahulbutton(root)
root.mainloop()"""#Tut 8


"""topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
button1 = Button(topFrame,text="Button 1",fg="red")
button2 = Button(topFrame,text="Button 2",fg="blue")
button3 = Button(topFrame,text="Button 3",fg="green")
button4 = Button(bottomFrame,text="Button 4",fg="purple")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)"""#Tut2


"""one=Label(root,text="ONE",bg="red",fg="white")
one.pack()
two=Label(root,text="TWO",bg="green",fg="black")
two.pack(fill=X)
three=Label(root,text="THREE",bg="blue",fg="white")
three.pack(fill=Y,side=LEFT)"""#Tut3


"""label1=Label(root,text="Name")
label2=Label(root,text="Password")
entry1=Entry(root)
entry2=Entry(root)
label1.grid(row=0,column=0,sticky=E)
label2.grid(row=1,column=0,sticky=E)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
checkbox=Checkbutton(root,text="Keep me logged in!!")
checkbox.grid(columnspan=2,row=2)"""#Tut4 && Tut5


"""def printname():
	print("Hello my name is Rahul Ranjan")
button1=Button(root,text="What is your name?",command=printname)
button1.grid()"""#Tut 6
"""def printname(event):
	print("Hello my name is Rahul Ranjan")
button1=Button(root,text="What is your name?")
button1.bind("<Button-1>",printname)
button1.grid()"""#Tut 6


"""def leftClick(event):
	print("You clicked left-mouse button")
def rightClick(event):
	print("You clicked right-mouse button")
def middleClick(event):
	print("You clicked middle-mouse button")

frame=Frame(root,width=300,height=250)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middleClick)
frame.bind("<Button-3>",rightClick)
frame.grid()""" #Tut 7



"""def doNothing():
 print("Okay Okay I won't...cool..cool..")

root = Tk()
menu = Menu(root)
root.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Now",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=doNothing)
subMenu.add_separator()
editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Undo",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Window Size",command=doNothing)
editMenu.add_separator()
root.mainloop()""" #Tut 9




"""def doNothing():
 print("Okay Okay I won't...cool..cool..")

root = Tk()

#**********Main Menu*********

menu = Menu(root)
root.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Now",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=doNothing)
subMenu.add_separator()
editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Undo",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Window Size",command=doNothing)
editMenu.add_separator()

#***********Tool Bar**********

toolbar = Frame(root,bg="blue")
insertButton = Button(toolbar,text="Insert Image",command=doNothing)
insertButton.pack(side=LEFT,pady=10,padx=10)
printButton = Button(toolbar,text="Print",command=doNothing)
printButton.pack(side=LEFT,pady=10,padx=10)
toolbar.pack(side=TOP,fill=X)
root.mainloop()""" #Tut 10





"""def doNothing():
 print("Okay Okay I won't...cool..cool..")

root = Tk()

#**********Main Menu*********

menu = Menu(root)
root.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Now",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=doNothing)
subMenu.add_separator()
editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Undo",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Window Size",command=doNothing)
editMenu.add_separator()

#***********Tool Bar**********

toolbar = Frame(root,bg="blue")
insertButton = Button(toolbar,text="Insert Image",command=doNothing)
insertButton.pack(side=LEFT,pady=10,padx=10)
printButton = Button(toolbar,text="Print",command=doNothing)
printButton.pack(side=LEFT,pady=10,padx=10)
toolbar.pack(side=TOP,fill=X)

#***********Status Bar**********

status = Label(root,text="Preparing to do nothing...",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()""" # Tut 11



"""import tkinter.messagebox
root = Tk()
tkinter.messagebox.showinfo("Window Title","Monkeys can live upto 300 years.")
answer = tkinter.messagebox.askquestion("Question 1","Do you like silly faces?")

if answer == "yes":
 print("8===D--")
else:
 print("DDDDD")
root.mainloop()""" # Tut 12



"""
root =Tk()

canvas = Canvas(root,width=200,height=100)
canvas.pack()

blackLine = canvas.create_line(0,0,120,50)
redLine = canvas.create_line(0,100,120,50,fill="red")
greenBox=canvas.create_rectangle(25,25,130,60,fill="green")
canvas.delete(redLine)
canvas.delete(blackLine)
canvas.delete(ALL)


root.mainloop()

""" #Tut 13




"""root = Tk()

photo = PhotoImage(file="img.PNG")
label = Label(root,image=photo)
label.pack()

root.mainloop()""" #Tut 14