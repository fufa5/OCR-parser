"""
This class acts as a domain object for contact information
"""
__author__ = "David Pinkler"


class ContactInfo():

    def __init__(self, name=None, phone_number=None, email_address=None):
        self._name = name
        self._phone_number = phone_number
        self._email_address = email_address

    def get_name(self):
        return self._name

    def get_phone_number(self):
        return self._phone_number

    def get_email_address(self):
        return self._email_address

    def set_name(self, name):
        self._name = name

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_email_address(self, email_address):
        self._email_address = email_address
