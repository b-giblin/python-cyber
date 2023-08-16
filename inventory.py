# Author: Brian Giblin
# Date: 8/16/23
# Description: Functions used to populate a dictionary in python.


# Create an empty list to populate
inventory_list = []


# Create function for adding items to the list
def add_item():
    try:
        name = input('Name:  ')
        q = int(input('Quantity:  '))
        desc = input('Description  ')
        new_item = {
            'name': name,
            'q': q,
            'desc': desc
        }
        inventory_list.append(new_item)

    except:
        print("an error has occured")


# create function for displaying the items
def display_item():
    for item in inventory_list:
        name = item['name']
        q = item['q']
        desc = item['desc']
        index = inventory_list.index(item)
        print('-------------------------------')
        print(f"Item Number:  {index}")
        print(f"Item Name:  {name}")
        print(f"Item Quantity:  {q}")
        print(f"Item Description:  {desc}")
        print('-------------------------------')


# create a function to change the quantity

def change_quantity():
    try:
        index = int(input("Enter the Item Number  "))
        item = inventory_list[index]
        new_quantity = int(input('Enter new quantity:  '))
        item['q'] = new_quantity
        print(f'The item has been changed to {new_quantity}')
    except:
        print('error')


# create a function to remove the item from the list
def remove_item():
    try:
        index = int(input("Enter the Item Number  "))
        inventory_list.pop(index)
    except:
        print("something went wrong")

add_item()
add_item()
display_item()
remove_item()
display_item()