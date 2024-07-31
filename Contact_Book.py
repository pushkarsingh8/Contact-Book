#Contact Book:-
import time
def main():
    contact_list = []
    while True:
        
        #Contact Book actions:-
        print("\nWelcome in Contact Book:-\n1.Add Contact\n2.View Contact\n3.Search Contact\n4.Update Contact\n5.Delete Contact\n6.Exit Contact Book")
        
        user = int(input(":> "))
        
        
        if user == 1:
            add_contact(contact_list)
        
        elif user == 2:
            view_contact(contact_list)
        
        elif user == 3:
            search_contact(contact_list)

        elif user == 4:
            update_contact(contact_list)
        
        elif user == 5:
            delete_contact(contact_list)
        
        elif user == 6:
            print("You want to exit (yes/no)")
            choice = input("> ").lower()
            if choice == "yes":
                break
            elif choice == "no":
                continue
            else:
                print("Invalid statements\nEnter yes/no for Exit...")
                
                
            
        
        else:
            print("Invalid Statements Please Enter again input:-")
            user = int(input("> "))





#Create new contact:-
def add_contact(contact_list):
    name = input("Enter Contact Name: ")
    number = input(f"Enter {name} Number: ")
    email = input(f"Enter {name} E-mail: ")
    address = input(f"Enter {name} Address: ")
    
            
            
    contact = {
        "name":name,
        "number":number,
        "email": email,
        "address":address
            }
            
    contact_list.append(contact)
    print("\nContact Added Successfully.\n")
            
    
#View Contact:-
def view_contact(contact_list):
    
    if not contact_list:
        print("Not contacts are available")
    else:
        for index,contact in enumerate(contact_list,start=1):
            print(f"\nContact {index}:")
            print(f"Name: {contact['name']} ")
            print(f"Number: {contact['number']}")
            print(f"E-mail: {contact['email']}")
            print(f"Address: {contact['address']}")
            
#Search Contact
def search_contact(contact_list):
    print("enter a name to search")
    name = input("> ")
    print("please wait...\n")
    time.sleep(2)
    
    for contact in contact_list:
        if contact['name'].lower() == name.lower():
            print(f"Name: {contact['name']} ")
            print(f"Number: {contact['number']}")
            print(f"E-mail: {contact['email']}")
            print(f"Address: {contact['address']}")
            return 
    
    print("Contact not found")
            
#Update Contact
def update_contact(contact_list):
    print("enter a name to Update contact details")
    name = input("> ")
    for contact in contact_list:
        if contact['name'].lower() == name.lower():
            contact ['number'] = int(input("enter New number: "))
            contact ['email'] = int(input("enter New E-mail: "))
            contact ['address'] = int(input("enter New Address: "))
            print("Contact Successfully Updated\n")
            return
    print("Contact not found")
    
#Delete Contact
def delete_contact(contact_list):
    name = input("enter a name for update conatact details")
    for contact in contact_list:
        if contact['name'].lower() == name.lower():
            contact_list.remove(contact)
            print("Contact Permanent Removed")
            return
    print("Contact not found")    
    
    
if __name__ == "__main__":
    main()


