"""
Exercise: Contact Book Menu
Student: Amir Katuwal
Day: 2
"""

# Initialize an empty dictionary to store contacts.

contacts = {}

# Contact Book Menu

while True:
    print("\n" + " Contact Book ".center(26, "-"))
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")
    print("\n" + "-" * 26)

    menu_choice = input("\nEnter your choice (1-5): ").strip()

    # Add a new contact with phone and email details.
    if menu_choice == "1":
        contact_name = input("Enter contact name: ").strip()
        phone_number = input("Enter phone number: ").strip()
        email_address = input("Enter email address: ").strip()

        contacts[contact_name] = {
            "phone": phone_number,
            "email": email_address
        }

        print(f"Contact added: {contact_name}")

    # Search for a contact without causing an error when it does not exist.
    elif menu_choice == "2":
        contact_name = input("Enter contact name to search: ").strip()

        if contact_name in contacts:
            contact_details = contacts[contact_name]

            print(f"Name: {contact_name}")
            print(f"Phone: {contact_details['phone']}")
            print(f"Email: {contact_details['email']}")
        else:
            print(f"Contact not found: {contact_name}")

    # Delete a contact only when the requested name exists.
    elif menu_choice == "3":
        contact_name = input("Enter contact name to delete: ").strip()

        if contact_name in contacts:
            del contacts[contact_name]
            print(f"Contact deleted: {contact_name}")
        else:
            print(f"Contact not found: {contact_name}")

    # Display all stored contacts and their details.
    elif menu_choice == "4":
        if contacts:
            print("\nAll contacts:")

            for contact_name, contact_details in contacts.items():
                print(f"Name: {contact_name} | Phone: {contact_details['phone']} | Email: {contact_details['email']}")
        else:
            print("No contacts available.")

    # Exit the program using break.
    elif menu_choice == "5":
        print("Exiting contact book...")
        break

    # Handle menu selections outside the available options.
    else:
        print("Invalid choice. Please select an option from 1 to 5.")