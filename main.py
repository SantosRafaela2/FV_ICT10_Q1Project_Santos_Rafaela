# Miffy's Kitchen - Basic Food Ordering System (Console Version)
# This matches the items shown in your website.

def show_menu(menu):
    print("\n🍴 Welcome to Miffy's Kitchen 🍴")
    print("Here's our menu:\n")
    for i, (item, price) in enumerate(menu.items(), start=1):
        print(f"{i}. {item} - ₱{price}")
    print()

def take_order(menu):
    order_list = []
    total = 0

    while True:
        choice = input("Enter the item number to order (or 'done' to finish): ").strip().lower()
        if choice == 'done':
            break
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(menu):
                item = list(menu.keys())[choice - 1]
                price = menu[item]
                order_list.append(item)
                total += price
                print(f"Added {item} - ₱{price}")
            else:
                print("Invalid choice. Try again.")
        else:
            print("Please enter a valid number or 'done'.")

    return order_list, total

def customer_info():
    print("\n🧁 Please enter your details:")
    name = input("Name: ")
    address = input("Address: ")
    contact = input("Contact Number: ")
    return name, address, contact

def order_summary(name, address, contact, orders, total):
    print("\n✨ Order Summary ✨")
    print(f"👤 Name: {name}")
    print(f"🏠 Address: {address}")
    print(f"📞 Contact: {contact}")
    print("\n🛒 Items Ordered:")
    for item in orders:
        print(f" - {item}")
    print(f"\n💵 Total Amount: ₱{total}")
    print("\nThank you for ordering from Miffy's Kitchen! 🐰")

def main():
    menu = {
        "Bunny Pancakes": 120,
        "Miffy’s Macarons": 80,
        "Cloud Milk Tea": 90,
        "Carrot Cupcake": 70,
        "Pastel Spaghetti": 150,
        "Easter Egg Pie": 200,
        "Molten Lava Mud Cake": 250
    }

    show_menu(menu)
    orders, total = take_order(menu)
    if not orders:
        print("No items ordered. Come back soon!")
        return

    name, address, contact = customer_info()
    order_summary(name, address, contact, orders, total)

if __name__ == "__main__":
    main()
