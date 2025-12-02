import os
import re

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


def show_welcome_and_menu():
    print("Welcome to Campus Food Hub")
    print("Your Friendly College Canteen\n")
    print("Menu:")
    for num, item in menu.items():
        print(num, "-", item[0], "₹", item[1])
    print(
        "\nPlease enter the item number from the menu to add it to your order.\n"
        "Type 'done' when you are finished.\n"
    )


def take_order():
    order = []

    while True:
        choice = input("Enter item number (or 'done' to place your order): ").strip()

        if choice.lower() == "done":
            break

        # validate item number using regex
        if not re.fullmatch(r"\d+", choice):
            print("That doesn’t look like a valid item number. "
                  "Please enter a number from the menu, for example 1, 2 or 3.\n")
            continue

        choice_num = int(choice)

        if choice_num not in menu:
            print("We couldn’t find that item. "
                  "Please choose an item number from the menu shown above.\n")
            continue

        #quantity loop
        while True:
            qty_input = input("Enter quantity: ").strip()

            if not re.fullmatch(r"\d+", qty_input):
                print("Quantity should be a whole number, like 1, 2 or 3. "
                      "Please try again.\n")
                continue

            quantity = int(qty_input)

            if quantity <= 0:
                print("Quantity must be at least 1. "
                      "Please update the quantity and try again.\n")
                continue

            # valid quantity -> exit this inner loop
            break
        #end quantity loop

        item_name = menu[choice_num][0]
        unit_price = menu[choice_num][1]
        line_total = unit_price * quantity

        order.append([item_name, quantity, unit_price, line_total])
        print(f"Added {quantity} x {item_name} to your order.\n")

    return order


def calculate_and_show_bill(order):
    print("\nYour Order Summary:")
    subtotal = 0
    for item in order:
        print(f"{item[0]} x {item[1]} = {item[3]}")
        subtotal += item[3]

    gst = round(subtotal * 0.05, 2)
    grand_total = round(subtotal + gst, 2)

    print("\nSubtotal:", subtotal)
    print("GST @ 5%:", gst)
    print("Amount Payable:", grand_total)

    return subtotal, gst, grand_total


def get_next_bill_filename():
    bill_no = 1
    while True:
        filename = f"bill{bill_no}.txt"
        if not os.path.exists(filename):
            return filename
        bill_no += 1


def save_bill(order, subtotal, gst, grand_total):
    filename = get_next_bill_filename()

    with open(filename, "w") as file:
        file.write("Campus Food Hub\n")
        file.write("Your Friendly College Canteen\n\n")
        file.write("===== BILL =====\n")
        for item in order:
            file.write(f"{item[0]}  {item[1]} qty x {item[2]} = {item[3]}\n")
        file.write("\nSubtotal = " + str(subtotal))
        file.write("\nGST 5% = " + str(gst))
        file.write("\nGrand Total = " + str(grand_total) + "\n")

    print(f"\nYour bill has been saved as '{filename}'.")
    print("Thank you for ordering from Campus Food Hub!")


def main():
    show_welcome_and_menu()
    order = take_order()

    if not order:
        print("\nYou didn’t add any items to your order.")
        print("Thank you for visiting Campus Food Hub. See you next time!")
        return

    subtotal, gst, grand_total = calculate_and_show_bill(order)
    save_bill(order, subtotal, gst, grand_total)


if __name__ == "__main__":
    main()
