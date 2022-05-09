products = [
    {
        "name": "apple",
        "category": "fruit",
        "price": 4.3,
    },
    {
        "name": "Croissant",
        "category": "bakery",
        "price": 1.3,
    },
    {
        "name": "Salmon",
        "category": "fish",
        "price": 15.00
    },
    {
        "name": "Soda Max",
        "category": "beverages",
        "price": 0.8
    },
    {
        "name": "Beer",
        "category": "beverages",
        "price": 1
    }
]

if __name__ == '__main__':
    prod_category = input('Enter the product category')
    discount = float(input('enter discount to apply'))
    for item in products:
        if item["category"] == prod_category:
            new_price = float(item["price"]) - (float(item["price"]) * discount / 100)
            print(f'{item["name"]} : {new_price}')
