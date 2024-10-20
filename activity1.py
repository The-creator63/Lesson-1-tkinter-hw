#Importing tkinter module
from tkinter import*

#creating the tkinter window
root = Tk()

#creating a button
btn = Button(root,text = "Click me!",background = "#23395B",command = root.destroy)
btn2 = Button(root,text = "Click me!",background = "#23395B",command = root.destroy)
btn3 = Button(root,text = "Click me!",background = "#23395B",command = root.destroy)
btn4 = Button(root,text = "Click me!",background = "#23395B",command = root.destroy)
#position the button
btn.pack(side = "top")
btn2.pack(side = "bottom")
btn3.pack(side = "left")
btn4.pack(side = "right")

root.mainloop()