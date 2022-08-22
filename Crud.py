# importing necessary modules
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import mysql.connector


# connecting sql database to pyton
from tkinter.simpledialog import askstring
prompt=askstring("Required field","Enter pasword for database")
try:
     mydb=mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6511664",password=prompt)
     messagebox.showinfo("Connetion","connection sucessfull")
     cursor=mydb.cursor()
     cursor.execute("use sql6511664")
except Exception as e:
    messagebox.showinfo("connection failed",e)
    exit()

# main window

win=Tk()
win.geometry("800x600")
win.title("Program")
win.resizable(0,0)

# global variables-
global e1
global e2
global e3
global e4

#Entry widgets to get data
e1=Entry(win)
e1.place(x=150,y=75,width=175,height=35)
e2=Entry(win)
e2.place(x=150,y=125,width=175,height=35)
e3=Entry(win)
e3.place(x=150,y=175,width=175,height=35)
e4=Entry(win)
e4.place(x=150,y=225,width=175,height=35)


#Text labels

tk.Label(win,text="Name",fg="black",font=('Georgia',20)).place(x=50,y=75)
tk.Label(win,text="D-O-B",fg="black",font=('Georgia',20)).place(x=50,y=125)
tk.Label(win,text="Email",fg="black",font=('Georgia',20)).place(x=50,y=175)
tk.Label(win,text="Phone",fg="black",font=('Georgia',20)).place(x=50,y=225)
tk.Label(win,text="Note! Phone number should be unique",font=("Georgia",8)).place(x=50,y=550)
tk.Label(win,text="And Record must be selected to perform actions on it.",font=("Georgia",8)).place(x=275,y=550)
tk.Label(win,text="Developed by Mithlesh BCA",font=("Georgia",8)).place(x=600,y=550)
tk.Label(win,text="linkedin/insta-@mithlesh1144",font=("Georgia",8)).place(x=600,y=575)
tk.Label(win,text="year-month-day",font=("Georgia",7)).place(x=50,y=155)

# column to show data
tree=ttk.Treeview()
tree['show']='headings'
tree["columns"]=("Name","D.O.B","Email","Phone")
tree.column("Name",width=175,minwidth=50,anchor=tk.CENTER)
tree.column("D.O.B",width=175,minwidth=50,anchor=tk.CENTER)
tree.column("Email",width=175,minwidth=50,anchor=tk.CENTER)
tree.column("Phone",width=175,minwidth=50,anchor=tk.CENTER)
tree.heading("Name",text="Name",anchor=tk.CENTER)
tree.heading("D.O.B",text="D.O.B",anchor=tk.CENTER)
tree.heading("Email",text="Email",anchor=tk.CENTER)
tree.heading("Phone",text="Phone",anchor=tk.CENTER)
tree.place(x=50,y=300)

# function to person actions
def sel_rec():
    clear()
    try:
        m = tree.focus()
        global values
        values=tree.item(m, "values")
        global c
        c=values[3]
        print(c)
        e1.insert(0, values[0])
        e2.insert(0, values[1])
        e3.insert(0, values[2])
        e4.insert(0, values[3])
    except:
        messagebox.showinfo("attention","No record selected")
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)


def ref():
     for item in tree.get_children():
        tree.delete(item)
     q1="SELECT * FROM DEPARTMENT"
     cursor.execute(q1)
     fe=cursor.fetchall()
     for i in fe:
         print(i)
         tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))

def tree_del():
     for item in tree.get_children():
         tree.delete(item)



def add():
    try:
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=int(e4.get())
        sql="INSERT INTO DEPARTMENT(Name,DOB,Email,Phone)VALUES(%s,%s,%s,%s)"
        val=(a1,a2,a3,a4)
        cursor.execute(sql,val)
        mydb.commit()
        e1.insert(0, val[0])
        e2.insert(0, val[1])
        e3.insert(0, val[2])
        e4.insert(0, val[3])
        messagebox.showinfo("Data","Data Entered sucessfully");
        tree.insert("",'end',values=(a1,a2,a3,a4))
        clear()
    except Exception as e:
        messagebox.showinfo("Failed",e)

def delete():
     q1="DELETE FROM DEPARTMENT WHERE Phone=%s"
     try:
         q2=cursor.execute(q1,(c,))
         mydb.commit()
         #tree.delete(values)
         e1.delete(0,END)
         e2.delete(0,END)
         e3.delete(0,END)
         e4.delete(0,END)
         messagebox.showinfo("Attention!","Record deleted sucessfully")
         ref()
     except:
         messagebox.showinfo("Attention","Record not selected")
def del_all():
     s2=messagebox.askyesno("Attention","Are you sure you want to delete all recrods")
     if(s2==True):
           cursor.execute("delete from DEPARTMENT")
           mydb.commit()
           messagebox.showinfo("Attention!","All records deleted sucessfully")
           tree_del()
     if(s2==False):
          ref()
def update():
     a1=e1.get()
     a2=e2.get()
     a3=e3.get()
     a4=int(e4.get())
     try:
         cursor.execute("UPDATE DEPARTMENT set Name=%s, DOB=%s, Email=%s, Phone=%s WHERE Phone=%s" ,(a1,a2,a3,a4,c))
         mydb.commit()
         tree_del()
         e1.delete(0,END)
         e2.delete(0,END)
         e3.delete(0,END)
         e4.delete(0,END)
         ref()
     except:
        messagebox.showinfo("Attention","Record not selected")

# calling ref function show data stored in the first ittration
ref()
# buttons
tk.Button(win,text="ADD",command=add,width=25,height=5).place(x=350,y=75)
tk.Button(win,text="DELETE",command=delete,width=25,height=5).place(x=550,y=75)
tk.Button(win,text="DELETE ALL",command=del_all,width=25,height=5).place(x=550,y=175)
tk.Button(win,text="UPDATE",command=update,width=25,height=5).place(x=350,y=175)
tk.Button(win,text="SELECT_RECORD",command=sel_rec,width=25,height=3).place(x=350,y=15)
tk.Button(win,text="REFRESH_DATABASE",command=ref,width=25,height=3).place(x=550,y=15)
win.mainloop()
