#BLL Start
import pymysql
class Customer:
    con=pymysql.connect(host='localhost', users='root', password='Python', database='cusdb')
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mobile_no=""
    def checkID(self,id):
        for e in Customer.list_cus:
            if e.id==id:
                raise Exception("Oops! ID Already Present!")
    def __str__(self):
        return "Customer Details:- Id: {0}, Name: {1}, Address: {2}, Mobile No: {3}".format(self.id, self.name, self.address, self.mobile_no)
    def add_customer(self):
        myCursor=Customer.con.cursor()
        strQuery="insert into customer values(%s,%s,%s,%s)"
        myCursor.execute(strQuery, (self.id, self.name, self.address, self.mobile_no))
        Customer.con.commit()
    def search_customer(self,id):
        myCursor = Customer.con.cursor()
        strQuery = "select * from customer where id=%s"
        rowaffected=myCursor.execute(strQuery, (id,))
        if rowaffected==0:
            raise Exception("Oops! ID Not Found!")
        else:
            row=myCursor.fetchone()
            self.id=row[0]
            self.name=row[1]
            self.address=row[2]
            self.mobile_no=row[3]
    def modify_customer(self,id):
        myCursor=Customer.con.cursor()
        strQuery="update  customer set name=%s,address=%s,mobileno=%s where id=%s"
        rowaffected=myCursor.execute(strQuery, (self.name,self.address,self.mobile_no,id,))
        if rowaffected==0:
            raise Exception("Oops! ID Not Found!")
        else:
            Customer.con.commit()
    def delete_customer(self,id):
        myCursor = Customer.con.cursor()
        strQuery = "delete from customer where id=%s"
        rowaffected = myCursor.execute(strQuery, (id,))
        if rowaffected==0:
            raise Exception("Oops! ID Not Found!")
        else:
            Customer.con.commit()
    @staticmethod
    def get_all_customer():
        return Customer.list_cus
#BLL End

#PL Start
if __name__ =="__main__":
    def show_all_customer():
        allCus=Customer.get_all_customer()
        print("*"*50)
        for cus in allCus:
            print(cus)
        print("*"*50)
    while (True):
        print("Choose 1 to Add Customer \nChoose 2 to Search Customer \nChoose 3 to Modify Customer \nChoose 4 to Delete Customer \nChoose 0 to Exit")
        ch=input("Enter Choice: ")
        if ch=='1':
            try:
                cus=Customer()
                cus.id=int(input("Enter Id: "))
                cus.name=input("Enter Name: ")
                cus.address=input("Enter Address: ")
                cus.mobile_no=input("Enter Mobile_No.: ")
                cus.add_customer()
                print("Customer Added Successfully!")
            except Exception as ex:
                print(ex)
        elif ch=='2':
            try:
                cus=Customer()
                id=int(input("Enter Id: "))
                cus.search_customer(id)
                print("*"*50)
                print(cus)
                print("*"*50)
            except Exception as ex:
                print(ex)
        elif ch=='3':
            try:
                cus=Customer()
                cus.id=int(input("Enter Id: "))
                cus.name=input("Enter Name: ")
                cus.address=input("Enter Address: ")
                cus.mobile_no=input("Enter Mobile_No.: ")
                cus.modify_customer(cus.id)
                print("Customer Modified Successfully!")
            except Exception as ex:
                print(ex)
        elif ch=='4':
            try:
                cus=Customer()
                id=int(input("Enter ID"))
                cus.delete_customer(id)
                print("Customer Deleted Successfully!")
            except Exception as ex:
                print(ex)
        elif ch=='0':
            print("Exit Successful!")
            break
#PL End