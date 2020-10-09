
class Item:
    id = 0
    title = ''
    catagory = ''
    stock = 0
    prce = 0.0
    

    def __init__(self,id, title, cat, stock, price):
        self.id = id
        self.title =title
        self.catagory = cat
        self.stock = stock
        self.price = price