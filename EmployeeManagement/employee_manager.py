# This program manages contacts.
import employee
import pickle

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the filename
FILENAME = 'employees.dat'

# main function
def main():
    # Load the existing contact dictionary and
    # assign it to mycontacts.
    myemployees = load_employees()

    # Initialize a variable for the user's choice.
    choice = 0

    # Process menu selections until the user
    # wants to quit the program.
    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(myemployees)
        elif choice == ADD:
            add(myemployees)
        elif choice == CHANGE:
            change(myemployees)
        elif choice == DELETE:
            delete(myemployees)

    # Save the mycontacts dictionary to a file.
    save_employees(myemployees)

def load_employees():
    try:
        # Open the contacts.dat file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        employee_dct = pickle.load(input_file)

        # Close the phone_inventory.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        employee_dct = {}

    # Return the dictionary.
    return employee_dct

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up a Employee')
    print('2. Add a new Employee')
    print('3. Change an existing Employee')
    print('4. Delete a Employee')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

# The look_up function looks up an item in the
# specified dictionary.
def look_up(myemployees):
    # Get a name to look up.
    ID = input('Enter a ID: ')

    # Look it up in the dictionary.
    print(myemployees.get(ID, 'That ID is not found.'))

# The add function adds a new entry into the
# specified dictionary.
def add(myemployees):
    # Get the contact info.
    ID = input("ID: ")
    name = input('Name: ')
    depart = input('Department: ')
    title = input('title: ')

    # Create a Contact object named entry.
    entry = employee.Employee(ID, name, depart, title)

    # If the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if name not in myemployees:
        myemployees[ID] = entry
        print('The entry has been added.')
    else:
        print('That ID already exists.')

# The change function changes an existing
# entry in the specified dictionary.
def change(myemployees):
    # Get a name to look up.
    ID = input('Enter a ID: ')

    if ID in myemployees:

        name = input("If a different name please enter the new name: ")
        # Get a new phone number.
        depart = input('Enter the new department: ')

        # Get a new email address.
        title = input('Enter the new job title: ')

        # Create a contact object named entry.
        entry = employee.Employee(ID, name, depart, title)

        # Update the entry.
        myemployees[ID] = entry
        print('Information updated.')
    else:
        print('That ID is not found.')

# The delete function deletes an entry from the
# specified dictionary.
def delete(myemployees):
    # Get a name to look up.
    ID = input('Enter a ID: ')

    # If the name is found, delete the entry.
    if ID in myemployees:
        del myemployees[ID]
        print('Entry deleted.')
    else:
        print('That ID is not found.')

# The save_contacts funtion pickles the specified
# object and saves it to the contacts file.
def save_employees(myemployees):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(myemployees, output_file)

    # Close the file.
    output_file.close()

# Call the main function.
main()

    
