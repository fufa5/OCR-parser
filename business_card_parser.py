#!/usr/bin/env python

import os.path
import glob
import re
from contact_info import ContactInfo

__author__ = "David Pinkler"


class BusinessCardParser():
    """
    Main execution class for parsing business card files
    """
    DEFAULT_FILE_SEARCH_STRING = "doc*txt"

    def __init__(self):

        self.run_path = os.path.abspath(os.path.dirname(__file__))
        self.input_directory = os.path.join(self.run_path, "input")

    def read_input_file(self, input_file):

        with open(input_file) as f:
            return f.readlines()

    def extract_entities_from_file(self, file_lines):
        """Loops through lines in a file twice - the first to populate the email
        and the second to populate phone number and name.  The name will be deduced from the email
        address, hence the need for two loops
        """

        contact = ContactInfo()

        email = None

        for content in file_lines:

            raw_line = content.replace("\n", "")

            email = self.extract_email(raw_line)

            if email:
                contact.set_email_address(email[0])
                continue

        for content in file_lines:

            raw_line = content.replace("\n", "")

            phone = self.extract_phone_number(raw_line)

            if phone:
                contact.set_phone_number(phone[0])

            name = self.extract_name(raw_line, email[0])

            if name:
                contact.set_name(name)
                continue

        return contact

    def get_list_of_files(self, directory, search_string=DEFAULT_FILE_SEARCH_STRING):
        """Gets list of files for processing.
           search_string defaults to "doc*txt", but can be defined at runtime
           (e.g., for testing)
        """

        return glob.glob(os.path.join(directory, search_string))

    def extract_email(self, content):

        return re.match(r"\S+@\S+\.\S+", content, re.IGNORECASE)

    def extract_phone_number(self, content):

        if re.match("[Ff]ax:", content):
            return None
        else:
            pattern = re.compile(r"(\s|-|\(|\)|\+|[Pp]hone:\s|[Tt]el:\s)")
            raw_content = pattern.sub("", content) #get rid of symbols in number
            return re.match("^[0-9]+$", raw_content) #only match numbers

    def extract_name(self, content, email):
        """Deduces name from email address by recursively comparing substrings
        for email address and last name
        Assumes that email addresses are of the form [prefix][last_name]@[domain]
        """

        last_name = self.extract_last_name(content)

        if last_name:
            if re.search(last_name, email, re.IGNORECASE):
                #Find last name in email address
                return content
            else:
                return None
        else:
            return None

    def extract_last_name(self, content):
        """Return the string after the final space if it exists.
           This string will be used to compare against the email address
           to test whether it the entire string is a name
        """
        last_name_index = content.rfind(" ")
        if last_name_index == -1:
            return None #If there is no space, this is definitely not a name
        else:
            return content[last_name_index + 1:]  # Get string between space and newline
            # return content[last_name_index+1:len(content)-1] #Get string between space and newline

    def print_results(self, contact):

        print("Name: " + contact.get_name())
        print("Phone: " + contact.get_phone_number())
        print("Email: " + contact.get_email_address())
        print("\n")

    def process_files(self):

        file_list = self.get_list_of_files(self.input_directory)

        for file in file_list:
            file_lines = self.read_input_file(os.path.join(self.input_directory, file))
            contact_info = self.extract_entities_from_file(file_lines)
            self.print_results(contact_info)


if __name__ == "__main__":
    BusinessCardParser().process_files()
