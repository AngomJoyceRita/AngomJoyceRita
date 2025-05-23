# Sample inventory with some items
stock = [
    {'name': 'Pen', 'qty': 100, 'price': 500},
    {'name': 'Notebook', 'qty': 50, 'price': 6000},
    {'name': 'Eraser', 'qty': 75, 'price': 300},
    {'name': 'Water', 'qty': 20, 'price': 1000},
]

# Function to add a new item to stock
def add_new_item():
    item_name = input("Enter item name: ").strip()
    for item in stock:
        if item['name'].lower() == item_name.lower():
            print("Item already in stock. Try updating instead.")
            return
    qty = int(input("Enter quantity: "))
    price = int(input("Enter price: "))
    stock.append({'name': item_name, 'qty': qty, 'price': price})
    print("Item added!")

# Function to show all items
def show_items():
    if not stock:
        print("Nothing in stock yet.")
        return
    print("\n--- Stock List ---")
    for item in stock:
        print(f"Name: {item['name']:<15} Qty: {item['qty']:<10} Price: UGX{item['price']}")

# Function to change quantity of an item
def change_quantity():
    item_name = input("Which item do you want to update? ").strip()
    for item in stock:
        if item['name'].lower() == item_name.lower():
            new_qty = int(input("Enter new quantity: "))
            item['qty'] = new_qty
            print("Updated successfully.")
            return
    print("Item not found.")

# Function to remove an item
def remove_item():
    item_name = input("Enter item name to delete: ").strip()
    for item in stock:
        if item['name'].lower() == item_name.lower():
            stock.remove(item)
            print("Item removed.")
            return
    print("Item not found.")

# Function to make an order
def make_order():
    item_name = input("Enter item to order: ").strip()
    for item in stock:
        if item['name'].lower() == item_name.lower():
            qty_needed = int(input("Enter quantity to order: "))
            if qty_needed <= 0:
                print("Enter a valid quantity.")
                return
            if qty_needed > item['qty']:
                print(f"Only {item['qty']} available.")
                return
            item['qty'] -= qty_needed
            total = qty_needed * item['price']
            print(f"Order successful! Total = UGX{total}")
            return
    print("Item not found.")

# Main menu 
def menu():
    while True:
        print("\n--- Inventory Menu ---")
        print("1. Show Items")
        print("2. Add New Item")
        print("3. Change Quantity")
        print("4. Remove Item")
        print("5. Make Order")
        print("6. Exit")

        choice = input("Choose (1-6): ").strip()

        if choice == '1':
            show_items()
        elif choice == '2':
            add_new_item()
        elif choice == '3':
            change_quantity()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            make_order()
        elif choice == '6':
            print("Bye!")
            break
        else:
            print("Invalid choice")

# Start the program
menu()
