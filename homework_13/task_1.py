import csv


class Product:

    def __init__(self, product_name, product_type, price):
        self.prod_name = product_name
        self.prod_type = product_type
        self.price = price

    def __str__(self):
        return f'{self.prod_type}: {self.prod_name} - price:{self.price}.'

    def __repr__(self):
        return self.__str__()


class Store:

    def __init__(self):
        self.list_product = []
        self.balance = 0

    def add_product(self, raw, times=5):
        for num in range(times):
            self.list_product.extend([Product(raw['Наименование'], raw['Тип'], float(raw['Цена']))])
        return self.list_product

    def read_csv(self):
        with open('inventory.csv', 'r', encoding='utf-8') as file:
            file_reader = csv.DictReader(file, delimiter=',')
            for row in file_reader:
                self.add_product(row)

    def type_list(self, name_product):
        type_list = []
        for i in self.list_product:
            if name_product == i.prod_type:
                type_list.append(i)
            if name_product is None:
                type_list.append(i)
        return type_list

    def cost_products(self):
        cost_products = 0
        for prod in self.list_product:
            cost_products += prod.price
        return f'Общая стоимость продуктов: {self.cost_products} грн.'

    def sale_product(self, name: str):
        prod_index = None
        for i, prod in enumerate(self.list_product):
            if prod.prod_name == name:
                prod_index = i
                break
        if prod_index is not None:
            self.balance += self.list_product[prod_index].price
            self.list_product.pop(prod_index)
            print(f'{name} - продан')
        else:
            print('Нет в наличии')

    def balance(self):
        return self.balance


coffee_store = Store()
coffee_store.read_csv()
print(coffee_store.list_product)
print(coffee_store.cost_products())
coffee_store.sale_product('Доппио')
print(coffee_store.type_list('coffee'))
print(coffee_store.balance)