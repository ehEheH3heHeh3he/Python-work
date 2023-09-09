class order:
    def __init__(self, table, order):
        self.table = table
        self.order = order
        
order1 = [order(1, 'latte'),order(2, 'americano')]

print(order1[0].order)