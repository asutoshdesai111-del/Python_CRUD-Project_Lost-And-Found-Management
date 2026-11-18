
items = {}

while True:
    print("\n===== LOST AND FOUND MANAGEMENT =====")
    print("1. Add Lost Item")
    print("2. Add Found Item")
    print("3. Display Items")
    print("4. Search Item")
    print("5. Update Item")
    print("6. Delete Item")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1 | 2:
            itemId = int(input("Enter Item ID: "))

            if itemId in items:
                print("Item ID already exists!")
            else:
                itemName = input("Enter Item Name: ")
                itemLoc = input("Enter Location: ")
                itemContact = input("Enter Contact: ")

                if choice == 1:
                    itemType = "Lost"
                else:
                    itemType = "Found"

                items[itemId] = {
                    "Name": itemName,
                    "Location": itemLoc,
                    "Contact": itemContact,
                    "Type": itemType
                }

                print("Item Added Successfully!")

        case 3:
            if items:
                for itemId, data in items.items():
                    print(itemId, data)
            else:
                print("No Items Available!")

        case 4:
            itemId = int(input("Enter Item ID: "))

            if itemId in items:
                print(items[itemId])
            else:
                print("Item Not Found!")

        case 5:
            itemId = int(input("Enter Item ID: "))

            if itemId in items:
                items[itemId]["Location"] = input("Enter New Location: ")
                items[itemId]["Contact"] = input("Enter New Contact: ")
                print("Item Updated Successfully!")
            else:
                print("Item Not Found!")

        case 6:
            itemId = int(input("Enter Item ID: "))

            if itemId in items:
                del items[itemId]
                print("Item Deleted Successfully!")
            else:
                print("Item Not Found!")

        case 7:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice!")
