import unittest

from evens import even_number_of_evens

class TestEvens(unittest.TestCase): 
    def test_throws_error_if_value_passed_is_not_a_list(self):
        self.assertRaises(TypeError, even_number_of_evens,4)

if __name__ == "__main__ ":  #When a file is running it gets named to main , so when this file name runs and is named main trigger the below function
    unittest.main() #Function needd to start with the word Test or they will be ignored 