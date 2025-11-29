#Create & Display Menu — Bhanu Prakash

menu = {
    1: ["Cheese Maggi", 110],
    2: ["Samosa", 50],
    3: ["Chicken Sandwich", 180],
    4: ["Filter Coffee", 80],
    5: ["Cappuccino", 150],
    6: ["Masala Chai", 40],
    7: ["Mango Juice", 40],
    8: ["Orange Juice", 35],
    9: ["Butterscotch Ice Cream", 60],
    10: ["Chocolate Ice Cream", 55]
}

print("Welcome to Campus Food Hub")
print("Your Friendly College Canteen\n")

print("Menu:")
for num, item in menu.items():
    print(num, "-", item[0], "₹", item[1])


# Take Customer Order - Chirag

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

#Generate Bill — Manikanta & Sai Mohith



#Save Bill to Text File — Chandrakala
