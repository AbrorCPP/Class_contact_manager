class Product:
    def __init__(self, name, price,title):
        self.name = name
        self.price = price
        self.title = title

class Shop:
    def __init__(self, title, phone):
        self.title = title
        self.phone = phone
        self.baza = []

    def add_water(self):
        title = "water"
        price = input("price: ")
        name = input("Enter the name: ")
        p1 = Product(name, price, title)
        self.baza.append(p1)

    def add_food(self):
        title = "food"
        price = input("price: ")
        name = input("Enter the name: ")
        p2 = Product(name, price, title)
        self.baza.append(p2)

    def add_parfum(self):
        title = "parfum"
        price = input("price: ")
        name = input("Enter the name: ")
        p3 = Product(name, price, title)
        self.baza.append(p3)

    def view_food(self):
        title1 = input("Enter the title: ")
        for p in self.baza:
            if p.title == title1:
                print(f"Title: {p.title}, Price: {p.price}, Year: {p.name}")
        if title1 == "all":
            for item in self.baza:
                print(f"Title = {item.title} , Price = {item.price} , Year = {item.name}")

    def delete_product(self):
        name = input("Enter the name: ")
        for obj in self.baza:
            if name == obj.name:
                self.baza.remove(obj)

    def edit_food(self):
        name1 = input("Enter the name: ")
        for p in self.baza:
            if p.name == name1:
                name = input("Enter the new name: ")
                price = input("Enter the new price: ")
                title = p.title
                a = Product(name, price, title)
                self.baza.remove(p)
                self.baza.append(a)

shop1 = Shop("Shop Title", 12314214123)

def main(shop:Shop):
    while True:
        a = input(" 1.Add water\n 2.Add food\n 3.Add parfum\n 4.View food\n 5.Delete product\n 6.Edit food\n--->")
        if a == "1":
            shop.add_water()
        elif a == "2":
            shop.add_food()
        elif a == "3":
            shop.add_parfum()
        elif a == "4":
            shop.view_food()
        elif a == "5":
            shop.delete_product()
        elif a == "6":
            shop.edit_food()
        else:
            break

main(shop1)