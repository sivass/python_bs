# Customer List
def userList():
    with open('/Applications/python_bs/userList.txt', 'r') as f:
        data = f.readlines()
        print("Customer List:")
        for line in data:
            words = line.split("|")
            print(words)
        f.close()
    menu = str(input("Go to Admin Menu type yes or no:"))
    admin(menu)
# Add New Customer
def addUser():
    cust_id    = str(input("Please enter new customer ID: "))
    if(cust_id):
        with open('/Applications/python_bs/userList.txt', 'r') as f:
            data = f.readlines()
            for line in data:
                words = line.split("|")
                if(cust_id == words[0]):
                    print("Sorry user ID already exit! please try new user id")
                    addUser()
                else:
                    cid = cust_id
    cust_name  = str(input("Please enter new customer name: "))
    cust_pass  = str(input("Please enter new customer password: "))
    cust_phone = str(input("Please enter new customer phone no: "))
    cust_addr  = str(input("Please enter new customer address: "))
    with open('/Applications/python_bs/userList.txt','a+') as File:
        # create = File.write(cust_id+"|"+cust_name+"|"+cust_pass+"|"+cust_phone+"|"+cust_addr+"\n")
        if(File.write(cid+"|"+cust_name+"|"+cust_pass+"|"+cust_phone+"|"+cust_addr+"\n")):
            print("Successfully customer created")
            File.close()
            userList()
            menu = str(input("Go to Admin Menu type yes or no:"))
            admin(menu)
        else:
            print("Sorry! please try again")
            addUser
# Specific customer detail
def getUser(uid):
    with open('/Applications/python_bs/userList.txt', 'r') as f:
        data = f.readlines()
        print("Customer Detail:")
        for line in data:
            words = line.split("|")
            if(uid == words[0]):
                print("Customer ID :"  + words[0])
                print("Customer First Name:" + words[1])
                print("Customer Last  Name:" + words[2])
                print("Customer Address:" + words[4])
        f.close()
    menu = str(input("Go to Admin Menu type yes or no:"))
    admin(menu)
#Transaction List
def transactionList():
    with open('/Applications/python_bs/userTransaction.txt', 'r') as f:
        data = f.readlines()
        print("Transaction List:")
        for line in data:
            words = (line.split("|"))
            print(words)
        f.close()
    menu = str(input("Go to Admin Menu type yes or no:"))
    admin(menu)
#Transcation Search
def getTransaction(tid):
    with open('/Applications/python_bs/userTransaction.txt', 'r') as f:
        data = f.readlines()
        print("Transaction Detail:")
        for line in data:
            words = line.split("|")
            if(tid == words[0]):
                print("Customer ID :"  + words[1])
                print("Transaction Type:" + words[2])
                print("Deposit Amount:" + words[3])
                print("Withdrawal Amount:" + words[4])
                print("Balance Amount:" + words[5])
        f.close()
    menu = str(input("Go to Admin Menu type yes or no:"))
    admin(menu)
#Admin Menu Section
def adminMenu(menu):
    if(menu == 1):
        userList()
    elif(menu == 2):
        addUser()
    elif(menu == 3):
        uid = str(input("Please enter user ID:"))
        getUser(uid)
    elif(menu == 4):
        transactionList()
    elif(menu == 5):
        tid = str(input("Please enter Transaction ID:"))
        getTransaction(tid)
    else:
        menu = "no"
        admin(menu)
#Admin
def admin(menu):
    if(menu == "yes"):
        print("Welcome Admin")
        print("Banking System Menu:")
        print("1: Customer List")
        print("2: Add New Customer")
        print("3: Search Customer")
        print("4: Transaction List")
        print("5: Search Transaction")
        print("6: Logout")
        selection_value = int(input("Please select type of activity:"))
        adminMenu(selection_value)
    else:
        welcomePage()
#Admin login
def adminLogin(uname,upass):
    if(uname == "Admin" and upass == "Admin12345"):
        menu = "yes"
        admin(menu) 
    else:
        welcomePage()
#Welcome Page
def welcomePage():
    print("Welcome to Banking System")
    print("Admin Login")
    uname = str(input("Username:"))
    upass = str(input("Password:"))
    adminLogin(uname,upass)
welcomePage()