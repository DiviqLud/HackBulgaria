class Product:
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, disk_space, RAM):
        super().__init__(name, stock_price, final_price)
        self.disk_space = disk_space
        self.RAM = RAM


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, dis_size, dis_pixel):
        super().__init__(name, stock_price, final_price)
        self.dis_size = dis_size
        self.dis_pixel = dis_pixel


class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.total_profit = 0

    def load_new_products(self, product, count):
        self.products[product] = count

    def list_products(self, product_class):
        for product in self.products:
            if isinstance(product, product_class):
                print(product_class.name + ' - ' + str(self.products[product_class]))

    def sell_product(self, product):
        if self.products[product] != 0:
            self.products[product] -= 1
            self.total_profit += product.profit()
            return True
        else:
            return False

    def total_income(self):
        return self.total_profit

store = Store('Laptop.bg')
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
store.load_new_products(smarthphone, 2)
store.sell_product(smarthphone)  # True
store.sell_product(smarthphone)  # True

print(store.total_income())  # 640
