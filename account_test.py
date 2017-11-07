import unittest
import pyperclip 
from accounts import User
from accounts import Credentials

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

		def test_get_user(self):
				"""
				test to check if you can find a user by their email and password
				"""

				self.new_user.save_user()
				test_user = User("Steven","Gerrard","stevenGerrard@gmail.com","gerrard01")
				test_user.save_user()

				login_user = User.find_by("stevenGerrard@gmail.com","gerrard01")
				self.assertEqual(login_user.email,test_user.email)

		def test_user_exists(self):
				"""
				test to see if a user account exists
				"""

				self.new_user.save_user()
				test_user = User("Steven","Gerrard","stevenGerrard@gmail.com","gerrard01")
				test_user.save_user()

				user_exists = User.user_exist("stevenGerrard@gmail.com","gerrard01")
				self.assertTrue(user_exists)

		def test_list_all_users(self):
				"""
				retuns a list of all the users saved in the app
				"""

				self.assertEqual(User.list_users(),User.user_list)
		
#subclass inherits methods and variables from parent class
class TestCredentials(unittest.TestCase):
		"""
		Test case defines test cases for the credentials class behaviours.

		Args:
				unittest.TestCase: TestCase class that helps in creating test cases
		"""

		def setUp(self):
				"""
				set up method to run before each test cases.
				"""
				self.new_credential = Credentials("Facebook","social media account","space\11")

		def tearDown(self):
				"""
				clean/refreshes after each test case runs
				"""

				Credentials.credential_list = []			

		def test_init(self):
				"""
				this tests if the object is initialized properly
				"""

				self.assertEqual(self.new_credential.account_name,"Facebook")
				self.assertEqual(self.new_credential.description,"social media account")
				self.assertEqual(self.new_credential.password,"space\11")

		def test_save_credential(self):
				"""
				this test method test to see whether we can save a new credential account
				"""
				self.new_credential.save_credential() #save the credential
				self.assertEqual(len(Credentials.credential_list),1)

		def test_save_many_credentials(self):
				"""
				test method to check if we can save multiple credentials
				"""
				self.new_credential.save_credential()
				test_credential = Credentials("Twitter","instant messenger","2222")
				test_credential.save_credential()

				self.assertEqual(len(Credentials.credential_list),2)

		def test_delete_credential(self):
				"""
				method that deletes user credentials account from a list
				"""
				self.new_credential.save_credential()
				test_credential = Credentials("Twitter","instant messenger","2222")
				test_credential.save_credential()

				self.new_credential.delete_credential() #deletes a credenial
				self.assertEqual(len(Credentials.credential_list),1)

		def test_find_credential(self):
				"""
				method to test whether we can find the specific credential in our credential list
				"""
				self.new_credential.save_credential()
				test_credential = Credentials("Twitter","instant messenger","2222")
				test_credential.save_credential()

				find_credential = Credentials.find_by_name("Twitter")
				self.assertEqual(find_credential.description,test_credential.description)

		def test_credential_exists(self):
				"""
				test to see if a credential is in the credentials list
				"""

				self.new_credential.save_credential()
				test_credential = Credentials("Twitter","instant messenger","2222")
				test_credential.save_credential()

				credential_exist = Credentials.credential_check("Twitter")
				self.assertTrue(credential_exist)

		def test_show_credentials(self):
				"""
				method will show a list of the credentials
				"""

				self.assertEqual(Credentials.show_credentials(),Credentials.credential_list)

		#def test_copy_password(self):
				#"""
				#test to see if I can copy my credentials to the clipboard
				#"""

				#self.new_credential.save_credential()
				#Credentials.copy_password("Twitter")

				#self.assertEqual(self.new_credential.password,pyperclip.paste()) 

		def test_generate_random_password(self):
			'''
			test to see if method can auto generate passwords
			'''
			generate_random_password = self.new_credential.generate_random_password()
			self.assertEqual(len(generate_random_password),8)

#if statement if this file is run then unittest should gather all of the test modules and execute them.
if __name__ == '__main__':
    unittest.main(verbosity=2)


