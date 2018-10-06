from tkinter import *
import random
import ctypes
import sys
import string


while True:
    
    window = Tk()
    window.geometry("400x200")

    title = window.title("Create Password")

    note = Label(text = "***Hello Friends***\nSupport : https://github.com/kamranabdullazade/createpassword\n\nNOTE : You can create passwords up to 90 symbols via the program.\n",fg = "Blue")
    note.pack()

    article = Label(text = "Password Length : ")
    article.pack()

    def say():
    

        a = list(range(10))


        character = list(string.ascii_lowercase)
        character2 = list(string.ascii_uppercase)

        k = ["!","@","#","$","%","/","^","&","*","(",")"]

        e = ["9","5","7","8","2","1"]



        b = k + a + character2 + a + character + k + e


        c = []
        random.shuffle(b)
        m1 = int(m.get())
        if m1 > 100:
            MessageBox1 = ctypes.windll.user32.MessageBoxW
            MessageBox1(None, "Please enter a maximum number of 100.", "Warning", 0)
            
        for i in range(0,m1):
            c.append(str(b[i]))

        u = "".join(c)
        print(u)
        window.withdraw()
        window.clipboard_clear()
        window.clipboard_append(u)
        window.update() 
        window.destroy()
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, "Copied to Clipboard", "Copied to Clipboard", 0)
        

    def exit():
        sys.exit()
        
        
    

    m = Entry()
    m.pack()


    button1 = Button(text = "Copy",command=say)
    button1.pack()

    button2 = Button(text = "Exit",command=exit)
    button2.pack()


    mainloop()
