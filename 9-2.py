import json

with open('products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

new_name = input("Введите название продукта: ")
new_price = int(input("Введите цену: "))
new_weight = int(input("Введите вес: "))
new_available = input("В наличии? (да/нет): ").strip().lower()

is_available = True if new_available == 'да' else False

data['products'].append({
    "name": new_name,
    "price": new_price,
    "available": is_available,
    "weight": new_weight
})

with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    
    if product['available']:
        print("В наличии\n")
    else:
        print("Нет в наличии!\n")
