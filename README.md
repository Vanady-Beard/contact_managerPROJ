https://github.com/Vanady-Beard/contacts_management.git

In the beginning of the code, started off using the Import re in order to use REGEX and lastly created a empty string where all the contacts will be stored.

def new (contacts)

This function def new (contacts) is where new contacts are being stored in. 

It use a REGEX for the phone number to make sure the user put the phone number in a certain format and if not than prompt the user to enter the phone number again. 


def edit (contacts):

This function def edit (contacts) is makeing sure that the user can edit their contacts. The user can either use the same name and edit the number or both if needed. 


def delete (contacts):

This function def delete (contacts) is where any contact the user want to delete the contact will be removed. Its using a try, except to take care of the errors if the user is trying to delete a contact that does not exist. 

def search (contacts):

This function def search (contacts) is where the user can search for any contacts. If the contact exist it will take out that contact and display only the contact the user searched. 

def display (contacts)

This function def display (contacts) show all the contacts that exist. 

def export(contacts)

This function def export(contacts) is used for the user to export their contacts to a txt file and have the contacts stored in the txt file. 


def import_file (contacts)

This function def import_file (contacts) is used for the user to import their contact from the txt file. 


def quit (contacts):

This function def quit (contacts) is used so the user can quit when the user is done. 

def main (contacts)

This function def main (contacts) is the driver code and the main function. This function hold a message so the user can choose what they want to do. If they do not enter a number for their option it will show an error message to prompt the user to enter a number. Depending on what the user select it will direct the user to the functions above and run the function. 
    
    