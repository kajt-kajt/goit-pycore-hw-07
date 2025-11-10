"""
Tests to ensure project works correctly
"""

from unittest import main as unittest_main
from unittest import TestCase
from unittest.mock import patch
import io
import sys
from main import main


class TestBot(TestCase):
    """
    TestCase to test bot interactively
    """

    @patch('builtins.input', side_effect=['hello',
                                          'exit'])
    def test_hello(self, mock_input):
        """
        Just hello and exit
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "How can I help you?\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(2):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['add Peter 0123456789',
                                          'all',
                                          'exit'])
    def test_add_contact_all(self, mock_input):
        """
        Add one contact and verify through all that it exists
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Contact added.\n"
                         + "Peter: 0123456789\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(3):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['add Peter 0123456789',
                                          'phone Peter',
                                          'exit'])
    def test_add_contact_phone(self, mock_input):
        """
        Add new contact and try to get it back with phone
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Contact added.\n"
                         + "0123456789\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(3):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['hello',
                                          'HELLO', 
                                          'Hello', 
                                          'Hello ufkjfkd', 
                                          'hello and more', 
                                          'close'])
    def test_hello_misc(self, mock_input):
        """
        Various options for hello: different case, additional parameters etc.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "How can I help you?\n"*5
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(6):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['add', 
                                          'add Peter', 
                                          'add Peter 123456787 fdfdfd', 
                                          'all', 
                                          'exit'])
    def test_add_contact_misc(self, mock_input):
        """
        Wrong number of arguments for add contact
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Wrong argument(-s) provided. Try again.\n"*3
                         + "\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(5):
            mock_input.assert_called_with("Enter a command: ")

    @patch('builtins.input', side_effect=['gdhgdhs',
                                          'ghghgh jgjj',
                                          '',
                                          'exit'])
    def test_random_input(self, mock_input):
        """
        Strings that are not commands at all.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Invalid command.\n"*3
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(4):
            mock_input.assert_called_with("Enter a command: ")

    @patch('builtins.input', side_effect=['all', 
                                          'phone', 
                                          'phone abcd', 
                                          'phone abcd fgfgfgf', 
                                          'exit'])
    def test_all_phone_misc(self, mock_input):
        """
        all and phone with wrong arguments and empty base
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n\n"
                         + "Wrong argument(-s) provided. Try again.\n"
                         + "No such contact found.\n"*2
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(5):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['add Peter 0123456789',
                                          'change Peter 9876543210', 
                                          'phone Peter', 
                                          'exit'])
    def test_change(self, mock_input):
        """
        Basic scenario for changing phone number in database
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Contact added.\n"
                         + "Contact updated.\n"
                         + "9876543210\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(4):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['change',
                                          'change Peter',
                                          'change Peter 9876543210', 
                                          'all',
                                          'close'])
    def test_change_misc(self, mock_input):
        """
        Various weird scenarios for changing phone number in database
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Wrong argument(-s) provided. Try again.\n"*2
                         + "ERROR: contact 'Peter' does not exist!\n"
                         + "\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(5):
            mock_input.assert_called_with("Enter a command: ")    

##### add test for wrong format of phone number to add_contact and change_contact
##### add test for adding second number for user with add_contact


if __name__ == '__main__':
    unittest_main()
