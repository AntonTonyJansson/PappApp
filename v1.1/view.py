from db import *
from tkinter import *
import glob, os
import tkinter

path = "C:/Users/anton/Documents/Python/PappApp/v1.1"
os.chdir(path)


def start():
    top = tkinter.Tk()
    top.state('zoomed')
    top.title("Lär dig italienska")
    B = tkinter.Button(top, text="Testa dina kunskaper", command=test,  width=20, height=2, bd=10, font=('Helvetica', '20'))
    C = tkinter.Button(top, text="Skapa ordlista", command=create_list,  width=20, height=2, bd=10, font=('Helvetica', '20'))
    D = tkinter.Button(top, text="Radera ordlista", command=delete_list,  width=20, height=2, bd=10, font=('Helvetica', '20'))
    E = tkinter.Button(top, text="Redigera ordlista", command=edit_list,  width=20, height=2, bd=10, font=('Helvetica', '20'))
    F = tkinter.Button(top, text="Avsluta", command=terminate, width=20, height=2, bd=10, font=('Helvetica', '20'))
    B.pack(), C.pack(), D.pack(), E.pack(), F.pack()
    top.mainloop()


def terminate():
    import sys
    sys.exit()


def exit_window(t):
    t.destroy()


def create_list():
    top = Tk()
    top.state('zoomed')
    top.title("Namnge din ordlista")
    L1 = Label(top, text="Namn på ordlista:", width=20, height=2, bd=10, font=('Helvetica', '20'))
    L1.pack()
    E1 = Entry(top, width=20, bd=10, font=('Helvetica', '20'))
    E1.pack()
    b = Button(top, text="Submit", command=lambda e=E1: create_file(e.get()+".txt", top),
               width=20, height=2, bd=10, font=('Helvetica', '20'))
    b.pack()
    top.mainloop()


def create_file(name, t):
    open(name, "w").close()
    t.destroy()
    add_words(name)


def add_words(name):
    top = Tk()
    top.state('zoomed')
    top.title("Ord")
    L1 = Label(top, text="Ord på italienska:", width=20, height=2, bd=10, font=('Helvetica', '20'))
    L1.pack()
    E1 = Entry(top, width=20, bd=10, font=('Helvetica', '20'))
    E1.pack()
    L2 = Label(top, text="Ord på svenska:", width=20, height=2, bd=10, font=('Helvetica', '20'))
    L2.pack()
    E2 = Entry(top, width=20, bd=10, font=('Helvetica', '20'))
    E2.pack()
    b = Button(top, text="Submit", command=lambda e1=E1, e2=E2: write_word(name, e1.get(), e2.get(), e1, e2),
               width=20, height=2, bd=10, font=('Helvetica', '20'))
    b.pack()
    c = Button(top, text="Exit", command=lambda t=top: exit_window(t),
               width=20, height=2, bd=10, font=('Helvetica', '20'))
    c.pack()
    top.mainloop()


def write_word(name, i, s, e1, e2):
    f = open(name, "a")
    f.write(i + "\n")
    f.write(s + "\n")
    e1.delete(0, END)
    e2.delete(0, END)
    f.close()



def delete_list():
    top = tkinter.Tk()
    top.state('zoomed')
    top.title("Detta är dina ordlistor du sparat hittills:")
    lb1 = Listbox(top, width=34, height=20, bd=10, font=('Helvetica', '30'))
    for file in glob.glob("*.txt"):
        lb1.insert(END, file)
    lb1.pack()
    b = Button(top, text="Delete", command=lambda lb=lb1: remove_file(lb.get(ACTIVE), lb1),
               width=32, height=3, bd=10, font=('Helvetica', '30'))
    b.pack()
    top.mainloop()


def remove_file(name,l):
    os.remove(name)
    l.delete(ACTIVE)


def edit_list():
    top = tkinter.Tk()
    top.state('zoomed')
    top.title("Detta är dina ordlistor du sparat hittills:")
    lb1 = Listbox(top, width=34, height=10, bd=10, font=('Helvetica', '30'))
    for file in glob.glob("*.txt"):
        lb1.insert(END, file)
    lb1.pack()
    a = Button(top, text="Add words", command=lambda lb=lb1: add_words(lb.get(ACTIVE)),
               width=32, height=3, bd=10, font=('Helvetica', '30'))
    a.pack()
    r = Button(top, text="Edit", command=lambda lb=lb1: add_words(lb.get(ACTIVE)),
               width=32, height=3, bd=10, font=('Helvetica', '30'))
    r.pack()
    top.mainloop()
