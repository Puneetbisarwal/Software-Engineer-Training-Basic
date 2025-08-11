import json
import os

# ====== Data Persistence ======
INVENTORY_FILE = "inventory.json"

def load_inventory():
    """Load inventory from JSON file."""
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    return {}

def save_inventory(inventory):
    """Save inventory to JSON file."""
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)

# ====== Core Functions ======
def add_item(inventory, item_id, name, category, quantity, price):
    """Add a new item to inventory."""
    inventory[item_id] = {
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price
    }
    print(f"✅ Item '{name}' added successfully!")

def remove_item(inventory, item_id):
    """Remove an item from inventory."""
    if item_id in inventory:
        removed_item = inventory.pop(item_id)
        print(f"🗑️ Item '{removed_item['name']}' removed.")
    else:
        print("❌ Item ID not found.")

def update_quantity(inventory, item_id, quantity):
    """Update the quantity of an item."""
    if item_id in inventory:
        inventory[item_id]["quantity"] = quantity
        print(f"✏️ Quantity updated for '{inventory[item_id]['name']}'.")
    else:
        print("❌ Item ID not found.")

def search_item(inventory, keyword):
    """Search for items by name or category."""
    found = False
    for item_id, details in inventory.items():
        if keyword.lower() in details["name"].lower() or keyword.lower() in details["category"].lower():
            print(f"🔍 Found: {item_id} - {details}")
            found = True
    if not found:
        print("No matching items found.")

def inventory_report(inventory):
    """Display full inventory and low-stock alerts."""
    print("\n📦 Inventory Report:")
    for item_id, details in inventory.items():
        print(f"{item_id}: {details}")
        if details["quantity"] < 5:
            print("⚠️ Low stock alert!")

# ====== Main Program ======
def main():
    inventory = load_inventory()

    while True:
        print("\n=== Inventory Management Menu ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. Search Item")
        print("5. Inventory Report")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            item_id = input("Enter item ID: ")
            name = input("Enter item name: ")
            category = input("Enter category: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_item(inventory, item_id, name, category, quantity, price)

        elif choice == "2":
            item_id = input("Enter item ID to remove: ")
            remove_item(inventory, item_id)

        elif choice == "3":
            item_id = input("Enter item ID to update: ")
            quantity = int(input("Enter new quantity: "))
            update_quantity(inventory, item_id, quantity)

        elif choice == "4":
            keyword = input("Enter search keyword: ")
            search_item(inventory, keyword)

        elif choice == "5":
            inventory_report(inventory)

        elif choice == "6":
            save_inventory(inventory)
            print("💾 Inventory saved. Exiting...")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
