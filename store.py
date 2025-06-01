class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

def add_item(self, item_name, price):
    self.items[item_name] = price
    print(f"Товар{item_name}добавлен, цена {price}")

def remove_item(self, item_name):
    if item_name in self.items:
        del self.items[item_name]
        print(f"Товар {item_name} удален")
    else:
        print(f"Товар {item_name} не найден")

def get_price(self, item_name):
    return self.items.get(item_name)

def update_price(self, item_name, new_price):
    if item_name in self.items:
        self.items[item_name] = new_price
        print(f"Цена товара {item_name} обновлена на {new_price}")
    else:
        print(f"Товар {item_name} Невозможно обновить цену")

store1 = Store("Продукты", ул. Мира, 15)
store2 = Store("Запчасти", ул. Новая, 235)
store3 = Store("Косметика", ул. Ленина, 96)

store1.add_item("Молоко", 120)
store1.add_item("Хлеб", 45)
store1.add_item("Яблоки", 60)










