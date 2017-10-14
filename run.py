#!/usr/bin/env python3.6 

from accounts import user

		#creating a new user account
		def create_account(first_name,last_name,email,password):
				"""
				function to create new user account
				"""

				new_user = User(first_name,last_name,email,password)
				return new_user

		def save_account(user):
				"""
				function to save new user account
				"""

				user.save_user()

		def delete_account(user):
				"""
				function to delete a user account
				"""
				user.delete_user()

		def login_user(user):
				"""
				function that finds a user accoutn and logs user in 
				"""
				return User.find_by(email,password)


		#task function
		def main():
				while True:
						print("Welcome to password Locker! the best website to store all of your important acount details use cn - create new account or l - login to an existing account")		

						code = input().lower()

						if code == 'cn':
								print("New Account")
								print("\n")

								print("Enter First Name")
								first_name = input()

								print("Enter Last Name")
								last_name = input()

								print("Enter Email Address")
								email = input()

								print("Enter Password")
								password = input()

								save_account(create_account(first_name,last_name,email,password)) #new account
								print("\n")
								print("creating......10%")
								print("creating......50%")
								print("........80%")
								print("done 100%")
								Print("\n")
								print(f,"Created account for {first_name} {last_name} with email {email}")
								print("\n")

						elif code = 'l':
								print("Enter an email address for your user account")
								search_email = input()

								print("Enter a password for your user account")
								search_password = input()

								if login_user():
										search_account = 




