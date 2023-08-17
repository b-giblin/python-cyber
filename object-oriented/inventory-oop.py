from item import Item
inventory_list = []

def add_item():
    try:
        name = input('Name:  ')
        q = int(input('Quantity:  '))
        desc = input('Description  ')
        item = Item(name, q, desc)
        inventory_list.append(item)
    except:
        print("error")

def display_item():
    for item in inventory_list:
        name = item.name
        q = item.quantity
        desc = item.description
        index = inventory_list.index(item)
        print("--------------------")
        print(f"Item Number: {index}")
        print(f"Item Name: {name}")
        print(f"Item Quantity: {q}")
        print(f"Item Description: {desc}")
        print("--------------------")

def change_quantity():
    try:
        index = int(input("Enter the Item Number  "))
        item = inventory_list[index]
        new_quantity = int(input("Enter the new Quantity:  "))
        item['q'] = new_quantity
        print(f'The item quantity has been changed to {new_quantity}')
    except:
        print('error')

def remove_item():
    try:
        index = int(input("Enter the item number to remove  "))
        inventory_list.pop(index)
    except:
        print("something went wrong")

add_item()
add_item()
display_item()
remove_item()
display_item()