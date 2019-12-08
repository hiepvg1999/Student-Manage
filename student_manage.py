from tkinter import *
from db import *
from tkinter import messagebox
db= Database()

def populate_list():
    student_list.delete(0,END)
    for row in db.fetch():
        student_list.insert(END,row)
def add_item():
    if mssv_text.get()=='' or name_text.get()=='' or sclass_text.get() =='' or phone_text.get() =='' or address_text.get()=='':
        messagebox.showerror('Required fields','Please include all fields')
        return
    
    db.insert(mssv_text.get(),name_text.get(),sclass_text.get(),phone_text.get(),address_text.get())
    student_list.delete(0,END)
    student_list.insert(END,(name_text.get(),sclass_text.get(),phone_text.get(),address_text.get()))
    clear_text()
    populate_list()

def remove_item():
    db.remove(mssv_text.get())
    clear_text()
    populate_list()

def update_item():
    db.update(mssv_text.get(),name_text.get(),sclass_text.get(),phone_text.get(),address_text.get())
    populate_list()

def clear_text():
    mssv_entry.delete(0,END)
    
    name_entry.delete(0, END)

    sclass_entry.delete(0, END)

    phone_entry.delete(0, END)

    address_entry.delete(0, END)

app = Tk()

name_text = StringVar()
name_label = Label(app,text='Name', font =('bold',14),pady= 20)
name_label.grid(row = 0, column= 0,sticky = W)
name_entry = Entry(app, textvariable = name_text)
name_entry.grid(row=0,column = 1)

sclass_text = StringVar()
sclass_label = Label(app,text='Class', font =('bold',14),pady= 20)
sclass_label.grid(row = 0, column= 2,sticky = W)
sclass_entry = Entry(app, textvariable = sclass_text)
sclass_entry.grid(row=0,column = 3)

mssv_text = StringVar()
mssv_label = Label(app,text='MSSV', font =('bold',14),pady= 20)
mssv_label.grid(row = 0, column= 4,sticky = W)
mssv_entry = Entry(app, textvariable = mssv_text)
mssv_entry.grid(row=0,column = 5)

phone_text = StringVar()
phone_label = Label(app,text='Phone Number', font =('bold',14),pady= 20)
phone_label.grid(row = 1, column= 0,sticky = W)
phone_entry = Entry(app, textvariable = phone_text)
phone_entry.grid(row=1,column = 1)

address_text = StringVar()
address_label = Label(app,text='Address', font =('bold',14),pady= 20)
address_label.grid(row = 1, column= 2,sticky = W)
address_entry = Entry(app, textvariable = address_text)
address_entry.grid(row=1,column = 3)

student_list = Listbox(app,height =8, width =50)
student_list.grid(row =3 , column= 0, columnspan =3,rowspan =6, pady =20,padx=20)

scrollbar = Scrollbar(app)
scrollbar.grid(column=3, row=3)

student_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = student_list.yview)

add_btn = Button(app, text='Add Part', width =12,command = add_item)
add_btn.grid(row=2, column=0,pady=20)

add_btn = Button(app, text='Remove Part', width =12,command = remove_item)
add_btn.grid(row=2, column=1,pady=20)

add_btn = Button(app, text='Update Part', width =12,command = update_item)
add_btn.grid(row=2, column=2,pady=20)

add_btn = Button(app, text='Clear Part', width =12,command = clear_text)
add_btn.grid(row=2, column=3,pady=20)
app.title('Part manage')
app.geometry('730x350')
app.mainloop()
