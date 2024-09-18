import sys
from phonebook import PhoneBook
from contact import Contact

def main():
    phonebook = PhoneBook()
    while True:
        print("1. Add Contact")
        print("2. Search Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Import from CSV")
        print("7. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            phone = input("Phone (###) ###-####: ")
            email = input("Email (optional): ")
            address = input("Address (optional): ")
            contact = Contact(first_name, last_name, phone, email, address)
            phonebook.add_contact(contact)

        elif choice == '2':
            query = input("Enter name or phone to search: ")
            results = phonebook.search(query)
            for contact in results:
                print(contact)

        elif choice == '3':
            phone = input("Enter the phone number of the contact to update: ")
            first_name = input("New First Name (leave blank to skip): ")
            last_name = input("New Last Name (leave blank to skip): ")
            new_phone = input("New Phone (leave blank to skip): ")
            email = input("New Email (leave blank to skip): ")
            address = input("New Address (leave blank to skip): ")
            phonebook.update_contact(phone, first_name=first_name, last_name=last_name,
                                     phone=new_phone, email=email, address=address)

        elif choice == '4':
            phone = input("Enter the phone number of the contact to delete: ")
            phonebook.delete_contact(phone)

        elif choice == '5':
            phonebook.display_contacts()

        elif choice == '6':
            csv_file = input("Enter the CSV file path: ")
            phonebook.batch_import(csv_file)

        elif choice == '7':
            sys.exit()

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
