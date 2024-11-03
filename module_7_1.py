class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file1 = open(self.__file_name, 'r')
        product = file1.read()
        file1.close()
        return product

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        for pro in products:
            if str(pro) in self.get_products():
                print(f"Продукт {str(pro)} уже есть в магазине")
            else:
                file.write(str(pro) + '\n')
        file.close()


class Product(Shop):
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Rice', 6.1, 'Groceries')

print(p4)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())