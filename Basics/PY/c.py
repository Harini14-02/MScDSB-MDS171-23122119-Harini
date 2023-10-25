# # class MSCDS:
# #     def __init__(self):
# #         #Data Members/ Properties/ Attributes
# #         self.name = "MSC DS B"
# #         self.student = ["A","B","C"]
    
# #     def display(self): #Member function
# #         for students in self.student:
# #             print(students)

# # obj = MSCDS()
# # print(obj.name,obj.student)
# # obj.display()

# # class color:
# #     def __init__(self, a, b):
# #         self.name = a
# #         self.thing = b

# # red = color("RED","BLOOD")
# # print()


# # class car:
# #     def __init__(self, a, b, c):
# #         self.manufacturer = a
# #         self.model = b
# #         self.year = c
    
# #     def __str__(self):
# #         return self.manufacturer
    
# # bmw = car("BMW","I Series",202)
# # dodge = car("Dodge","Challenger",2020)
# # print(bmw.manufacturer)
# # print(dodge.model)


# #create a class restaurant that accepts items and quantity as input 
# # inside your class you are having the item and its price as a dictionary 
# # create a fuction to calculate the totalcost then print the itemname, qty and price 

# class restaurant:
#     def __init__(self,item,qty):
#         self.item = item
#         self.qty = qty
#         self.menu = {
#             "D1":20,
#             "D2":30,
#             "D3":40,
#         }

#     def totalcost(self):
#         print("Totla cost of  the order")
#         print("item\t",self.item)
#         print("quantity\t",self.qty)
#         total = self.qty * self.menu[self.item]
#         print("total\t",total)

# order = restaurant("D1",4)
# order.totalcost()

# define a class expense tracker that stores the expense and income in a dictionary 
# implement the method to store the transaction, view the transaction, calculate the total expenses/income

# define a class expense tracker that stores the
# expenses and income in a dictionary
# implement the method to
# - store the transaction;
# - view transactions;
# - calculate the total expense/income
# def fileOpen(): #function to initiate a new file and write column header
#     file=open("expense.txt","w+")

# def fileWrite(amt, category, details): #function to write user input in data
#     file=open("order details.txt","a+")
#     file.write(amt,category,details)
#     file.close()
#     return True

class expenseTracker:
    def __init__(self):
        self.expenseDict = {
            "income": [],
            "expense": [],
        }

    def store_transactions(self, type, amt, category, date, details):
        trans = {
            "Amount": amt,
            "Category": category,
            "Date": date,
            "Details": details,
        }
        if type == "income":
            self.expenseDict['income'].append(trans)
        else:
            self.expenseDict['expense'].append(trans)

    def view_transactions(self):
        print("Your Income:")
        for item in self.expenseDict['income']:
            print(item)
        print("Your Expenses:")
        for item in self.expenseDict['expense']:
            print(item)

    def calculate_transactions(self):
        total_income = 0
        for item in self.expenseDict['income']:
            total_income += item["Amount"]
        print("Total Income\t:\t", total_income)

        total_expense = 0
        for item in self.expenseDict['expense']:
            total_expense += item["Amount"]
        print("Total Expenses\t:\t", total_expense)

# define a menu that will let users to enter expense, view expenses
# or income, get totals in each and exit from the program


def collectInput():
    amt = int(input("Enter the amout: "))
    category = input("Enter Category: ")
    date = input("Enter Date (DD/MM/YYYY): ")
    details = input("Enter description: ")
    return amt, category, date, details


myexpense = expenseTracker()

while True:
    print("...MY EXPENSE TRACKER...")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Records")
    print("4. View My Spendings")
    print("5. Exit")

    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        print("Enter the details of income")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("income", amt, category, date, details)
    elif choice == 2:
        print("Enter the details of expense")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("expense", amt, category, date, details)
    elif choice == 3:
        myexpense.view_transactions()
    elif choice == 4:
        myexpense.calculate_transactions()
    elif choice == 5:
        exit()
    else:
        print("In valid choice")


    




    

# Create a method in the class
# to export the details in the form of csv
# add export details to the file in the menu option
    

    

