import datetime
import os
print()
print (os.environ['USERPROFILE'])
user = (os.getenv('username'))
now = datetime.datetime.now()
print (f"Alice's Final Project") 
print (now.strftime("%X on %A, %B the %dth, %Y"))
print("\n")

# ----- This class holds general data about a person -----
class Person:
    # ----- __init__ method for initialization -----
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
    # ----- Mutators - Setters -----
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    # ----- Accessors - Getters -----
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone_number(self):
        return self.__phone_number
# ----- The Customer class is a subclass of the Person class -----
class Customer(Person):
    def __init__(self, name, address, phone_number, custom_number, mailing_list):           # Pass main class attributes as arguments and add new attributes
        Person.__init__(self, name, address, phone_number)                                  # Only old arguments
        self.__custom_number = custom_number                                                # Create new objects for subclass
        self.__mailing_list = mailing_list
    # ----- Mutators - Setters -----                                                        # Gets input from main
    def set_custom_number(self, custom_number):
        self.__custom_number = custom_number
    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list
    # ----- Accessors - Getters -----                                                       # Returns to main
    def get_custom_number(self):
        return self.__custom_number
    def get_mailing_list(self):
        return self.__mailing_list
# ----- Main function -----
def main():
    mailing_list = 'y'
    name = input(f"Please enter the customer's name: ")
    address = input(f"Please enter the customer's address: ")
    p_number = input(f"Please enter the customer's phone number: ")
    c_number = int(input(f"Please enter the customer number: "))
    mailing_list = input(f"Does the customer wish to be on the mailing list? y/n: ")
    # Create instance of class, calling Customer subclass
    customer_info = Customer(name, address, p_number, c_number, mailing_list)
    # Display info entered using getter methods
    print(f'\nHere is the info entered: \n')
    print(f'Name: {customer_info.get_name()}')
    print(f'Address: {customer_info.get_address()}')
    print(f'Phone number: {customer_info.get_phone_number()}')
    print(f'Customer number: {customer_info.get_custom_number()}')
    # Display whether the customer will be added to list or not, depending on their input
    if mailing_list.lower() == 'y':
        print('Customer has been added to list!\n')
    else:
        print("Customer won't be added to list.\n")
main()
