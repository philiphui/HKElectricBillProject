import cx_Oracle
from tkinter import *

def item_B1_action():
    window_01 = Toplevel(window_00)
    window_01.geometry("800x100")
    centre_window(window_01)
    window_01.title('Show all records')
    label = Label(window_01, text='Show all Records')
    label.pack(padx=300, pady=10)
    listbox = Listbox(window_01)
    listbox.pack(side=LEFT, fill=BOTH, expand=1)
    cur.execute('SELECT CUSTOMERID, CHINESENAME, ENGLISHNAME, EMAIL, ACTIVE FROM CUSTOMERINFO')
    for row in cur.fetchall():
        listbox.insert(END, row)

def item_B2_action():
    window_01 = Toplevel(window_00)
    window_01.geometry("800x100")
    centre_window(window_01)
    window_01.title('Show all records')
    label = Label(window_01, text='Show all Records')
    label.pack(padx=300, pady=10)
    listbox = Listbox(window_01)
    listbox.pack(side=LEFT, fill=BOTH, expand=1)
    cur.execute('SELECT * FROM METER m LEFT JOIN ADDRESS c  ON m.billchineseaddressid = c.addressid LEFT JOIN ADDRESS e ON m.billenglishaddressid = e.addressid')
    for row in cur.fetchall():
        listbox.insert(END, row)

def item_B3_action():
    def search_by_studentID():
        window_02 = Toplevel(window_01)
        window_02.geometry("300x100")
        centre_window(window_02)

        window_02.title('Show all records')
        sql = "SELECT FEE FROM METERFEE where month = " + val_01.get() + " and year = " + val_02.get()
        cur.execute(sql)
        listbox = Listbox(window_02)
        listbox.pack(side=LEFT, fill=BOTH, expand=1)

        listbox.insert(END, 'Fee')
        for row in cur.fetchall():
            listbox.insert(END, row)

    window_01 = Toplevel(window_00)
    window_01.geometry("200x200")
    centre_window(window_01)
    window_01.title('')
    label = Label(window_01, text='Search by Sex')

    Label(window_01, text="Month").grid(row=0)
    Label(window_01, text="Year").grid(row=1)

    val_01 = Entry(window_01)
    val_02 = Entry(window_01)

    val_01.grid(row=0, column=1)
    val_02.grid(row=1, column=1)

    Button(window_01, text='Search', command=search_by_studentID).grid(row=2, column=1)

def item_B4_action():
    def update_student_info():
        window_02 = Toplevel(window_01)
        window_02.geometry("300x100")
        centre_window(window_02)

        window_02.title('Show all records')
        sql = "SELECT METER FROM METER where ACCOUNTNO = '" + val_01.get() + "'"
        cur.execute(sql)
        listbox = Listbox(window_02)
        listbox.pack(side=LEFT, fill=BOTH, expand=1)

        listbox.insert(END, 'METER')
        for row in cur.fetchall():
            listbox.insert(END, row)

    window_01 = Toplevel(window_00)
    window_01.geometry("200x200")
    centre_window(window_01)
    window_01.title('')
    label = Label(window_01, text='Search by Sex')

    Label(window_01, text="Account NO").grid(row=0)
    val_01 = Entry(window_01)

    val_01.grid(row=0, column=1)

    Button(window_01, text='Search', command=update_student_info).grid(row=2, column=1)

def item_B5_action():
    def delete_student_info():
        window_02 = Toplevel(window_01)
        window_02.geometry("300x100")
        centre_window(window_02)

        window_02.title('Show all records')
        sql = "SELECT * FROM METER where ACCOUNTNO = '" + val_01.get() + "'"
        cur.execute(sql)
        listbox = Listbox(window_02)
        listbox.pack(side=LEFT, fill=BOTH, expand=1)

        listbox.insert(END, 'METER')
        for row in cur.fetchall():
            listbox.insert(END, row)

    window_01 = Toplevel(window_00)
    window_01.geometry("200x200")
    centre_window(window_01)
    window_01.title('')
    label = Label(window_01, text='Search by Sex')

    Label(window_01, text="Account NO").grid(row=0)
    val_01 = Entry(window_01)

    val_01.grid(row=0, column=1)

    Button(window_01, text='Search', command=delete_student_info).grid(row=4, column=1)


def item_B6_action():
    def grant_access():
        window_02 = Toplevel(window_01)
        window_02.geometry("300x100")
        centre_window(window_02)
        sql = "Grant SELECT, INSERT ON " + val_01.get() + ".study to std021"
        cur.execute(sql)
        conn.commit()

        msg = Message(window_02, text='Update success.')
        msg.pack()

    window_01 = Toplevel(window_00)
    window_01.geometry("200x200")
    centre_window(window_01)
    window_01.title('')
    label = Label(window_01, text='Grant Access by UserID')

    Label(window_01, text="User ID").grid(row=0)

    val_01 = Entry(window_01)

    val_01.grid(row=0, column=1)

    Button(window_01, text='Submit', command=grant_access).grid(row=2, column=1)

def item_B7_action():

    def create_table():
        window_02 = Toplevel(window_01)
        window_02.geometry("300x100")
        centre_window(window_02)
        sql = "create table std021." + val_02.get() +" as select * from "+ val_01.get() + ".study"

        cur.execute(sql)
        conn.commit()

        msg = Message(window_02, text='Update success.')
        msg.pack()

    window_01 = Toplevel(window_00)
    window_01.geometry("300x200")
    centre_window(window_01)
    window_01.title('')
    label = Label(window_01, text='Create New Table by UserID')

    Label(window_01, text="User ID").grid(row=0)
    Label(window_01, text="New Table Name").grid(row=1)

    val_01 = Entry(window_01)
    val_02 = Entry(window_01)

    val_01.grid(row=0, column=1)
    val_02.grid(row=1, column=1)

    Button(window_01, text='Submit', command=create_table).grid(row=2, column=1)

def centre_window(window):
    window.update_idletasks()
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    window.geometry("%dx%d+%d+%d" % (size + (x, y)))

def create_menu(window):

    my_menu = Menu(window)
    window.config(menu=my_menu)

    # ----Item B----#
    item_B = Menu(my_menu)
    my_menu.add_cascade(label="Bill Function", menu=item_B)
    item_B.add_command(label="1. Display the information of all customer", command=item_B1_action)
    item_B.add_command(label="2. Display the information of all electric meters", command=item_B2_action)
    item_B.add_command(label="3. Search the price of electricity by inputting the month and year", command=item_B3_action)
    item_B.add_command(label="4. Search the meter by using customer information", command=item_B4_action)
    item_B.add_command(label="5. Show all history of meter of selected account number", command=item_B5_action)
    item_B.add_command(label="6. Generate the electricity bill by inputting the date and account number", command=item_B6_action)
    item_B.add_command(label="7. Pay a selected bill", command=item_B7_action)
    item_B.add_command(label="8. Exit", command=window.quit)

"""Main Program"""

conn = cx_Oracle.connect('G2_team004/ceG2_team004@144.214.177.102/xe')

cur = conn.cursor()

window_00 = Tk()
window_00.geometry('800x100')
window_00.title('Group 2 Team 4 - HK Electric Bill')
centre_window(window_00)
create_menu(window_00)

mainloop()

