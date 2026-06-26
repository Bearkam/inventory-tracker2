# NAMA: DHIKA MAULANA
# KELAS :IF25D
# NIM: 25416255201121
# PROJEK CSV STRUKTUR DATA
# MENGGUNAKAN HASH MAP DAN SEARCHING

import csv
import os

INVENTORY_CSV = 'inventory.csv'
inventory = {}

def load_inventory():
    if os.path.exists(INVENTORY_CSV):
        with open(INVENTORY_CSV, mode = 'r', newline = '') as file:
            reader = csv.reader(file)

            for row in reader:
                item, quantity =   row
                inventory[item] = int(quantity)

def save_inventory():
    with open(INVENTORY_CSV, mode= 'w', newline= '') as file:
        writer = csv.writer(file)

        for item, quantity in inventory.items():
            writer.writerow([item, quantity])
def add_items(item, quantity):
    if item in inventory:
        inventory[item] += quantity
        
    else:
        inventory[item] = quantity
        print(f"Ditambah {quantity}")
def remove_item(item, quantity):
    if item in inventory:
        if inventory[item] <= quantity:
            del inventory[item]
            print(f"{item} Dihapus semua dari inventory.")
        else:
            inventory[item] -= quantity
            print(f"Mengambil {quantity}{item}(s)")
    else:
        print(f"{item} not found in inventory")
def check_item(item):
    if item in inventory:
        print(f"{item}: {inventory[item]}")
    else:
        print(f"{item} is not in inventory")
def show_inventory():
    if not inventory:
        print("Inventory Kosong")
    else:
        print("Inventory Terkini")

        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

def main():
    load_inventory()

    print("Selamat Datang di Inventory Tracker")
    print("Commands : add <qty> <item>, remove <qty> <item>, check <item>, show, quit")

    while True:
        command = input(">").strip().lower()
        if command == "quit":
            save_inventory()
            print("Inventory disimpan. Terima kasih")
        elif command == "show":
            show_inventory()
        elif command.startswith("add"):
            try:
                parts = command.split()
                qty = int(parts[1])
                item = ' '.join(parts[2:])
                add_items(item, qty)
            except:
                print("Invalid sebagai command. Gunakan add <qty> <item>")
        elif command.startswith("remove"):
            try:
                parts = command.split()
                qty = int(parts[1])
                item = " ".join(parts[2:])
                remove_item(item, qty)
            except:
                print("Invalid sebagai command. Gunakan remove <qty> <item>")
        elif command.startswith("check"):
            item = command[6:].strip()
            check_item(item)
        else:
            print("Command Tidak Ada. Silahkan coba lagi")
            break

if __name__ == "__main__":
    main()
    

