#!/usr/bin/env python3.6 

from accounts import User

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

def login_user(email,password):
				"""
				function that finds a user accoutn and logs user in 
				"""
				return User.find_by(email,password)

def check_users(email,password):
				"""
				function that checks to see if a user exists in the list befor calling login_user to 
				return the user account
				"""
				return User.user_exist(email,password)

#task function
def main():
				while True:
						print("Welcome to password Locker! the best website to store all of your important acount details use cn - create new account/sign up or l - login to an existing account or x - exit the application")		
						print("\n")
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
								print("\n")

								save_account(create_account(first_name,last_name,email,password)) #new account
								print("\n")
								print("creating...10%...50%.......80%")
								print("done 100%")
								print("\n")

								print(f"Created account for {first_name} {last_name} with email {email}")
								print("\n")

						elif code =='l':
								print("Enter an email address for your user account")
								search_email = input()

								print("Enter a password for your user account")
								search_password = input()

								if check_users(search_email,search_password):
										search_account = login_user(search_email,search_password)

										print(f"searching {search_email}.........")
										print("\n")
										print(f"UserName: {search_account.first_name} {search_account.last_name}")
										print(f"Email Address: {search_account.email}")

								else:
										print("That user account does not exist please sign up t create a new account!")
										print("\n")		

						elif code == 'x':
								print("Nooooooo....don't go!")
								break
						else:
								print("sorry you did not enter either of the codes provided above, please enter the codes provided above!")	
								print("\n")				
		

if __name__ == '__main__':

		main()