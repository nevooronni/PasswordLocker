import unittest
from accounts import User

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
				self.new_user = User("Nevill","Oronni","nevooronni@gmail.com","speeds01") 

		def tearDown(self):
				"""
				method that cleans up after each test has run.
				"""
				User.user_list = []

		def test_init(self):
				"""
				test_init test case to test if the object is initialized properly
				"""

				self.assertEqual(self.new_user.first_name,"Nevill")
				self.assertEqual(self.new_user.last_name,"Oronni")
				self.assertEqual(self.new_user.email,"nevooronni@gmail.com")
				self.assertEqual(self.new_user.password,"speeds01")


		def test_save_user(self):
				"""
				test_save_account test case to test if the new account object is saved into the contact list
				"""
				self.new_user.save_user()
				self.assertEqual(len(User.user_list),1)

		def test_save_user_many_times(self):
				"""
				test_save_account_many_times sees if we can save many contacts to our list
				"""
				self.new_user.save_user()
				test_user = User("Steven","Gerrard","stevenGerrard@gmail.com","gerrard01")
				test_user.save_user()
				self.assertEqual(len(User.user_list),2)		

		def test_delete_user(self):
				"""
				method tests whether we can delete a user account form our user list
				"""
				self.new_user.save_user()
				test_user = User("Steven","Gerrard","stevenGerrard@gmail.com","gerrard01")
				test_user.save_user()

				self.new_user.delete_user()
				self.assertEqual(len(User.user_list),1)

		def test_login(self):
				"""
				test to check if the user can login with his name and email
				and display their account information
				"""

				self.new_user.save_user()
				test_user = User("Steven","Gerrard","stevenGerrard@gmail.com","gerrard01")
				test_user.save_user()

				login_user = User.find_by("stevenGerrard@gmail.com","gerrard01")
				self.assertEqual(login_user.first_name,test_user.first_name)


if __name__ == '__main__':
    unittest.main()


