import unittest
from accounts import user

class TestAccounts(unittest.TestCase):

		"""
		Test class that define test cases for the user class behaviours.

		Args:
				unittest.TestCase: TestCase class that helps in creating test cases

		"""

		def setUp(self):
				"""
				set up to run before each test cases.
				"""
				self.new_user = user("Nevill","Oronni","nevooronni@gmail.com","speeds01") 


		def test_init(self):
				"""
				test_init test case to test if the object is initialized properly
				"""

				self.assertEqual(self.new_user.first_name,"Nevill")
				self.assertEqual(self.new_user.last_name,"Oronni")
				self.assertEqual(self.new_user.email,"nevooronni@gmail.com")
				self.assertEqual(self.new_user.password,"speeds01")

if __name__ == '__main__':
	unittest.main()