from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import backend
import sqlite3
#================================================ Root Window ==========================================================

root = Tk()
root.geometry('1366x768')
root.title("Student Database Management System")
root.iconbitmap(r'logo.ico')

#=============================================== Variables for storing data ===================================================

StdID = StringVar()
Name = StringVar()
DoB = StringVar()
Branch = StringVar()
Gender = StringVar()
Email = StringVar()
Mobile = StringVar()

#=============================================== Management Frame =====================================================

info_frame = Frame(root, width=506, height=705, bd=2, relief=RIDGE,bg='cyan')
info_frame.pack(side = LEFT)

#=============================================== Mangement Frame Labels ================================================

heading = Label(info_frame, text="STUDENT INFORMATION", bg='Turquoise', width=49, height=2,bd = 5, relief=RIDGE,
                         font=("Open Sans", 12, 'bold'))
heading.place(x=0)
name_label = Label(info_frame, text = "NAME", width=6, font=("Open Sans", 12, 'bold'),bg='cyan')
name_label.place(x=0, y=60)
roll_label = Label(info_frame, text="ROLL NO", width=8, font=("Open Sans", 12, 'bold'),bg='cyan')
roll_label.place(x=0, y=120)
branch_label = Label(info_frame, text="BRANCH", width=8, font=("Open Sans", 12, 'bold'),bg='cyan')
branch_label.place(x=0, y=180)
email_label = Label(info_frame, text="EMAIL", width=6, font=("Open Sans", 12, 'bold'),bg='cyan')
email_label.place(x=0, y=300)
gender_label = Label(info_frame, text="GENDER", width=8, font=("Open Sans", 12, 'bold'),bg='cyan')
gender_label.place(x=0, y=240)
contact_no_label = Label(info_frame, text="CONTACT", width=9, font=("Open Sans", 12, 'bold'),bg='cyan')
contact_no_label.place(x=0, y=360)
d_o_b_label = Label(info_frame, text="D.O.B", width=6, font=("Open Sans", 12, 'bold'),bg='cyan')
d_o_b_label.place(x=0, y=420)

#=============================================== Mangement Frame Entry =================================================

name_entry = Entry(info_frame,textvariable=Name, width=60)
name_entry.place(x=100, y=60)

roll_entry = Entry(info_frame, textvariable=StdID, width=20)
roll_entry.place(x=100, y=120)

Mobile_entry = Entry(info_frame,textvariable=Mobile, width=20)
Mobile_entry.place(x=100, y=360)

email_entry = Entry(info_frame,textvariable=Email, width=60)
email_entry.place(x=100, y=300)

dob_entry = Entry(info_frame,textvariable=DoB, width=20)
dob_entry.place(x=100, y=420)

branch_entry = Entry(info_frame,textvariable=Branch, width=50)
branch_entry.place(x=100, y=180)

gender_entry = Entry(info_frame,textvariable=Gender, width=20)
gender_entry.place(x=100,y=240)


#==================================================== Insert function ====================================================

def insertdata () :
    if( name_entry.get()=="" or roll_entry.get()=="" or Mobile_entry.get()=="" or email_entry.get()=="" or dob_entry.get()=="" or branch_entry.get()=="" or gender_entry.get()==""):
        messagebox.showinfo("STUDENT DATABASE", "All fields are compulsory")
    else :
        backend.addStdRec(StdID.get(), Name.get(), Branch.get(), Gender.get(), DoB.get(), Mobile.get(),Email.get())
        display()

#================================================ Display Function =====================================================

def display () :
    # Create connection
    conn = sqlite3.connect('studentrecord.db')
    # create cursor
    c = conn.cursor()
    # Display from  db
    c.execute("SELECT *, oid  FROM studentmanagement")
    rows = c.fetchall()
    rows.sort(key = lambda rows : rows[0])
    if len(rows)!=0 :
        disp_table.delete(* disp_table.get_children())
        for row in rows :
            disp_table.insert('' , END ,values = row)
        # commit connection
        conn.commit()
    # close connection
    conn.close()

