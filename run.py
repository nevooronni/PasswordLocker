#!/usr/bin/env python3.6 

from accounts import User
from accounts import Credentials

#creating a new user account
def create_account(first_name,last_name,email,password):
				"""
				function to create new user account
				"""

				new_user = User(first_name,last_name,email,password)
				return new_user

#saving a new user account
def save_account(user):
				"""
				function to save new user account
				"""

				user.save_user()

#dele a user account
def delete_account(user):
				"""
				function to delete a user account
				"""
				user.delete_user()

#login into a user account
def login_user(email,password):
				"""
				function that finds a user accoutn and logs user in
				"""
				return User.find_by(email,password)

#confirm if a user account exists
def check_users(email,password):
				"""
				function that checks to see if a user exists in the list befor calling login_user to
				return the user account
				"""
				return User.user_exist(email,password)


#creates a new credential
def create_credential(account_name,description,password):
				"""
				function to create new credential
				"""
				new_credential = Credentials(account_name,description,password)
				return new_credential

#function that save user credentials
def save_credential(credential):
				"""
				save credential
				"""
				credential.save_credential()

def delete_credential(credential):
				"""
				deletes a credential
				"""
				credential.delete_credential()

def get_credential(name):
				"""
				finds a credential for the user
				"""
				return Credentials.find_by_name(name)

def check_credential(name):
				"""
				checks to find if a credential exists and returns a true/false value
				"""
				return Credentials.credential_check(name)

def list_credentials():
				"""
				returns all of the saved credentials
				"""
				return Credentials.show_credentials()

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
										print("\n")
										print("Enter n to create a new credential, Enter v to view a list of your credentials, Enter s to search/find a credential, Enter b to go back, x to exit the application")
										enter = input()

										if enter == 'n':
												print("New Credentials")
												print("\n")

												print("Enter Name")
												account_name = input()

												print("Enter Description")
												description = input()

												print("Enter Password")
												password2 = input()
												print("\n")

												save_credential(create_credential(account_name,description,password2)) #new credential
												print("\n")
												print("done 100%")
												print("\n")

												print(f"Created credentials account name: {account_name} description: {descripetion} password: {password}")
												print("\n")

										elif enter == 's':
												print("Enter Credential Name")
												credential_name = input()
												if check_credential(credential_name):
														search_credential = get_credential(credential_name)

														print("searching.........")
														print("\n")
														print(f"CREDENTIAL NAME: {search_credential.account_name}")
														print(f"DESCRITPION: {search_credential.description}")
														print(f,"PASSWORD: {search_credential.password}")
														print("\n")
												else:
														print("sorry that credential does not exist! please try again.")				

										elif enter == 'v':
                    		if list_credentials():
                    				print("Here is a list of all your credentials")
                    				print('\n')

                    				for credential in list_credential():
                    						print(f"ACCOUNT NAME: {credential.account_name} DESCRIPTION: {credential.description } PASSWORD: {credential.password}")
                    						print("\n")
                        else:
                        		print("\n")
                            print("You dont have any credentials saved yet!")
                            print("\n'")

										elif enter == 'b':
												main()

										elif enter == 'x':
												print("Nooooooo....don't go!")
												break
										else:
												print("sorry you did not enter either of the code provided above, please enter the code provided above!")
												print("\n")

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

			