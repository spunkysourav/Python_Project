#Calculator using class
#BLL Start
class Calculator:
    def __init__(self):
        self.no1=0
        self.no2=0
        self.res=0
    def add(self):
        self.res=self.no1+self.no2
    def sub(self):
        self.res=self.no1-self.no2
    def mul(self):
        self.res=self.no1*self.no2
    def div(self):
        self.res=self.no1/self.no2
#BLL End
#PL Start
while(True):
    print("Press 1 for ADDITION \nPress 2 for SUBTRACTION \nPress 3 for MULTIPLICATION \nPress 4 for DIVISION")
    ch=int(input("Press Number: "))
    if ch==1:
        ob=Calculator()
        ob.no1=int(input("Enter Number: "))
        ob.no2=int(input("Enter Number: "))
        ob.add()
        print("Result: ",ob.res)
    elif ch==2:
        ob=Calculator()
        ob.no1=int(input("Enter Number: "))
        ob.no2=int(input("Enter Number: "))
        ob.sub()
        print("Result: ",ob.res)
    elif ch==3:
        ob=Calculator()
        ob.no1=int(input("Enter Number: "))
        ob.no2=int(input("Enter Number: "))
        ob.mul()
        print("Result: ",ob.res)
    elif ch==4:
        ob=Calculator()
        ob.no1=int(input("Enter Number: "))
        ob.no2=int(input("Enter Number: "))
        ob.div()
        print("Result: ",ob.res)
    elif ch==0:
        print("!!Please Select Correct Number!!")
    else:
        ch>4
        print("!!Wrong Selection!!")
        break
#PL End