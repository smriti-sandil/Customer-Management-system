#BLL STARTS HERE
cusdict={}
def addcustomer(id,name,age,mob):
    cusdict[id]=[name,age,mob]
def deletecustomer(id):
    del cusdict[id]
def modifycustomer(id,name,age,mob):
    cusdict[id]=[name,age,mob]
#BLL ENDS HERE

#PL STARTS HERE
while (1):
    print("welcome to manvendra's CMS")
    print('''press 1 to add customer
            press 2 to search customer
            press 3 to delete customer
            press 4 to modify customer
            press 5 to view all customer
            press 6 to exit''')
    choice1 = input("enter 1,2,3,4,5 or 6:")

    if (choice1 == '1'):
        id = input("enter customer id:")
        name = input("enter customer name:")
        age = int(input("enter customer age:"))
        mob = int(input("enter customer mobile number:"))
        addcustomer(id,name,age,mob)
        print("customer added successfully")
    elif (choice1 == '2'):
        id = input("enter customer id:")
        print(cusdict.get(id))
    elif (choice1 == '3'):
        id = input("enter customer id:")
        deletecustomer(id)
        print("customer deleted successfully")
    elif (choice1 == '4'):
        id = input("enter customer id:")
        name = input("enter updated customer name:")
        age = int(input("enter updated customer age:"))
        mob = int(input("enter updated customer mobile number:"))
        modifycustomer(id,name,age,mob)
        print("customer modified successfully")
    elif (choice1 == '5'):
        k=cusdict.items()
        for i,j in k:
            print(i,":",j)
    elif (choice1 == '6'):
        print("Thanks for using manv cms")
        break
    else:
        print("incorrect choice")
#PL ENDS HERE









