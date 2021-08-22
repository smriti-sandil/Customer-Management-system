"CMS PL using TKinter"

from tkinter import *
from tkinter import messagebox
from CMSBLL import *

def btnAdd_click():
    cus = Customer()
    cus.id = varID.get()
    cus.name = varName.get()
    cus.age = varAge.get()
    cus.mob_no = varMob_no.get()
    cus.addCustomer()
    messagebox.showinfo("CMS","Customer Added Successfully")
    varID.set("")
    varName.set("")
    varAge.set("")
    varMob_no.set("")

def btnSearch_click():
    cus = Customer()
    cus.id = varID.get()
    cus = cus.searchCustomer()
    varName.set(cus.name)
    varAge.set(cus.age)
    varMob_no.set(cus.mob_no)

def btnDelete_click():
    ch = messagebox.askyesno("CMS","Are you sure you want to delete this customer?")
    if ch == True:
        cus = Customer()
        cus.id = varID.get()
        cus.deleteCustomer()
        messagebox.showinfo("CMS","Customer Deleted Successfully")

def btnModify_click():
    cus = Customer()
    cus.id = varID.get()
    cus.name = varName.get()
    cus.age = varAge.get()
    cus.mob_no = varMob_no.get()
    cus.updateCustomer()
    messagebox.showinfo("CMS","Customer Updated Successfully")

def btnAll_click():
    root1 = Tk()
    root1.title("All Customers")
    lblID1 = Label(root1,text = "Cust ID", bg = "Orange", width = 10, font = 20)
    lblID1.grid(row = 0, column = 0)
    lblName1 = Label(root1,text = "Cust Name", bg = "Orange", width = 10, font = 20)
    lblName1.grid(row = 0, column = 1)
    lblAge1 = Label(root1,text = "Cust Age", bg = "Orange", width = 10, font = 20)
    lblAge1.grid(row = 0, column = 2)
    lblMob1 = Label(root1,text = "Cust Mob", bg = "Orange", width = 10, font = 20)
    lblMob1.grid(row = 0, column = 3)
    i = 1
    for cus in Customer.cus_list:
        lblID2 = Label(root1, text = f"{cus.id}",bg = "Yellow", width = 10, font = 20)
        lblID2.grid(row = i, column = 0)
        lblName2 = Label(root1, text=f"{cus.name}", bg="Yellow", width=10, font=20)
        lblName2.grid(row=i, column=1)
        lblAge2 = Label(root1, text=f"{cus.age}", bg="Yellow", width=10, font=20)
        lblAge2.grid(row=i, column=2)
        lblMob2 = Label(root1, text=f"{cus.mob_no}", bg="Yellow", width=10, font=20)
        lblMob2.grid(row=i, column=3)
        i+=1

def btnExit_click():
    root.destroy()

root = Tk()
root.geometry("600x600")
root.title("Our CMS")

lblID = Label(root, text = "Enter Customer ID:", font = 20)
lblID.grid(row = 0, column = 0)
varID = StringVar()
entrID = Entry(root, textvariable = varID, font = 20)
entrID.grid(row = 0, column = 1)

lblName = Label(root, text = "Enter Customer Name:", font = 20)
lblName.grid(row = 1, column = 0)
varName = StringVar()
entrName = Entry(root, textvariable = varName, font = 20)
entrName.grid(row = 1, column = 1)

lblAge = Label(root, text = "Enter Customer Age:", font = 20)
lblAge.grid(row = 2, column = 0)
varAge = StringVar()
entrAge = Entry(root, textvariable = varAge, font = 20)
entrAge.grid(row = 2, column = 1)

lblMob_no = Label(root, text = "Enter Customer Mob_no:", font = 20)
lblMob_no.grid(row = 3, column = 0)
varMob_no = StringVar()
entrMob_no = Entry(root, textvariable = varMob_no, font = 20)
entrMob_no.grid(row = 3, column = 1)

btnAdd = Button(root, text = "Add Cus", font = 20, width = 15, command = btnAdd_click)
btnAdd.grid(row = 4, column = 0)

btnSearch = Button(root, text = "Search Cus", font = 20, width = 15, command = btnSearch_click)
btnSearch.grid(row = 4, column = 1)

btnDelete = Button(root, text = "Delete Cus", font = 20, width = 15, command = btnDelete_click)
btnDelete.grid(row = 4, column = 2)

btnModify = Button(root, text = "Modify Cus", font = 20, width = 15, command = btnModify_click)
btnModify.grid(row = 5, column = 0)

btnAll = Button(root, text = "View all Cus", font = 20, width = 15, command = btnAll_click)
btnAll.grid(row = 5, column = 1)

btnExit = Button(root, text = "Exit", font = 20, width = 15, command = btnExit_click)
btnExit.grid(row = 5, column = 2)


root.mainloop()