# Write a function that lets the user add items to a list

def add_item(shopping_list):
    item = input("Enter the item you want to add: ")
    shopping_list.append(item)
    print(f"Added '{item}' to your shopping list.")

# Include a function to remove items from a list
    def remove_item(shopping_list):
        item = input("Enter the item you want to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed '{item}' from your shopping list.")
        else:
            print(f"'{item}' is not in your shopping list.")

# Add a function that prints out the entire list in a formatted way

def print_list(shopping_list):
    print("In Your shopping list:")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")