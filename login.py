import re

class Creds:
    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email 
    
    def set_creds(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email 
    
    def get_creds(self):
        # Validate the existing username
        if len(self.username) < 7:
            return False, "Username must be at least 7 characters long", self.username
        if not re.search(r'\d', self.username):
            return False, "Username must contain at least one number.", self.username
        
        return True, "Username is valid", self.username
    
    def passcode(self):
        if len(self.password)>8:
            return True, "this is the correct password set up.", self.password
        else:
            return False, "please make sure there are more then 8 string charechters ", self.password
#all of this is outside the function. We use objects to pass into the class or modules of the function to check an input to make sure it works right
# Example usage:

def looping_until_right():
    while True:

        set_creds = input("please enter a username")
        set_passcode= input("please enter a password")

# Initialize the Creds object with the set_creds list
        user = Creds(set_creds, set_passcode)  # *set_creds unpacks the list into the three arguments

# Validate the username
        valid_username, message_username, username = user.get_creds()

        valid_password, message_password, password = user.passcode()

        if valid_username and valid_password:
            print(f"Username '{username} and Password '{password} is valid.")
            break

        else:
            if not valid_username:
                print(f"Error{message_username}")
            if not valid_password:
                print (f"Error {message_password}")
            print("please try again. \n")
            
looping_until_right()

