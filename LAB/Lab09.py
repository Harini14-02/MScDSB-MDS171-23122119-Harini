class petstore:
    def __init__(self):
        self.pet = {
            "DOGS":[
                {"Pitbull":"Sold",
                 "German":"Not sold",
                 "Lab":"Sold"}],
            "CATS":[
                {"Abyssinian":"Sold",
                 "American Bobtail":"Not Sold",
                 "American Cu":"Sold"}],
            "FISH":[
                {"Koi":"Not Sold",
                 "Fighter":"Not Sold",
                 "Comet":"Not Sold"}],
        }

    def display(self):
        for key, val in self.pet.items():
            for i in val:
                print("{} : {}".format(key, i))
        print("---------------------------------------")
    
    def sell(self):
        flag =0
        breed = input("Enter the pet you want to search - ")
        name = input("Enter the name - ")
        for value in self.pet[breed]:
            for i in self.pet:
                if i == name:
                    print("This breed is available ",name)
                    flag = 1
            if flag == 0:
                print("The breed is not available")
            if value == 'Sold':
                print("Not available for adoption",end='')
                flag = 1
            if flag == 0:
                print("Thank you for the adoption \n",end='')

    def search(self):
        flag =0
        breed = input("Enter the pet you want to search - ")
        name = input("Enter the name - ")
        for item in self.pet[breed]:
                for i in item:
                    if i == name:
                        print("This breed is available ",name)
                        flag = 1
                if flag == 0:
                    print("The breed is not available")


    def store(self):
        my_dict = {}
        breed = input("Enter the breed - ")
        sold = input("Sold or Not Sold - ")
        my_dict['Breed']=breed
        my_dict['Availabilty']=sold
        print(my_dict)



a = petstore()
a.display()
a.search()
a.sell()
a.store()