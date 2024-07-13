#Contact Book

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts.append(Contact(name, phone_number, email, address))

    def view_contacts(self):
        for i, contact in enumerate(self.contacts):
            print(f"{i+1}. {contact.name} - {contact.phone_number}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        for contact in self.contacts:
            if search_term in [contact.name, contact.phone_number]:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")

    def update_contact(self):
        self.view_contacts()
        index = int(input("Enter the number of the contact to update: ")) - 1
        
        contact = self.contacts[index]
        
        print(f'''
              Current Name: {contact.name}, 
              Phone Number: {contact.phone_number}, 
              Email: {contact.email}, 
              Address: {contact.address}
              ''')
        contact.name = input("Enter new name (or press Enter to keep current): ") or contact.name
        contact.phone_number = input("Enter new phone number (or press Enter to keep current): ") or contact.phone_number
        contact.email = input("Enter new email (or press Enter to keep current): ") or contact.email
        contact.address = input("Enter new address (or press Enter to keep current): ") or contact.address

    def delete_contact(self):
        self.view_contacts()
        index = int(input("Enter the number of the contact to delete: ")) - 1
        del self.contacts[index]

def main():
    contact_book = ContactBook()
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
