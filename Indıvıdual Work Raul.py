import json
import os
data_file = "inventory.json"

# Load existing dat
def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def show_menu():
    print("--- Medical Store Inventory ---")
    print("1. Add new record")
    print("2. View all records")
    print("3. Search record")
    print("4. Update record")
    print("5. Delete record")
    print("6. Summary statistics")
    print("7. Help")
    print("8. Clear all data")
    print("9. Exit")

def add_record(data):
    try:
        record = {
            "id": input("Enter ID: "),
            "name": input("Enter medicine name: "),
            "quantity": int(input("Enter quantity: ")),
            "price": float(input("Enter price per unit: "))
        }
        data.append(record)
        print("Record added.")
    except ValueError:
        print("Invalid input. Please enter numeric values for quantity and price.")

def view_records(data):
    if not data:
        print("No records found.")
        return
    for record in data:
        print(record)

def search_record(data):
    search_id = input("Enter ID to search: ")
    for record in data:
        if record["id"] == search_id:
            print("Record found:", record)
            return
    print("Record not found.")

def update_record(data):
    search_id = input("Enter ID of record to update: ")
    for record in data:
        if record["id"] == search_id:
            try:
                record["name"] = input("Enter new name: ")
                record["quantity"] = int(input("Enter new quantity: "))
                record["price"] = float(input("Enter new price: "))
                print("Record updated.")
            except ValueError:
                print("Invalid input.")
            return
    print("Record not found.")

def delete_record(data):
    search_id = input("Enter ID to delete: ")
    for i, record in enumerate(data):
        if record["id"] == search_id:
            del data[i]
            print("Record deleted.")
            return
    print("Record not found.")

def summary_stats(data):
    if not data:
        print("No data available.")
        return
    total_items = sum(record["quantity"] for record in data)
    total_value = sum(record["quantity"] * record["price"] for record in data)
    print(f"Total items: {total_items}")
    print(f"Total inventory value: {total_value:.2f}")

def help_info():
    print("\nThis is a Medical Store Inventory System.")
    print("Use the menu options to manage your medicine records.")
    print("Each record contains an ID, name, quantity, and price.")

def clear_data(data):
    confirm = input("Are you sure you want to delete all data? (yes/no): ")
    if confirm.lower() == "yes":
        data.clear()
        print("All data cleared.")

def main():
    data = load_data()
    while True:
        show_menu()
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                add_record(data)
            elif choice == 2:
                view_records(data)
            elif choice == 3:
                search_record(data)
            elif choice == 4:
                update_record(data)
            elif choice == 5:
                delete_record(data)
            elif choice == 6:
                summary_stats(data)
            elif choice == 7:
                help_info()
            elif choice == 8:
                clear_data(data)
            elif choice == 9:
                save_data(data)
                print("Exiting. Data saved.")
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")
main()