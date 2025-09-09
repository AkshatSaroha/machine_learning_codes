class AuthenticationError(Exception):
    def _init_(self, message="Authentication failed. Please check your credentials."):
        self.message = message
        super()._init_(self.message)


def login(username, password):
    correct_username = "admin"
    correct_password = "password123"

    if username != correct_username or password != correct_password:
        raise AuthenticationError("Wrong credentials")

try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    login(username, password)
    print("Login successful!")

except AuthenticationError as e:
    print(e)