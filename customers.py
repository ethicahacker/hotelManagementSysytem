from customer import create_customer, print_header
from rooms import get_and_print_room_by_no, change_room_status
from datafile import DataFile
from datetime import datetime

NUMBER_OF_RECORDS_PER_PAGE = 10
customerTable = DataFile("customers.dat")


def add_customer():
    rooms, found, position = get_and_print_room_by_no()
    if found:
        room_no = rooms[position].room_no
        customers = customerTable.get_records()
        if len(customers) == 0:
            customer_id = 0
        else:
            customer_id = customers[len(customers)-1].customer_id + 1
        customer = create_customer(customer_id, room_no)
        confirm = input("Complete the operation? (Y/N) ")
        if confirm.lower() == 'y':
            customerTable.add_record(customer)
            change_room_status(room_no, False)
            print("Operation Successful")
        else:
            print("Operation Canceled")


def get_and_print_customer_list_by_name():
    customers = customerTable.get_records()
    results = []
    if len(customers) == 0:
        print("No Records found")
    else:
        name = input("Enter the name: ").lower()
        words = name.split()

        for customer in customers:
            for word in words:
                if word in customer.name.lower():
                    results.append(customer)
        if len(results) == 0:
            print("No matching record")
        else:
            print(len(results), " matching records")
            print_header()
            for customer in results:
                customer.print_all()
    return results


def get_and_print_employee_by_id():
    customers = customerTable.get_records()
    found = False
    position = -1
    if len(customers) == 0:
        print("No Records found")
    else:
        customer_id = int(input("Enter the id: "))
        for customer in customers:
            position += 1
            if customer_id == customer.customer_id:
                found = True
                break
        if not found:
            print("No matching record")
        else:
            customers[position].print_full()
    return customers, found, position


def get_and_print_customer_list_by_address():
    customers = customerTable.get_records()
    results = []
    if len(customers) == 0:
        print("No Records found")
    else:
        address = input("Enter the address: ").lower()
        words = address.split()

        for customer in customers:
            for word in words:
                if word in customer.address.lower():
                    results.append(customer)
        if len(results) == 0:
            print("No matching record")
        else:
            print(len(results), " matching records")
            print_header()
            for customer in results:
                customer.print_all()
    return results


def get_and_print_customer_list_by_phone():
    customers = customerTable.get_records()
    results = []
    if len(customers) == 0:
        print("No Records found")
    else:
        phone = input("Enter the phone number: ")
        for customer in customers:
            if phone in customer.phone:
                results.append(customer)
        if len(results) == 0:
            print("No matching record")
        else:
            print(len(results), " matching records")
            print_header()
            for customer in results:
                customer.print_all()
    return results


def get_and_print_customer_by_room_no():
    customers = customerTable.get_records()
    found = False
    position = -1
    if len(customers) == 0:
        print("No Records found")
    else:
        room_no = int(input("Enter the room no: "))
        for customer in customers:
            position += 1
            if room_no == customer.room_no and customer.checkout_date is None:
                found = True
                break
        if not found:
            print("No matching record")
        else:
            customers[position].print_full()
    return customers, found, position


def print_customer_list_by_check_in():
    customers = customerTable.get_records()
    if len(customers) == 0:
        print("No customers found")
    else:
        print("Enter the date: ")
        day = int(input("day of month: "))
        month = int(input("month: "))
        year = int(input("year: "))
        check_in = datetime(year, month, day)
        results = []
        for customer in customers:
            if customer.entry_date.date() == check_in.date():
                results.append(customer)
        if len(results) == 0:
            print("no matching records")
        else:
            print(len(results), " matching customers")
            print_header()
            for customer in results:
                customer.print_all()


def print_current_list_of_customers():
    customers = customerTable.get_records()
    if len(customers) == 0:
        print("No customers found")
    else:
        results = []
        for customer in customers:
            if customer.checkout_date is None:
                results.append(customer)
        if len(results) == 0:
            print("no matching records")
        else:
            print(len(results), " matching customers")
            print_header()
            for customer in results:
                customer.print_all()


def check_out():
    customers, found, position = get_and_print_customer_by_room_no()
    if found:
        customer = customers[position]
        customer.checkout_date = datetime.now()
        confirm = input("Confirm checkout? (Y/N): ")
        if confirm == 'y':
            customerTable.overwrite(customers)
            change_room_status(customer.room_no, True)
            print("Operation Successful")
        else:
            print("Operation Cancelled")


def edit_customer_details():
    customers, found, position = get_and_print_customer_by_room_no()
    if found:
        customer = customers[position]
        print("Input new values (leave blank to keep previous value)")
        name = input("Enter new name: ")
        if len(name) > 0:
            customer.name = name
        address = input("Enter new address: ")
        if len(address) > 0:
            customer.address = address
        phone = input("Enter new phone: ")
        if len(phone) > 0:
            customer.phone = phone
        confirm = input("Confirm Edit? (Y/N): ")
        if confirm == 'y':
            customerTable.overwrite(customers)
            print("Operation Successful")
        else:
            print("Operation Cancelled")


def delete_customer():
    customers, found, position = get_and_print_customer_by_room_no()
    if found:
        print("Confirm delete?? (Y/N): ")
        confirm = input()
        if confirm == 'y':
            customers.pop(position)
            customerTable.overwrite(customers)
            print("Operation Successful")
        else:
            print("Operation Cancelled")


def view_all_customers():
    customers = customerTable.get_records()
    if len(customers) == 0:
        print("No Record found")
    else:
        i = 0
        print_header()
        for customer in customers:
            i += 1
            customer.print_all()
            if i == NUMBER_OF_RECORDS_PER_PAGE:
                input("Press any key to continue.")


def customer_menu():
    while True:
        print()
        print("==============================")
        print("==========Customer Menu=========")
        print("==============================")
        print()
        print("1. New Customer")
        print("2. Show Customer Details by name")
        print("3. Show customer details by id")
        print("4. Show customer details by address")
        print("5. Show customer details by phone number")
        print("6. Show customer details by room no")
        print("7. Show customer details by check in date")
        print("8. Show current list of customers")
        print("9. Check out")
        print("10. Edit customer Details")
        print("11. Delete Customer record")
        print("12. View all customers")
        print("0. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_customer()
        elif choice == 2:
            get_and_print_customer_list_by_name()
        elif choice == 3:
            get_and_print_employee_by_id()
        elif choice == 4:
            get_and_print_customer_list_by_address()
        elif choice == 5:
            get_and_print_customer_list_by_phone()
        elif choice == 6:
            get_and_print_customer_by_room_no()
        elif choice == 7:
            print_customer_list_by_check_in()
        elif choice == 8:
            print_current_list_of_customers()
        elif choice == 9:
            check_out()
        elif choice == 10:
            edit_customer_details()
        elif choice == 11:
            delete_customer()
        elif choice == 12:
            view_all_customers()
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")
