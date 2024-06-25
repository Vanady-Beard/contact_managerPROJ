import re

contacts = []


def new (contacts):
  user_name = input("What is the name you will like to add ? ")
  user_number = input("What is the phone number ? ")

  phone_number_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
  while not phone_number_pattern.match(user_number):
        print("Please enter a valid phone number (format: ###-###-####)")
        user_number = input("What is the phone number ? ")
  contact = {"name": user_name, "phone_number" : user_number}
  contacts.append(contact)


  print(contacts)




def edit (contacts):
    edit_contact = input("What is the name of the contact you want to change?")
    for contact in contacts:
        if contact["name"] == edit_contact:
           contact["name"] = input("What is the name?")
           contact['phone_number'] = input("What is the phone number")
      
    print(contacts)



def delete (contacts):
    
    try:
        user_remove = input("What contact you will like to remove?")
        for c_remove in contacts:
            if c_remove["name"] == user_remove:
                contacts.remove(c_remove)
                print (contacts)
               

    except:
        print ('Name is not in your contacts')


def search (contacts):
    search_contact = input('What contact you want to search ? ')

    search = [] 
    for s_contact in contacts:
        if s_contact["name"] == search_contact:
           search.append(s_contact)
    print(search)
  
        
 
    

def display (contacts):
    print(contacts)



def export(contacts):
    file_name = "my_contacts.txt"
    with open(file_name, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone_number']}\n")
    print("Contacts exported to ", file_name)

def import_file (contacts):
    file_name = "my_contacts.txt"
    with open (file_name, "r") as file:
       for line in file:
           name, phone_number = line.strip().split(",")
           contacts.append({"name": name, "phone_number": phone_number})
    print("Contacts imported from", file_name)


def quit (contacts):
    print ('Goodbye !!')


def main (contacts):
    while True:
        welcome_user = input(
    '''
    🤗 Hello Welcome To Your Contact Management System 🤗
        
        Menu:
            1. Add a new contact
            2. Edit an existing contact
            3. Delete a contact
            4. Search for a contact
            5. Display all contacts
            6. Export contacts to a text file
            7. Import contacts from a text file
            8. Quit 
    ''' )

        if welcome_user == '1':
            new(contacts)

        elif welcome_user == '2':
            edit(contacts)
        elif welcome_user == '3':
            delete(contacts)
        elif welcome_user == '4':
            search(contacts)
        elif welcome_user == '5':
            display(contacts)
        elif welcome_user == '6':
            export(contacts)
        elif welcome_user == '7':
            import_file(contacts)
        elif welcome_user == '8':
            quit(contacts)
            break
        else:
            print("Please type a number to refer to the menu")


main(contacts)




