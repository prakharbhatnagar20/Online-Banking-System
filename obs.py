def import_and_create_bank(filename):

    bank = {}

    # your code here
    f = open(filename,'r')
    lines = f.readlines()
    for line in lines:
        lst = line.strip().split(':')
        if len(lst)<=1:
            continue
        key = lst[0].strip()
        value = lst[1].strip()
        try:
            value = float(value)
            bank[key] = bank.get(key, 0) + value
        except:
            continue
        
    f.close()

    return bank
def signup(user_accounts, log_in, username, password):


    # your code here
    uslist=list(user_accounts.keys())
    up=0
    lo=0
    nu=0
    if username in uslist:
        return False
    if username==password:
        return False
    if len(password)>=8:
        for i in password:
            if i.isupper():
                up+=1
            elif i.isdigit():
                nu+=1
            elif i.islower():
                lo+=1
    else:
        return False
            
    if up==0 or lo==0 or nu==0:
        return False
    user_accounts[username]=password
    log_in[username]=False
    return True
    
 
    
        
def valid_pass(username,password):
    up=0
    lo=0
    nu=0
    if username==password:
        return False
    if len(password)>=8:
        for i in password:
            if i.isupper():
                up+=1
            elif i.isdigit():
                nu+=1
            elif i.islower():
                lo+=1
    else:
        return False
            
    if up==0 or lo==0 or nu==0:
        return False
    
    return True

def import_and_create_accounts(filename):
  
    user_accounts = {}
    log_in = {}

    # your code here
    f = open(filename,'r')
    lines = f.readlines()
    for line in lines:
        lst = line.strip().split('-')
        if len(lst)<=1:
            continue
        username = lst[0].strip()
        password = lst[1].strip()
        


        
        signup(user_accounts, log_in, username, password)    
    f.close()
    
    

    return user_accounts,log_in
def login(user_accounts, log_in, username, password):
   
    uslist=list(user_accounts.keys())
    if username in uslist:
        if password==user_accounts[username]:
            log_in[username]=True
            return True
    return False
def update(bank, log_in, username, amount):

    # your code here
    if username not in bank:
        bank[username]=0
    if log_in[username]==True:
        a=bank[username]+amount
        if a<0:
            return False
        else:
            bank[username]=a
            return True
    else:
        return False
        
def transfer(bank, log_in, userA, userB, amount):

    # your code here
   
    if (userA not in bank) or (userA not in log_in):
        return False
    if userB not in log_in:
        return False
    
    if userB not in bank:
        bank[userB]=0
    if log_in[userA]==True:
        a=bank[userA]-amount
        if a<0:
            return False
        else:
            bank[userA]=a
    else:
        return False
    b=bank[userB]+amount
    bank[userB]=b
    return True

def change_password(user_accounts, log_in, username, old_password, new_password):

    
    # your code here
    if (username in user_accounts) and (log_in[username]==True) and (user_accounts[username]==old_password) and (old_password!=new_password) and valid_pass(username,new_password):
        user_accounts[username]=new_password
        return True
    return False

def delete_account(user_accounts, log_in, bank, username, password):
   

    # your code here
    if (username in user_accounts) and (log_in[username]==True) and (user_accounts[username]==password):
        del user_accounts[username]
        del log_in[username]
        del bank[username]
        return True
    return False
    
def main():
    

    bank = import_and_create_bank("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        # for debugging
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to login
            login(user_accounts, log_in, username, password);
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to signup
            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            # add code to change password
            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to delete account
            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break;
        else:
            print("The option is not valid. Please re-enter the option.\n")

#This will automatically run the main function in your program
#Don't change this
if __name__ == '__main__':
    main()
        
    
                  
    
    