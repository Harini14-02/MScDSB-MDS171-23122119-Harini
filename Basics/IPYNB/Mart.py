class studentdetail:
    def __init__(self):
        self.details=[]
    def storedetails(self,name,regno,age):
        details={
            "Name":name,
            "Regno":regno,
            "Age":age
        }
        self.details.append(details)
    def displaydetails(self):
        for data in self.details:
            print(data)
    def searchdetail(self):
        flag =0
        for data in self.details:
            if data["Name"] == abc:
                print("Details for this exists")
                print(data["Name"])
                flag=1
        if flag == 0:
            print("Details for this Name does not exist...")
hii=studentdetail()
while True:
    print("Menu","\n","1.store details","\n","2.Display the details","\n","3.search name","\n","4.Exit")
    n=input("enter a number b/w 1 to 4")
    if n == "1":
        name =input("enter a name")
        regno=input("enter regno num")
        age =input("enter your age")
        hii.storedetails(name,regno,age)
        print("Details added successfully...")
    elif n == "2":
        print("here are the details")
        hii.displaydetails()
    elif n=="3":
        abc =input("enter a name")
        hii.searchdetail()
    elif n =="4":
        break
    else:
        print("enter a valid option")  