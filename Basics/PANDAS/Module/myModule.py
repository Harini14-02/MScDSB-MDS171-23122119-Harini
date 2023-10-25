# class student:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone

#     def printStudent(self):
#         print(self.name, self.phone)
    
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
        flag = 0
        breed = input("Enter the pet you want to adopt")
        name = input("Enter the name")
        for item in self.pet[breed]:
            if item == 'Not Sold':
                print("Not available for adoption",end='')
                flag=1
        if flag == 0:
            print("Thank you for the adoption",end='')

    def search(self):
        flag =0
        breed = input("Enter the pet you want to search")
        name = input("Enter the name")
        for item in self.pet[breed]:
                for i in item:
                    if i == name:
                        print("This breed is available - ",name)
                        flag = 1
                if flag == 0:
                    print("The breed is not available")



    # def store(self):
    #     name = input("enter the breed name")
    #     price = input("enter the price of the breed")
    #     self.pet
    #     self.price.append(price)
    #     print("Breed available for adoption ", self.breed)
    #     print("Price ", self.price)



a = petstore()
# a.display()
# a.search()
a.sell()
        
