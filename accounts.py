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

    @classmethod
    def find_by(cls,email,password):
        """
        Takes in an email and password and return that user with those details.

        Args:
            email: user email
            password: user password
        Returns :
            user account of a person that matches those details.
        """

        for user in cls.user_list:
            if user.email == email and user.password == password:
                return user

    @classmethod
    def user_exist(cls,email,password):
        """
        authenticates if a user accounts exists
        Args:
            email: user email address
            password: user password
        Returns :
            Boolean: True or false depending on whether the user account exists
        """
        for user in cls.user_list:
            if user.email == email and user.password == password:
                return True

    @classmethod
    def list_users(cls):
        """
        returns the list of users
        """

        return cls.user_list


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


class Credentials:
    """
    class that generate new instances of credentials
    """

    #class variable that can be accessed by all instances of the class used to store our created credential accounts objects
    credential_list = []    

    def save_credential(self):

        """
        this method save a new credential account for the user
        """

        Credentials.credential_list.append(self)

    def delete_credential(self):
        """
        method that deletes a credential form a the users credential list
        """

        Credentials.credential_list.remove(self)

    @classmethod    
    def find_by_name(cls,name):
        """
        method which takes an input and returns a credential that mathces the input
        
        Args:
            name: name of the specific user credential/account the user wants to find
        Returns:
            credential of the user that matches.
        """

        for credential in cls.credential_list:
            if credential.account_name == name:
                return credential  


    def __init__(self,account_name,description,password):

        """
        __init__ deines for us properties four our credentials objects
        
        Args:
            account_name: name of the account user wants to store/generate pasword.
            description: succint description of the specific account/imporotant details to remember.
            password: password for that specific user account custom or generated for the user.
        """

        #instance variable that take up the acountname, description, password of our new credential
        self.account_name = account_name
        self.description = description
        self.password = password


    pass 
