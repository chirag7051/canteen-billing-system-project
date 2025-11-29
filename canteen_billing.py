    ## developing a canteen menu code -- Bhanu Prakash.

menu = {
    "Snacks": [
        {"name": "Cheese Maggi", "cost": 110, "type": "Veg"},
        {"name": "Samosa", "cost": 50, "type": "Veg"},
        {"name": "Chicken Sandwich", "cost": 180, "type": "Non-Veg"}
    ],
    "Hot Beverages": [
        {"name": "Filter Coffee", "cost": 80, "volume": "200ML"},
        {"name": "Cappuccino", "cost": 150, "volume": "250ML"},
        {"name": "Masala Chai", "cost": 40, "volume": "180ML"}
    ],
    "Ice Creams and Drinks": [
        {"name": "Mango Juice", "cost": 40, "volume": "200ML"},
        {"name": "Orange Juice", "cost": 35, "volume": "200ML"},
        {"name": "Butterscotch Ice Cream Tub", "cost": 60, "volume": "250ML"},
        {"name": "Chocolate Ice Cream Tub", "cost": 55, "volume": "200ML"}
    ]
}
print("Welcome to the Canteen Menu!")

## next step is select item from the category.




# Take Order - Chirag

print("\nPlease enter the item number from the menu to add it to your order. Type 'done' when you are finished.\n")
order = []
while True:
    choice = input("Enter item number (or 'done'): ")
    if choice.lower() == "done":
        break
    if not choice.isdigit():
        print("Invalid input! Enter a number.")
        continue
    choice = int(choice)
    if choice not in menu:
        print("Invalid item number! Try again.")
        continue
    quantity = input("Enter quantity: ")
    if not quantity.isdigit():
        print("Quantity must be a number!")
        continue
    quantity = int(quantity)
    if quantity <= 0:
        print("Quantity must be greater than 0!")
        continue
    price = menu[choice][1] * quantity
    order.append([menu[choice][0], quantity, menu[choice][1], price])
    print("Added!\n")
