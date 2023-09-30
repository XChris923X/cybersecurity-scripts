# password_checker.py

def is_valid_password(password):
    """
    Check if a password is at least 8 characters long.
    
    Args:
        password (str): The password to check.
    
    Returns:
        bool: True if the password is valid, False otherwise.
    """
    return len(password) >= 8

if __name__ == "__main__":
    password = input("Enter a password: ")
    
    if is_valid_password(password):
        print("Password is valid.")
    else:
        print("Password is too short. It must be at least 8 characters long.")
 
