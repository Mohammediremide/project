import customtkinter

from tkinter import *
from Quiz_data import score
import tkinter.messagebox
import sqlite3

root =  customtkinter.CTk()
root.minsize(width=450, height=550)
root.maxsize(width=450, height=550)
root.title('Registration form')
root.config(background='#ffe6f0')

fn = StringVar()
ln = StringVar()
em = StringVar()
var = StringVar()

var_c2 = 'Python'

radio_var = StringVar()

sc = f'{score}' 


def printentry():
    first = fn.get()
    second = ln.get()
    email = em.get()
    gender = var.get()
    var3 = var_c2
    var4 = radio_var.get()
    # score = score_label

    conn = sqlite3.connect('form.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (id INTEGER PRIMARY KEY AUTOINCREMENT, FName TEXT, LName TEXT, email TEXT, COUNTRY TEXT, ProgLanguage TEXT, Gender TEXT, score TEXT)')
    cursor.execute('''INSERT INTO STUDENT(FName, LName , email, Country, ProgLanguage, Gender, score)Values(?, ?, ?, ?, ?, ?, ?)''', (first, second, email, gender, var3, var4, score))
    conn.commit()
    
   
  
    tkinter.messagebox.showinfo('Congratulations', 'You have succesfully finished your exam!! Good job')

heading = Label(root, text='Registration Form', relief=SOLID, width=20, font='arial 19 bold', fg='#b30047', bg='#ffe6f0')    
heading.pack(pady=10)

fname = Label(root, text='First Name: ', width=20, font='bold 10', bg='#ffe6f0' )
fname.pack(pady=10)


efname = Entry(root, textvariable=fn)
efname.pack(pady=10)

lname = Label(root, text='Last Name: ', width=20, font='bold 10', bg='#ffe6f0')
lname.pack(pady=10)

elname = Entry(root, textvariable=ln)
elname.pack(pady=10)

address = Label(root, text='email address: ', width=20, font='bold 10', bg='#ffe6f0')
address.pack(pady=10)

eemail = Entry(root, textvariable=em)
eemail.pack(pady=10)

country = Label(root, text='country', width=20, font='bold 10', bg='#ffe6f0' )
country.pack(pady=10)


List = ['Nigeria', 'America', 'Nepal', 'SouthAfrica', 'Canada']
droplist = OptionMenu(root, var, *List)

var.set('selectcountry')
droplist.config(width=15)
droplist.pack(pady=10)

Language = Label(root, text='Prog Lang ', width=20, font='bold 10', bg='#ffe6f0')
Language.pack(pady=10)

c1 = Checkbutton(root, text='Python', variable=var_c2).pack(pady=10)

gender = Label(root, text='Gender: ', width=20, font='bold 10', bg='#ffe6f0').pack(pady=10)
r1 = Radiobutton(root, text='Male', variable=radio_var, value='Male').pack(pady=10)
r2 = Radiobutton(root, text='Female', variable=radio_var, value='Female').pack(pady=10)


submit = Button(root, text='Submit', width=12, bg='#ff4d94', fg='white', command=printentry).pack(pady=10)
Quit = Button(root , text='Quit', width=12, bg='#ff4d94', fg='white', command=exit).pack(pady=10)






root.mainloop()