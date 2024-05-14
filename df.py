from tkinter import *
from tkinter import messagebox

jsa = Tk()
jsa.geometry("500x600")
jsa.title("huhuhu")

class bh:
    def __init__(self):
       print("GO TO:https://neal.fun/")
    def gt(self):
       ñ= Label(jsa,text="hola",fg="red")
       ñ.pack(padx=20, pady=10)
       btnc =  Button(jsa, text="hola", command=self.fgr)
       btnc.pack(padx=20, pady=10)
    def fgr(self):
        print("hola")
        messagebox.showinfo("Imprimiste algo inutil","hola" )

o = bh()
btny =  Button(jsa, text="imprimir hola", command=o.gt)
btny.pack(padx=20, pady=10)


jsa.mainloop()