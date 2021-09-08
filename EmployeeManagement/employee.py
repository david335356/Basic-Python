# The Contact class holds contact information.

class Employee:
    # The __init__ method initializes the attributes.
    def __init__(self, ID, name, depart, title):
        self.__ID = ID
        self.__name = name
        self.__depart = depart
        self.__title = title

    # The set_name method sets the name attribute.
    def set_ID(self, ID):
        self.__ID = ID

    def set_name(self, name):
        self.__name = name

    # The set_phone method sets the phone attribute.
    def set_depart(self, depart):
        self.__depart = depart

    # The set_email method sets the email attribute.
    def set_title(self, title):
        self.__title = title

    # The get_name method returns the name attribute.
    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name
    # The get_phone method returns the phone attribute.
    def get_depart(self):
        return self.__depart

    # The get_email method returns the email attribute.
    def get_title(self):
        return self.__title

    # The __str__ method returns the object's state
    # as a string.
    def __str__(self):
        return "ID: " + self.__ID + \
               "Name: " + self.__name + \
               "\nDepartment: " + self.__depart + \
               "\nTitle: " + self.__title
    
