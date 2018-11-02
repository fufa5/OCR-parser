import os.path
import unittest

from business_card_parser import BusinessCardParser


class ParserTestCase(unittest.TestCase):
    """ Test cases for BusinessCardParser """

    def setUp(self):
        self.parser = BusinessCardParser()
        self.run_path = os.path.abspath(os.path.dirname(__file__))
        self.input_directory = os.path.join(self.run_path, "../input")

        fw = open(os.path.join(self.input_directory, "test1.txt"), "w")
        fw.write("Hello\nWorld")
        fw.close()

        fw = open(os.path.join(self.input_directory, "test2.txt"), "w")
        fw.write("Bonjour le Monde!")
        fw.close()

    def test_file_list(self):
        """ Test get_list_of_files, assuming there will be 2 files
            Really more of an integration test
        """
        files = self.parser.get_list_of_files(self.input_directory, "test*txt")
        self.assertEqual(len(files), 2, "Unexpected number of files.")

    def test_read_input_file(self):

        files = self.parser.get_list_of_files(self.input_directory, "test*txt")
        test_file = os.path.abspath(files[0])
        file_lines = self.parser.read_input_file(test_file)
        self.assertEqual(len(file_lines), 2, "Unexpected number of lines in file.")

    def test_extract_email(self):
        """ Test regex, assuming that email will be on its own line """
        result = self.parser.extract_email("msmith@asymmetrik.com")
        self.assertEqual(result[0], "msmith@asymmetrik.com", "Invalid email extraction")

        result = self.parser.extract_email("lisa.haung@foobartech.com")
        self.assertEqual(result[0], "lisa.haung@foobartech.com", "Invalid email extraction")

        result = self.parser.extract_email("awilson@abctech.com")
        self.assertEqual(result[0], "awilson@abctech.com", "Invalid email extraction")

        result = self.parser.extract_email("awilson@abctech.edu")
        self.assertEqual(result[0], "awilson@abctech.edu", "Invalid email extraction")

        result = self.parser.extract_email("bad_email234.com")
        self.assertIsNone(result, "Invalid email extraction")

        result = self.parser.extract_email("bad_email@test")
        self.assertIsNone(result, "Invalid email extraction")

    def test_extract_phone_number(self):

        result = self.parser.extract_phone_number("(410)555-1234")
        self.assertEqual(result[0], "4105551234", "Invalid phone number extraction 1")

        result = self.parser.extract_phone_number("410-555-1234")
        self.assertEqual(result[0], "4105551234", "Invalid phone number extraction 2")

        result = self.parser.extract_phone_number("+1 (703) 555-1259")
        self.assertEqual(result[0], "17035551259", "Invalid phone number extraction 3")

        result = self.parser.extract_phone_number("Tel: +1 (703) 555-1259")
        self.assertEqual(result[0], "17035551259", "Invalid phone number extraction 3")

        result = self.parser.extract_phone_number("Phone: 410-555-1234")
        self.assertEqual(result[0], "4105551234", "Invalid phone number extraction 4")

        result = self.parser.extract_phone_number("Mike Smith445")
        self.assertIsNone(result, "Invalid phone number extraction 5")

        result = self.parser.extract_phone_number("Fax: 410-555-1234")
        self.assertIsNone(result, "Invalid phone number extraction 6")

        result = self.parser.extract_phone_number("1234 Sentry Road")
        self.assertIsNone(result, "Invalid phone number extraction 7")

    def test_extract_last_name(self):
        result = self.parser.extract_last_name("Mike Smith")
        self.assertEqual(result, "Smith", "Invalid last name extraction")

        result = self.parser.extract_last_name("+1 (703) 555-1259")
        self.assertEqual(result, "555-1259", "Invalid last name extraction")


    def test_extract_name(self):
        result = self.parser.extract_name("Mike Smith", "msmith@asymmetrik.com")
        self.assertEqual(result, "Mike Smith", "Invalid name extractions")

        result = self.parser.extract_name("123 North 11th Street", "msmith@asymmetrik.com")
        self.assertIsNone(result, "Invalid name extraction")

        result = self.parser.extract_name("ASYMMETRIK LTD", "msmith@asymmetrik.com")
        self.assertIsNone(result, "Invalid name extraction")

        result = self.parser.extract_name("+1 (703) 555-1259", "awilson@abctech.com")
        self.assertIsNone(result, "Invalid name extraction")

    def test_extract_entities_from_file(self):
        file_lines = ["ASYMMETRIK LTD\n","Mike Smith\n","Senior Software Engineer\n",\
                      "(410)555-1234\n","msmith@asymmetrik.com\n"]
        result = self.parser.extract_entities_from_file(file_lines)
        self.assertEqual(result.get_name(), "Mike Smith", "Extraction from file lines failed")
        self.assertEqual(result.get_phone_number(), "4105551234", "Extraction from file lines failed")
        self.assertEqual(result.get_email_address(), "msmith@asymmetrik.com", "Extraction from file lines failed")

    def tearDown(self):
        os.remove(os.path.join(self.input_directory, "test1.txt"))
        os.remove(os.path.join(self.input_directory, "test2.txt"))

