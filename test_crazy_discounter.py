import unittest
#you will need to import crazy_discounter so we can acess its function and run tests on it

class Test_discount_remover(unittest.TestCase):

    def test_remove_discount_lower(self):
        # calls the remove_discount_from function from the crazy discounter program with test value 100 and stores result
        test_100 = crazy_discounter.remove_discount_from(100) #calls the remove_discount_from function
        #here we check if the result is 85
        self.assertEqual(85, test_100)

    #modify this function to do the same as above but with a test case of 500 instead of 1000
    def test_something_else(self):
        self.assertEqual(True, False)

    #write a third function with your third test case


if __name__ == '__main__':
    unittest.main()
