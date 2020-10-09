"""
Program: Warehouse control
Author: Mesaye Addisu
Functionality:
    -Register Items
        - Id (auto generated): int
        -title: str
        -catagor: str
        -stock: int
        -price: float
"""


#imports
from menu import print_menu, clear, print_item, print_header
from item import Item
import pickle

# global vars
catalog =[]
last_id = 0
data_file = 'warhouse.data'


#functions

def serialize_catalog():
    global data_file
    writer = open(data_file,'wb') #wb => create/overwrite the file
    pickle.dump(catalog, writer)
    writer.close()
    print('Data saved!')

def deserialize_catalog():
    global data_file
    global last_id
    try:
        reader = open(data_file, 'rb')#rb => read binarry, throw wxwption if file does not exist
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last = catalog[-1]
        last_id = last.id + 1
        how_many = len(catalog)
        print('Deserealized # items'+ str(how_many)+'items' )
    except:
        print("Error, data not loaded")

def register_item():
    try:
        global last_id
        print_header("Register new Item")
        title = input('Plese provide the Title:')
        catagory = input('Please provide the Catagory:')
        stock = int(input('please provide the Stock:'))
        price = float(input('Please provide the Price'))

    except ValueError:
        print("*Error, provide valid numbers")

    except:
        print("*Error, verify data and try again!")



    the_item = Item(last_id, title, catagory, stock, price)
    last_id += 1
    catalog.append(the_item)

    count = len(catalog)
    print(" Item saved, you have" + str(count) + "items in your catalog")

def display_catalog():
    print_header("Your catalog")
    for item in catalog:
        print_item(item)

def display_out_or_stock():
    print_header("Items out of stock")
    for item in catalog:
        if(item.stock ==0):
            print_item(item)

def total_stock_value():
    print_header("Total stock value")
    total =0.0

    for item in catalog:
        total += item.stock * item.price

        print('Thetotal is: $'+ str(total))


def update_price():
    print_header("update price")
    id = input("choose an id")
    found = False
    for item in catalog:
        if (str(item.id) == id):
            found = True
            print('found it, its:' + item.title)
            price = float(input('Provide new Price$'))
            item.price = price

    if(not found):
         print("error, invalid ID.try again!")

def delete_item():
    display_catalog("")
    id = input('Please choose an id:')
    for item in catalog:
        if(str(item.id)== id):
            item.remove(item.catagory)
            print("Item removed")

def update_item_stock():
    display_catalog("")
    id = input("choose an id")
    for item in catalog:
        if(str(item.id) == id):
            found = True
            input(" new item stock")

        if(not found):
            print("invalid ID")


def select_catagory():
        print_header("Unique catagories")
        temp = []
        for item in catalog:
            if(not item.category in temp):
                temp.append(item.catagory)
                print(item.catagory)

def chepest_product():
        print_header()
        cheapest = catalog[0]

        for item in catalog:
            if (item.price < cheapest.price)
        print(item + item.price)
        cheapest = item

        print_item(chepest)

def three_most_expensive():
        prices = []
        for item in catalog:
            prices.append(item.price)

        prices.sort(reverse = True)

        print (prices[0]) #find the product that has the price,print_item(product)
        print (prices[1])
        print (prices[2])









"""

-show the catalog
-ask the user to chose an id
-find the id in the catalog
-   ask for the new price
-   set the price
-else, show an error

"""

#insturctions
deserialize_catalog()
input('Press enter to continue...')


opc = ''

while(opc != 'X'):
    clear()
    print_menu()
    opc= input('Please select an option:')

    if(opc ==  '1'):
        register_item
        serialize_catalog()

    elif(opc == '2'):
        display_catalog()

    elif( opc == '3'):
        display_out_or_stock()

    elif(opc == '4'):
        total_stock_value()

    elif(opc == '5'):
        update_price()

    elif(opc == '6'):
        delete_item()

    elif(opc == '7'):
        update_item_stock()

    elif(opc == '8'):
        select_catagory()

    elif(opc == '9'):
        cheapest_product()

    elif(opc == '10'):
        three_most_expensive()

    input('Press Enter to continue...')
