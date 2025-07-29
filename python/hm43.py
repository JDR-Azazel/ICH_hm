"""
Создайте программу, которая подключается к MongoDB и:
- выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
- очищает коллекцию перед началом
- добавляет 3 товара с полями: name, price, stock
- выводит сообщение о количестве добавленных товаров

Пример вывода:
3 products inserted.
"""

from pymongo import MongoClient


client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)


db = client["ich_edit"]
collection_name = "products_210225_ptm_daniil_boiko"
products_collection = db[collection_name]

products_collection.delete_many({})

products = [
    {"name": "Laptop", "price": 999.99, "stock": 10},
    {"name": "Keyboard", "price": 49.99, "stock": 25},
    {"name": "Mouse", "price": 19.99, "stock": 30}
]

result = products_collection.insert_many(products)

print(f"{len(result.inserted_ids)} products inserted.")

#print("\nAll products in collection:")
#for product in products_collection.find():
#    print(f"- {product['name']}: ${product['price']} ({product['stock']} in stock)")

"""
Продолжите предыдущую задачу. Теперь программа должна:
- увеличить цену всех товаров на 20%
- вывести количество обновлённых записей
- затем вывести список всех товаров с новыми ценами

Пример вывода: 
Prices updated for 3 products.
Updated products:
- Pen — $1.80
- Notebook — $4.79
- Backpack — $30.00
"""

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)

db = client["ich_edit"]
collection_name = "products_210225_ptm_daniil_boiko"
products_collection = db[collection_name]

result = products_collection.update_many(
    {},
    {"$mul": {"price": 1.2}}
)

print(f"Prices updated for {result.modified_count} products.")
print("Updated products:")

for product in products_collection.find():
    print(f"- {product['name']} — ${product['price']:.2f}")
