from tkinter import *
from tkinter import messagebox
from proga import frst_fun
from Proga_part2 import scnd_fun

def rachet():
    a = int(rowww.get())
    b = int(guyss.get())
    c = int(zaddd.get())
    frst_fun(c)
    scnd_fun(a,b)










root = Tk()
root.title('Всплывающее окно')
root.geometry('400x400')
rowww = StringVar()
guyss = StringVar()
zaddd = StringVar()


roww = Label(text='Введите кол-во рядов')
guys = Label(text = 'Введите кол-во учеников')
zadani = Label(text = 'Введите кол-во заданий')

roww.place(relx = 0.1, rely = 0.2)
guys.place(relx = 0.1, rely = 0.3)
zadani.place(relx = 0.1, rely = 0.4)

roww_entry = Entry(textvariable=rowww)
guys_entry = Entry(textvariable=guyss)
zadani_entry = Entry(textvariable=zaddd)

roww_entry.place(relx = 0.5, rely = 0.2)
guys_entry.place(relx = 0.5, rely = 0.3)
zadani_entry.place(relx = 0.5, rely = 0.4)

active_bttn = Button(text='расчитать',command=rachet)
active_bttn.place(relx = 0.5,rely = 0.7)





root.mainloop()