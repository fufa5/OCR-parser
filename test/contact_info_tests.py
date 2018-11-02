import unittest
from contact_info import ContactInfo

class ContactInfoTestCase(unittest.TestCase):
    """Test cases for ContactInfo class"""

    def setUp(self):
        self.contact = ContactInfo()

    def test_mutators(self):
        """Test mutators for phone number"""
        self.contact.set_phone_number("4433330098")
        self.assertEqual(self.contact.get_phone_number(), "4433330098", "Phone numbers not set in ContactInfo")

        """Test mutators for email address"""
        self.contact.set_email_address("msmith@asymmetrik.com")
        self.assertEqual(self.contact.get_email_address(), "msmith@asymmetrik.com", "Email address not set in ContactInfo")

        """Test mutators for name"""
        self.contact.set_name("Mike Smith")
        self.assertEqual(self.contact.get_name(), "Mike Smith", "Name not set in ContactInfo")
