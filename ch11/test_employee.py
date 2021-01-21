# Ex 11-3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test cases for the Employee class."""

    def setUp(self):
        """Set up an employee instance for testing."""
        self.employee = Employee('Scott', 'Renegado', 40000)

    def test_give_default_raise(self):
        """Give a raise of $5,000."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 45000)

    def test_give_custom_raise(self):
        """Give a raise of, say, $10,000."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 50000)


if __name__ == '__main__':
    unittest.main()