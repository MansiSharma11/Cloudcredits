import bcrypt
import getpass

# In-memory storage for users (in a real-world application, this would be a database)
users_db = {}

# Function to register a user
def register_user():
    print("Register a new user:")
    username = input("Enter username: ")
    
    # Make sure the username is not already taken
    if username in users_db:
        print("Username already exists! Please choose another one.")
        return

    # Securely handle the password
    password = getpass.getpass("Enter password: ")
    password_confirmation = getpass.getpass("Confirm password: ")

    if password != password_confirmation:
        print("Passwords do not match!")
        return

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Store the user in the database
    users_db[username] = hashed_password
    print(f"User {username} registered successfully.")

# Function to login a user
def login_user():
    print("Login to your account:")
    username = input("Enter username: ")

    if username not in users_db:
        print("Username not found.")
        return

    # Securely get the password input
    password = getpass.getpass("Enter password: ")

    # Verify the entered password against the stored hashed password
    stored_password = users_db[username]
    if bcrypt.checkpw(password.encode('utf-8'), stored_password):
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Incorrect password.")

# Main function to handle user interactions
def main():
    while True:
        print("\n1. Register User")
        print("2. Login User")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please choose again.")

# Run the program
if __name__ == "__main__":
    main()
