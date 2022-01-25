from tkinter import *
from turtle import back

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() #instantite an instance of a window
window.geometry("420x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="black")

window.mainloop() #place window on computer screen