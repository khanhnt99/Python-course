from tkinter import *

# label = an area widget that holds text and/or an image within a window
window = Tk()

photo = PhotoImage(file='file.png')

label = Label(window,
            text="bro, do you even code?",
            font=('Arial',40,'bold'),
            fg='green',
            bg='black',
            relief=RAISED,
            bd=10,
            pady=20,
            image=photo,
            compound='bottom')
label.pack()
# label.place(x=100, y=100)

window.mainloop()