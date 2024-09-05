
class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
        product = (self.name, self.weight, self.category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        strin_ = file.read()
        file.close()
        return f'{strin_}'

    def add(self, *products):
        for product in products:
            strin = Product.__str__(product)
            file = open(self.__file_name, 'r')
            if strin in file.read():
                print('Продукт ', strin, ' уже есть в магазине')
                file.close()
            else:
                file.close()
                file = open(self.__file_name, 'a')
                file.write(strin)
                file.write('\n')
            file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
# print(p1)
print(p2)  # __str__
# print(p3)
s1.add(p1, p2, p3)

print(s1.get_products())
