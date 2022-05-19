from tkinter import*
from tkcalendar import DateEntry
# import tkinter as tk
from tkinter import ttk
import sqlite3  as db


root = Tk()
geometry = root.geometry("700x800")
def Datacon():
    con = db.connect("Data.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE expense(date INTEGER,name STRING,tittle STRING,expense INTEGER)")
    cur.close()
Datacon()    
root.title("sheet")
lable =Label(root,text="progress track",font=('black',20,'bold'),bg="red",fg="white",width=12).pack()
DateEntry( date_pattern='MM/dd/yyyy').place(x=200,y=150)
name = Label(root, text="Name",font=('arial',13,'bold'),bg="blue",fg="white").place(x=80,y=53)
entry=Entry(root).place(x=150,y=53)
title = Label(root,text="Title",font=('arial',13,'bold'),bg="blue",fg="white").place(x=90,y=100)
enter_1=Entry(root).place(x=160,y=100)
date = Label(root,text="date",font=('arial',13,'bold'),bg="blue",fg="white").place(x=80,y=150)
expense = Label(root,text="expense",font=('arial',13,'bold'),bg="blue",fg="white").place(x=70,y=200)
enter_3 = Entry(root).place(x=160,y=200)





button = Button(root,text="submit",font=('arial',13,'bold'),bg="blue",fg="white").place(x=80,y=270)
Elist=['Date','Name','Title','Expense']
Etable=ttk.Treeview(root,column=Elist,show='headings',height=7)
for c in Elist:
    Etable.heading(c,text=c.title())
Etable.place(x=5,y=400)


root.mainloop()