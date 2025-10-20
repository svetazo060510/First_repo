def add_contact(contact_info, contacts_list):
    parts = contact_info.split(',')
    if len(parts) != 3:
        print("Error: Invalid format. Please use Name, Phone, Email.")
        return False
    else:
        contact_dictionary = {
            "name": parts[0].strip(),
            "phone": parts[1].strip(),
            "email": parts[2].strip()
        }
        contacts_list.append(contact_dictionary)
        return True

def search_contact(search_name, contacts_list):
    for contact in contacts_list:
        if contact['name'].lower() == search_name.lower():
            return contact    
    return None

def main():
    contacts = []
    print("--- Add Contacts ---")
    while True:
        contact_info = input("Enter contact as 'Name, Phone, Email' (or 'done' to finish): ")
        if contact_info.lower() == "done":
            break
        add_contact(contact_info, contacts)

    if contacts:
        print("\n--- Search for a Contact ---")
        search_name_input = input("Enter a name to search for: ")        
        found_contact = search_contact(search_name_input, contacts)
        
        if found_contact:
            print("\n--- Contact Found ---")
            print(f"Name: {found_contact['name']}")
            print(f"Phone: {found_contact['phone']}")
            print(f"Email: {found_contact['email']}")
        else:
            print("Contact not found.")
    else:
        print("Your contact book is empty.")

if __name__ == "__main__":
    main()