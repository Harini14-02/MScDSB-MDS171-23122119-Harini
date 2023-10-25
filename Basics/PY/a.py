listNames = []

def storenames(name):                              #to store the valus in the lsit
    name = name.strip().title()
    if name in listNames:
        return False
    else:
        listNames.append(name)
        return True
    
def displaynames():                                    #to print all the names present in the list
    print("*"*30)
    for name in listNames:
        print(name)
    print("*"*30)

def searchname():                               #to search the name in the list
    name = name.strip().title()
    flag = False
    for item in listNames:
        if name == item:
            flag = True
            break
    if flag == True:
        print("Name is in the list")
    else:
        print("Name does not exsist in the loop")
           

while True:                                         #to diplay the options
    print("Menu Options")
    print("*"*30)
    print("1. Enter a name")
    print("2. Search a name")
    print("3. List all name")
    print("4. Exit")

    choice = int(input("Enter your choice : "))             #get user input choice

    if choice == 1:
        userInp = input("Enter a name :")
        retval = storenames(userInp)
        if retval == True:
            print("Name is added to the list")
        else:
            print("Name exists in the list")
    
    elif choice == 2:
        userInp = input("Enter the name to be searched :")
        searchname(userInp)
    
    elif choice == 3:
        displaynames()

    elif choice == 4:
        exit()

    else:
        print("Invalid option !! Please select the correct option")