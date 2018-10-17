from tkinter import *
import string
import random
import ctypes
import sys

while True:


    window = Tk()

    title = window.title("Create Password")

    window.geometry("500x320")

    note = Label(text = "***Hello Friends***\nSupport : https://github.com/kamranabdullazade/createpassword\nor\nhttps://www.instagram.com/k4mran_abdullazade\n\nNOTE : You can create passwords up to 100 symbols via the program.\n",fg = "Blue")
    note.pack()

    vers = Label(text="V2.0")
    vers.pack(side=BOTTOM)


    def about():
        MessageBox1 = ctypes.windll.user32.MessageBoxW
        MessageBox1(None,"Hello Friends, This program is written in Python 3.\n\nYou can create passwords up to 100 symbols via the program.\n\n\nYou can contact me at : https://www.instagram.com/k4mran_abdullazade\n\n\nDeveloper : Kamran Abdullazade\nVersion : 2.0","About", 0)


    menu = Menu()

    menu.add_command(label="About", command=about)

    window.config(menu=menu)

    def say():
        a = list(range(10))

        character = list(string.ascii_lowercase)
        character2 = list(string.ascii_uppercase)

        k = ["!", "@", "#", "$", "%", "/", "^", "&", "*", "(", ")"]


        if che1.get() == 1 and che2.get() == 1 and che3.get() == 1 and che4.get() == 1:
            b = k + a + character2 + character + k + a + character2 + character

        elif che1.get() == 1 and che2.get() == 1 and che3.get() == 1:
            b = k + a + character2 + k + a + character2 + k + a + character2

        elif che2.get() == 1 and che3.get() == 1 and che4.get() == 1:
            b = a + character2 + character + a + character2 + character

        elif che1.get() == 1 and che2.get() == 1:
            b = k + a + k + a + k + a + k + a + k + a

        elif che1.get() == 1 and che3.get() == 1:
            b = k + character2 + k + character2 + k + character2 + k + character2

        elif che1.get() == 1 and che4.get() == 1:
            b = k + character + k + character + k + character + k + character

        elif che2.get() == 1 and che3.get() == 1:
            b = a + character2 + a + character2 + a + character2 + a + character2

        elif che2.get() == 1 and che4.get() == 1:
            b = a + character + a + character + a + character + a + character

        elif che3.get() == 1 and che4.get() == 1:
            b = character2 + character + character2 + character

        elif che1.get() == 1:
            b = k + k + k + k + k + k + k + k + k + k

        elif che2.get() == 1:
            b = a + a + a + a + a + a + a + a + a + a + a

        elif che3.get() == 1:
            b = character2 + character2 + character2 + character2 + character2

        elif che4.get() == 1:
            b = character + character + character + character + character

        elif che1.get() == 0 and che2.get() == 0 and che3.get() == 0 and che4.get() == 0:
            MessageBox1 = ctypes.windll.user32.MessageBoxW
            MessageBox1(None, "Please mark at least one option.", "Warning", 0)


        c = []
        random.shuffle(b)
        m1 = int(m.get())
        if m1 > 100:
            MessageBox1 = ctypes.windll.user32.MessageBoxW
            MessageBox1(None, "Please enter a maximum number of 100.", "Warning", 0)

        elif m1 < 4:
            MessageBox1 = ctypes.windll.user32.MessageBoxW
            MessageBox1(None, "Please enter a minimum number of 4.", "Warning", 0)

        else:
            if che1.get() == 1 and che2.get() == 1 and che3.get() == 1 and che4.get() == 1:

                for i in range(0, m1-4):
                    c.append(str(b[i]))
                j = ["/","8","R","h"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che1.get() == 1 and che2.get() == 1 and che3.get() == 1:
                for i in range(0, m1-3):
                    c.append(str(b[i]))
                j = ["/","8","R"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che2.get() == 1 and che3.get() == 1 and che4.get() == 1:
                for i in range(0, m1-3):
                    c.append(str(b[i]))
                j = ["8","R","h"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che1.get() == 1 and che2.get() == 1:
                for i in range(0, m1-2):
                    c.append(str(b[i]))
                j = ["/","8"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che1.get() == 1 and che3.get() == 1:
                for i in range(0, m1-2):
                    c.append(str(b[i]))
                j = ["/","R"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che1.get() == 1 and che4.get() == 1:
                for i in range(0, m1-2):
                    c.append(str(b[i]))
                j = ["/","h"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che2.get() == 1 and che3.get() == 1:
                for i in range(0, m1-2):
                    c.append(str(b[i]))
                j = ["8","R"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che2.get() == 1 and che4.get() == 1:
                for i in range(0, m1-2):
                    c.append(str(b[i]))
                j = ["8","h"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che3.get() == 1 and che4.get() == 1:
                for i in range(0, m1-2):
                    c.append(str(b[i]))
                j = ["R","h"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che1.get() == 1:
                for i in range(0, m1-1):
                    c.append(str(b[i]))
                j = ["/"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che2.get() == 1:
                for i in range(0, m1-1):
                    c.append(str(b[i]))
                j = ["8"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che3.get() == 1:
                for i in range(0, m1-1):
                    c.append(str(b[i]))
                j = ["R"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)

            elif che4.get() == 1:
                for i in range(0, m1-1):
                    c.append(str(b[i]))
                j = ["h"]
                random.shuffle(j)
                u = "".join(c) + "".join(j)


        print(u)
        window.withdraw()
        window.clipboard_clear()
        window.clipboard_append(u)
        window.update()
        window.destroy()
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, "Copied to Clipboard : {}".format(u), "Copied to Clipboard", 0)


    def exit():
        sys.exit()


    che1 = BooleanVar()
    che1.set(True)

    che2 = BooleanVar()
    che2.set(True)

    che3 = BooleanVar()
    che3.set(True)

    che4 = BooleanVar()
    che4.set(True)

    bu1 = Checkbutton(text="Character",var=che1)
    bu1.pack(side=TOP)

    bu2 = Checkbutton(text="Number",var=che2)
    bu2.pack(side=TOP)

    bu3 = Checkbutton(text="Upper Case",var=che3)
    bu3.pack(side=TOP)

    bu4 = Checkbutton(text="Lower Case",var=che4)
    bu4.pack(side=TOP)

    article = Label(text = "Password Length : ")
    article.pack()

    m = Entry()
    m.pack()


    button1 = Button(text = "Copy",command=say)
    button1.pack()

    button2 = Button(text = "Exit",command=exit)
    button2.pack()

    mainloop()