#================================================ Clear Function =======================================================

def clear () :
    Name.set("")
    StdID.set("")
    Mobile.set("")
    Email.set("")
    DoB.set("")
    Branch.set("")
    Gender.set("")

#================================================ Delete Function ======================================================

def delete () :
    if (len(StdID.get()) != 0):
        backend.deleteRec(row[0])
        clear()
        display()
#================================================ Get Cursor Function ======================================================

def getcursor (ev) :
    global row
    cursor_row = disp_table.focus()
    contents = disp_table.item(cursor_row)
    row = contents['values']
    StdID.set(row[1])
    Name.set(row[2])
    Branch.set(row[3])
    Gender.set(row[4])
    DoB.set(row[5])
    Mobile.set(row[6])
    Email.set(row[7])

#================================================ Update Functions =====================================================

def update():
    if (len(StdID.get()) != 0):
        backend.deleteRec(row[0])
    if (len(StdID.get()) != 0):
        backend.addStdRec(StdID.get(), Name.get(), Branch.get(), Gender.get(), DoB.get(), Mobile.get(),Email.get())
        disp_table.delete(0, END)
        disp_table.insert(END, (StdID.get(), Name.get(), Branch.get(), Gender.get(), DoB.get(), Mobile.get(),Email.get()))
        display()


#================================================ Management Frame Buttons =============================================

insert_button = Button(info_frame, text="INSERT", width=10, height=1,
                                 activebackground="green", font=("Open Sans", 12, 'bold'), command = insertdata)
insert_button.place(x=10, y=620)
delete_button = Button(info_frame, text="DELETE", width=10, height=1,
                               activebackground="green", font=("Open Sans", 12, 'bold'), command = delete)
delete_button.place(x=250, y=620)
update_button = Button(info_frame, text="UPDATE", width=10, height=1,
                               activebackground="green", font=("Open Sans", 12, 'bold'), command = update)
update_button.place(x=130, y=620)
clear_button = Button(info_frame, text="CLEAR", width=10, height=1,
                               activebackground="green", font=("Open Sans", 12, 'bold') , command = clear)
clear_button.place(x=370, y=620)


#================================================ Display Canvas =======================================================

disp_canvas = Canvas(root ,  width=840, height=700,relief=RIDGE,bg='cyan')
yscrollbar = Scrollbar(disp_canvas)
yscrollbar.pack(side = RIGHT, fill=Y)
xscrollbar = Scrollbar(disp_canvas, orient=HORIZONTAL)
xscrollbar.pack(side = BOTTOM , fill = X)
disp_table = ttk.Treeview(disp_canvas , columns = ("1" , "2" , "3" , "4" , "5" , "6" , "7", "8") , yscrollcommand = yscrollbar.set , xscrollcommand = xscrollbar.set )
yscrollbar.config(command=disp_table.yview)
xscrollbar.config(command=disp_table.xview)
disp_table.heading("1", text = "Id")
disp_table.heading("2", text = "Roll")
disp_table.heading("3", text = "Name")
disp_table.heading("4", text = "Branch")
disp_table.heading("5", text = "Gender")
disp_table.heading("6", text = "DOB")
disp_table.heading("7", text = "Contact")
disp_table.heading("8", text = "Email")
disp_table['show'] = 'headings'
disp_table.pack(expand = True , fill = Y , pady = 105 ,padx = 10)
disp_canvas.pack(expand=True, fill=BOTH)
heading_2= Label(disp_canvas, text="STUDENT DISPLAY", bg='Turquoise', width=83, height=2,bd=5, relief=RIDGE,
                        font=("Open Sans", 12, 'bold'))
heading_2.place(x=0 , y=0)
# Calling getcursor function

disp_table.bind("<ButtonRelease-1>",getcursor)

# Calling Display Function
display()



root.mainloop()