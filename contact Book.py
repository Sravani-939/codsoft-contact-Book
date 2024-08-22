contacts={}
def add_contact():
    name=input("enter name:")
    phone=input("enter phone number:")
    if name in contacts:
        print("This contact is already exists...!")
    else:
        contacts[name]=phone
        print("contact added successfully.")
def delete_contact():
    name=input("enter name:")
    if name in contacts:
        del contacts[name]
        print("contact deleted successfully.")
    else:
        print("This contact does not exists...!")
def update_contact():
    name=input("enter name:")
    for contact in contacts:
        if contact==name:
            phone=input("enter new phone number:")
            contacts[name]=phone
            print("contact updated successfully.")
            break
        else:
            print("this contact does not exist.")
def search_contact():
    name=input("enter name:")
    for contact in contacts:
        if contact.lower()==name.lower():
            print("contact Found")
            print(contact,contacts[contact])
            break
        else:
            print("contact not found.")
def display_contact():
        if contacts=={}:
            print("There are no contacts.")
        else:
            print("contacts list:")
            for name,phone in contacts.items():
                print(name,phone)
            
            
        
        
        
while True:
    print("/ncontact Book Menu:")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Update contact")
    print("4. Search contact")
    print("5. Display contacts")
    print("6. Exit")
    choice = int(input("Enter your choice(1-6):"))
    if choice==1:
        add_contact()
    elif  choice==2: 
        delete_contact()
    elif  choice==3: 
        update_contact()
    elif  choice==4: 
        search_contact()
    elif  choice==5: 
        display_contact()
    elif  choice==6: 
        print("Existing contact Book. Goodbye!")
        break
    else:
        print("invalid choice: please enter a number from (1-6) Only")
         
    
    
