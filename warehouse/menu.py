import os
import datetime


def print_menu():
    print("_"*50)
    print("Warehouse control"  +  get_date_time())
    print("-"* 50)

    print('[1] Register new Item')
    print('[2] Display catalog')
    print('[3] Display items out of stock')
    print('[4] stock value')
    print('[5] update price')
    print('[6] Delete an Item')
    print('[7] Update item Stock')
    print('[8] Select catagories')
    print('[9] Cheapest product')
    print('[10] 3 most expensive products')

    print('[X] Close')

def get_date_time():
    now = datetime.datetime.now()
    return now.strftime("%b/%d/%Y/%T")

def clear():
    command = ''
    if(os.name =='nt'):
        command = 'cls'
        return os.system(command)

    return os.system(command)
        # clear the console on python script


def print_item(item):
    print(
        str(item.id).rjust(3)
        + " | " + item.title.ljust(25)
        + " | " + item.catagory.ljust(12)
        + " | " + str(item.stock).rjust(11)
        + " | $" + str(item.price).rjust(15)
    )

def print_header(title):
    clear()
    print("-"*50)
    print(title)
    print("-"* 50)


    """
    1 - finish opc 4
    2 - clear the screen
    3 - Inv what is object serialization


    """
