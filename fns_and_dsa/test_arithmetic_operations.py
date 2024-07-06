# test_arithmetic_operations.py

import unittest
from arithmetic_operations import perform_operation

class TestArithmeticOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(perform_operation(3, 2, 'add'), 5.0)
    
    def test_subtract(self):
        self.assertEqual(perform_operation(10, 4, 'subtract'), 6.0)
    
    def test_multiply(self):
        self.assertEqual(perform_operation(7, 3, 'multiply'), 21.0)
    
    def test_divide(self):
        self.assertEqual(perform_operation(8, 2, 'divide'), 4.0)
    
    def test_divide_by_zero(self):
        self.assertEqual(perform_operation(8, 0, 'divide'), "Error: Division by zero is not allowed.")
    
    def test_invalid_operation(self):
        self.assertEqual(perform_operation(5, 2, 'mod'), "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'.")

if __name__ == '__main__':
    unittest.main()

