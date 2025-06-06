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
        price = self.items.get(item_name)
        if price is not None:
            return price
        else:
            print(f"Товар '{item_name}' не найден.")
            return None

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} обновлена на {new_price}")
        else:
            print(f"Товар {item_name} Невозможно обновить цену")

store1 = Store("Продукты", "ул. Мира, 15")
store2 = Store("Запчасти", "ул. Новая, 235")
store3 = Store("Косметика", "ул. Ленина, 96")

store1.add_item("Молоко", 120)
store1.add_item("Хлеб", 45)
store1.add_item("Яблоки", 60)

store2.add_item("Диски", 15300)
store2.add_item("Свеча зажигания", 220)
store2.add_item("Ремень", 4600)

store3.add_item("Крем для лица ночной", 1850)
store3.add_item("Крем для лица дневной", 1750)
store3.add_item("Средство для волос", 640)

store2.add_item("Масло трансмиссионное", 2700)
store2.update_price("Ремень", 5000)
store2.remove_item("Свеча зажигания")

price = store2.get_price("Диски")
print(f"\nЦена товара 'Диски': {price} руб.")

print("\nТекущий ассортимент магазина 'Запчасти':")
for item, price in store2.items.items():
    print(f"{item}: {price} руб.")

item_name = "Фильтр масляный"
price = store2.get_price(item_name)

















