class User:
    """
    class that generates new instance of users
    """

    #class variables
    user_list = []

    def save_user(self):

    		"""
    		save_account method save accounts into the user_list
    		"""

    		User.user_list.append(self)

    def delete_user(self):

    		"""
    		deletes a saved user account from user list
    		"""

    		User.user_list.remove(self)

    def __init__(self,first_name,last_name,email,password):

    		"""
    		__init__ method that defines properties for our user account>

    		Args:
    				first_name: New user first name.
    				last_name:	New user last name
    				email: New user email 
    				password: New user password
    		"""

    		#instance variables
    		self.first_name = first_name
    		self.last_name = last_name
    		self.email = email
    		self.password = password

    pass 
