



def negative_this(amnt_in):
    amnt_out = 0
    amnt_out = (amnt_in * (-1))
    return amnt_out

def enter_amount():
    amnt_in = int(input("Enter the amount:"))
    return amnt_in

def enter_cat_in():
    cat_in = int(input('which category you want to deposit the money in?\n1.Food.\n2.Entertainment\n3.Clothes:' ))
    return cat_in

    
def enter_cat_out():
    cat_out = int(input("Which category you want to withdraw money from?\n1.Food.\n2.Entertainment\n3.Clothes:\n"))
    return cat_out

def error_hndl(products_list):
    for x in products_list:
        if x.amount < 0:
            print(">>>>>>There is NOT enough funds for the selected transaction.\nExiting>>>>>>>")
        else: 
            return True




      





        
        


