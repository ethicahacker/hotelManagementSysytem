from rooms import room_menu
from customers import customer_menu
from myprint import print_center, input_center

if __name__ == '__main__':
    while True:
        print()
        print_center("==============================")
        print_center("=====Code With Anshuman Hotels=====")
        print_center("==============================")
        print_center("1. Manage Rooms")
        print_center("2. Manage Customers")
        print_center("0. Exit")
        print()

        choice = int(input_center("Enter your choice: "))
        if choice == 1:
            room_menu()
        elif choice == 2:
            customer_menu()
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to exit)")
    print_center("GoodBye")
