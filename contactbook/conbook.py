import csv

CONTACTS_FILE = 'contacts.csv'

def load_contacts():
    """Load contacts from a CSV file."""
    contacts = {}
    try:
        with open(CONTACTS_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:  # Expecting name, phone, email, address
                    name, phone, email, address = row
                    contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contacts loaded successfully.")
    except FileNotFoundError:
        print("No contacts file found. Starting with an empty contact list.")
    except Exception as e:
        print(f"Error loading contacts: {e}")
    return contacts

def save_contacts(contacts):
    """Save contacts to a CSV file."""
    try:
        with open(CONTACTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            for name, details in contacts.items():
                writer.writerow([name, details['phone'], details['email'], details['address']])
        print("Contacts saved successfully.")
    except Exception as e:
        print(f"Error saving contacts: {e}")

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter the contact's name: ").strip()
    phone = input("Enter the contact's phone number: ").strip()
    email = input("Enter the contact's email: ").strip()
    address = input("Enter the contact's address: ").strip()
    
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    """Display the list of all contacts."""
    if not contacts:
        print("No contacts available.")
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

def search_contact(contacts):
    """Search for a contact by name or phone number."""
    search_term = input("Enter the name or phone number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if search_term in (name, details['phone']):
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
    if not found:
        print("No contact found with that name or phone number.")

def update_contact(contacts):
    """Update a contact's details."""
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        phone = input(f"Enter the new phone number (current: {contacts[name]['phone']}): ").strip()
        email = input(f"Enter the new email (current: {contacts[name]['email']}): ").strip()
        address = input(f"Enter the new address (current: {contacts[name]['address']}): ").strip()
        
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
