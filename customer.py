#Customer Profile
def profile(cid):
    with open('/Applications/python_bs/userList.txt', 'r') as f:
        data = f.readlines()
        print("My Account:")
        for line in data:
            words = line.split("|")
            if(cid == words[0]):
                print("Customer ID :"  + words[0])
                print("Customer First Name:" + words[1])
                print("Customer Last  Name:" + words[2])
                print("Customer Address:" + words[4])
        f.close()
    menu = str(input("Go to Customer Menu type yes or no:"))
    customer(menu,cid)
#Add New Deposit
def addDeposit(cid):
    dAmount = str(input("Enter Deposit Amount:"))
    bamount = str(dAmount)
    tType   = str("Deposit")
    TID     = str('1')
    # Get balanace amount
    with open('/Applications/python_bs/userTransaction.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            words = (line.split("|"))
            #balance
            if(cid == words[1]):
                oldbal  = int(words[5])
                bamount = oldbal + int(dAmount)
            #transaction id
            if(words[0]):
                oid = int(words[0])
                TID =  oid + 1
            
    withDrawal = str('0')
    #Add deposit amount to transaction txt
    with open('/Applications/python_bs/userTransaction.txt','a+') as File:
        if(File.write(str(TID)+"|"+str(cid)+"|"+tType+"|"+dAmount+"|"+withDrawal+"|"+str(bamount)+"\n")):
            print("Successfully Deposited")
            File.close()
            menu = str(input("Go to Customer Menu type yes or no:"))
            customer(menu,cid)
        else:
            print("Sorry! please try again")
            menu = str(input("Go to Customer Menu type yes or no:"))
            customer(menu,cid)
# Add New withdrawal
def addWithdrawal(cid):
    wAmount = str(input("Enter Withdrawal Amount:"))
    tType   = str("Withdrawal")
    TID     = int('0')
    # Get balanace amount
    with open('/Applications/python_bs/userTransaction.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            words = (line.split("|"))
        #balance
        if(cid == words[1]):
            oldbal  = int(words[5])
            if(oldbal > int(wAmount)):
                bamount = oldbal - int(wAmount)
                oid = int(words[0])
                TID =  oid + 1
    Deposit = str('0')
    #Add deposit amount to transaction txt
    if(TID):
        with open('/Applications/python_bs/userTransaction.txt','a+') as File:
            if(File.write(str(TID)+"|"+str(cid)+"|"+tType+"|"+Deposit+"|"+wAmount+"|"+str(bamount)+"\n")):
                print("Successfully Withdrawaled")
                File.close()
                menu = str(input("Go to Customer Menu type yes or no:"))
                customer(menu,cid)
            else:
                print("Sorry! please try again")
                menu = str(input("Go to Customer Menu type yes or no:"))
                customer(menu,cid)
    else:
        print("Sorry! Insufficient Funds")
        menu = str(input("Go to Customer Menu type yes or no:"))
        customer(menu,cid)
#Transaction List
def transactionList(cid):
    with open('/Applications/python_bs/userTransaction.txt', 'r') as f:
        data = f.readlines()
        print("Transaction List:")
        for line in data:
            words = (line.split("|"))
            if(cid == words[1]):
                print(words)
        f.close()
    menu = str(input("Go to Customer Menu type yes or no:"))
    customer(menu,cid)
#Transcation Search
def getTransaction(tid,cid):
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
    menu = str(input("Go to Customer Menu type yes or no:"))
    customer(menu,cid)
#Menu Activity 
def customerMenu(menu,cid):
    if(menu == 1):
        profile(cid)
    elif(menu == 2):
        addDeposit(cid)
    elif(menu == 3):
        addWithdrawal(cid)
    elif(menu == 4):
        transactionList(cid)
    elif(menu == 5):
        tid = str(input("Please enter Transaction ID:"))
        getTransaction(tid,cid)
    else:
        menu = "no"
        customer(menu,cid)
#Customer Menu
def customer(menu,cid):
    if(menu == "yes"):
        print("Welcome Customer")
        print("Banking System Menu:")
        print("1: My Account")
        print("2: Add New Deposit")
        print("3: Add New Withdrawal")
        print("4: Transaction List")
        print("5: Search Transaction")
        print("6: Logout")
        selection_value = int(input("Please select type of activity:"))
        customerMenu(selection_value,cid)
    else:
        exit
#Admin login
def userLogin(uid,uname,upass):
    with open('/Applications/python_bs/userList.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            words = line.split("|")
            cid   = words[0]
            cname = words[1]
            cpass = words[2]
            if(uid == cid and uname == cname and upass == cpass):
                menu = "yes"
                customer(menu,cid) 
        welcomePage()
#Welcome Page
def welcomePage():
    print("Welcome to Banking System")
    print("User Login")
    uid   = str(input("User ID:"))
    uname = str(input("Username:"))
    upass = str(input("Password:"))
    userLogin(uid,uname,upass)
welcomePage()