"""CMS Using OOPS"""


# BLL Starts Here
import pickle
import json
class Customer:

    cus_list = []               # cus_list = [1000, 2000, 3000, ........]

    def __init__(self):
        self.id = 0
        self.name = 0
        self.age = 0
        self.mob_no = 0

    def addCustomer(self):      # self: 1000
        Customer.cus_list.append(self)

    def searchCustomer(self):       # self = 8000
        for e in Customer.cus_list:         # e = 1000
            if e.id == self.id:             # self.id = 210
                return e
        raise ValueError("ID not Found")

    def updateCustomer(self):
        for e in Customer.cus_list:  # e = 1000
            if e.id == self.id:
                e.name = self.name
                e.age = self.age
                e.mob_no = self.mob_no
        raise ValueError("ID not Found")

    def deleteCustomer(self):
        for e in Customer.cus_list:  # e = 1000
            if e.id == self.id:
                Customer.cus_list.remove(e)
                return
        raise ValueError("Customer not Found")

    @staticmethod
    def savetoPickle():
        f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python_12 PM_8th Feb Batch\cmspickle.txt","wb")
        pickle.dump(Customer.cus_list,f)
        f.close()

    @staticmethod
    def loadFromPickle():
        f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python_12 PM_8th Feb Batch\cmspickle.txt","rb")
        Customer.cus_list = pickle.load(f)
        f.close()

    @staticmethod
    def criteriaID(ob):
        return ob.id

    @staticmethod
    def mySort():
        Customer.cus_list.sort(key = Customer.criteriaID)

    @staticmethod
    def convertToDict(ob):
        return ob.__dict__

    @staticmethod
    def saveToJSON():
        f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python_12 PM_8th Feb Batch\cmsjson.txt","w")
        json.dump(Customer.cus_list,f, default=Customer.convertToDict)
        f.close()

    @staticmethod
    def convertToObj(d):
        cus = Customer()
        cus.id = d['id']
        cus.name = d['name']
        cus.age = d['age']
        cus.mob_no = d['mob_no']
        return cus

    @staticmethod
    def loadFromJSON():
        f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python_12 PM_8th Feb Batch\cmsjson.txt", "r")
        Customer.cus_list = json.load(f,object_hook= Customer.convertToObj)
        f.close()



# BLL Ends Here