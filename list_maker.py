def shopping_list_maker():
    shopping_list = []

    while True:
        print("Shopping List Maker")
        print("1. Add item")
        print("2. Remove item")
        print("3. Print list")
        print("4. Quit")

        choice = input("What would you like to do? ")

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            print_list(shopping_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

shopping_list_maker()