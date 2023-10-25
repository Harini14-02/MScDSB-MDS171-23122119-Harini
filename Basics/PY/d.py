class restaurant:
    def __init__(self,item,qty):
        self.item = item
        self.qty = qty
        self.menu = {
            "D1":20,
            "D2":30,
            "D3":40,
        }

    def totalcost(self):
        print("Totla cost of  the order")
        print("item\t",self.item)
        print("quantity\t",self.qty)
        total = self.qty * self.menu[self.item]
        print("total\t",total)


order = restaurant("D1",4)
order.totalcost()