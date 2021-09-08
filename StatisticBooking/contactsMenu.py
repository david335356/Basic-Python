
import os

ADD = 1
SHOW = 2
SEARCH = 3
MODIFY = 4
DELETE = 5
QUIT = 6





def main():
    choice = 0
    
    while choice != QUIT:
        # Get the user's menu choice.
        choice = menuChoice()

        # Process the choice.
        if choice == ADD:
            addContact()
        elif choice == SHOW:
            showContact()
        elif choice == SEARCH:
            searchContact()
        elif choice == MODIFY:
            modifyContact()
        elif choice == DELETE:
            deleteContact()

def menuChoice():
    print()
    print('Contact Information')
    print('---------------------------')
    print('1. Add contact')
    print('2. Show list of Contacts')
    print('3. Search contacts')
    print('4. Modify contact')
    print('5. Delelte contact')
    print('6. Quit')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < ADD or choice > QUIT:
        choice = int(input('Enter a valid choice: '))
    if choice == QUIT:
        quitMenu()
    # return the user's choice.
    return choice

def quitMenu():
    print("Exiting out of Contact Menu")
    contact_file = open('contacts.txt','r')
    contact_file.close()


    
def addContact():
    another = 'y'

    contact_file = open("contacts.txt",'a')

    while another =='y' or another =="Y":
        print("Enter the person information.")

        name = input("Name: ")
        email = input("Email: ")
        phoneNumber = int(input("Phone Number: "))

        contact_file.write(name + '\n')
        contact_file.write(email +'\n')
        contact_file.write(str(phoneNumber) + '\n')

        print("Would you like to enter another contact?")
        another = input('Y = yes, anything else = no: ')

    contact_file.close()
    print("The contact has been added!")

def showContact():
    contact_file = open("contacts.txt", 'r')

    name = contact_file.readline()


    while name != '':

        email = contact_file.readline()
        phoneNumber = contact_file.readline()

        name = name.rstrip('\n')
        email = email.rstrip('\n')




        print("Name:", name)
        print("Email:", email)
        print("Phone:", phoneNumber)

        name = contact_file.readline()


    contact_file.close()

def searchContact():
    found = False

    search = input("Enter the persons name to locate there information: ")

    contact_file = open("contacts.txt", 'r')

    name = contact_file.readline()

    while name != '':
        email = contact_file.readline()
        phoneNumber = str(contact_file.readline())

        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phoneNumber = phoneNumber.rstrip('\n')
        if name == search:
            print("Name: ", name)
            print("Email: ", email)
            print("Phone: ", phoneNumber)

            found = True
        
        name = contact_file.readline()

    contact_file.close()
    if not found:
        print("That person doesn't exisit in the contacts.")

def modifyContact():
    found = False

    search = input('Enter a name to search for: ')
    new_email = input('Enter the new email: ')
    new_phone = int(input('Enter the new phone: '))

    contact_file = open("contacts.txt", 'r')
    temp_file = open("tempFile.txt", 'w')

    name = contact_file.readline()

    while name != '':
        email = contact_file.readline()
        phoneNumber = contact_file.readline()

        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phoneNumber = phoneNumber.rstrip('\n')
        
        if name == search:
            temp_file.write(name + '\n')
            temp_file.write(new_email + '\n')
            temp_file.write(str(new_phone)+ '\n')

            found = True

        else:
            temp_file.write(name + '\n')
            temp_file.write(email + '\n')
            temp_file.write(str(phoneNumber) + '\n')

        name = contact_file.readline()


    contact_file.close()
    temp_file.close()


    os.remove('contacts.txt')

    os.rename('tempFile.txt', 'contacts.txt')


    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

def deleteContact():
    found = False

    # Get the coffee to delete.
    search = input('Which name do you want to delete? ')

    # Open the original coffee.txt file.
    contact_file = open('contacts.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first record's description field.
    name = contact_file.readline()

    while name != '':
        # Read the quantity field.
        email = contact_file.readline()
        phoneNumber = contact_file.readline()
        
        # Strip the \n from the description.
        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phoneNumber = phoneNumber.rstrip('\n')

        # If this is not the record to delete, then
        # write it to the temporary file.
        if name != search:
            # Write the record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(email + '\n')
            temp_file.write(str(phoneNumber) + '\n')

        else:
            # Set the found flag to True.
            found = True

        # Read the next description.
        name = contact_file.readline()

    contact_file.close()
    temp_file.close()

    os.remove('contacts.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'contacts.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')
main()
