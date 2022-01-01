import functions_lib as fnc
import ast
import time
import json

from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./database.txt")
with open(file_path, 'r') as data:
  dictionary = ast.literal_eval(data.read())



class Service:
    def __init__(self, serv_code, cat_code_in=0, cat_code_out=0, am_in = 0, am_out = 0): #serv_code changes to whatever value the chosen category is (food, clothes )
        self.serv_code = serv_code
        self.cat_code_in = cat_code_in
        self.cat_code_out = cat_code_out
        self.am_in = am_in
        self.am_out = am_out


class Product:
    def __init__(self, cat_code = int, amount = 0):
        self.cat_code = cat_code
        self.amount = amount

food = Product(1)
enter = Product(2)
clothes = Product(3)

#saving the current amount saved on file and making a list
food.amount = dictionary.get("food")
enter.amount = dictionary.get("entertainment")
clothes.amount = dictionary.get("clothes")
products_list = [food, enter, clothes]


#srv_code id's what service is selected
sv_deposit = Service(1)
sv_withdraw = Service(2)
sv_transfer = Service(3)
sv_balance = Service(4)



service_list = [sv_deposit, sv_withdraw, sv_transfer, sv_balance] 
def service_chsn(select_srv):    
    for x in service_list: 
        if (x.serv_code) == select_srv:
            return select_srv

def main_menu():
    print ("\n\nWelcome to BudgetApp.")
    select_srv = int(input ("\nPlease enter the number for the service you want to use:\n1.Deposit\n2.Withdraw\n3.Move Funds Between Categories\n4.Check your balance:\n\nEnter the number:"))
    service_chsn(select_srv)
    deposit(select_srv)

def deposit(select_srv):
    if select_srv == 1:
        cat_out = 0
        cat_in = fnc.enter_cat_in()
        amnt_in  = fnc.enter_amount()
        amnt_out = 0
    elif select_srv == 2:
        cat_in = 0
        cat_out = fnc.enter_cat_out()  
        amnt_in = fnc.enter_amount()
        amnt_out = fnc.negative_this(amnt_in)
        amnt_in = 0
    elif select_srv == 3:
        cat_out = fnc.enter_cat_out()  
        amnt_in = fnc.enter_amount()
        cat_in = fnc.enter_cat_in()  
        amnt_out = fnc.negative_this(amnt_in)
    elif select_srv == 4:
        balance()
        

    
        
    products_chsn(cat_in, cat_out, amnt_in, amnt_out)



def products_chsn(cat_in, cat_out, amnt_in, amnt_out):
    for x in products_list:
        if (x.cat_code) == cat_in:
            x.amount += amnt_in
        elif (x.cat_code) == cat_out:
            x.amount += amnt_out
        else: 
            continue
        print(f'new amount: {x.amount} category: {x.cat_code}')
        fnc.error_hndl(products_list)
        if fnc.error_hndl(products_list) == True:
            write_file(dictionary)


def write_file(dictionary):
    # dictionary
    dictionary['food']= food.amount
    dictionary['entertainment'] = enter.amount
    dictionary['clothes'] =clothes.amount
    with open('./database.txt', "w") as myfile:
        myfile.write(json.dumps(dictionary))  


def balance():
                print ('\n\nThis is your current balance by category:' )
                print(f'Food: {food.amount} \nEntertainment: {enter.amount} \nClothes: {clothes.amount}')
                time.sleep(5)
                back_menu =str(input('\nReturn to Main Menu? Press Y for yes, N to exit:\n'))
                if back_menu == ("Y" or "y"):
                    main_menu() 
                else:
                    print("Exiting...") 
                    time.sleep(3) 
                    exit()  
             
   


main_menu()




 














