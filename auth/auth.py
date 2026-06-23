import json
import os
from getpass import getpass

class auth:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.signup_file = os.path.join(base_dir, "database", "signup.json")
        os.makedirs(os.path.dirname(self.signup_file), exist_ok=True)
        if not os.path.exists(self.signup_file):
            with open(self.signup_file, "w") as file:
                json.dump([], file)

    def _load_users(self):
        try:
            with open(self.signup_file, "r") as file:
                users = json.load(file)
                return users if isinstance(users, list) else []
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_users(self, users):
        with open(self.signup_file, "w") as file:
            json.dump(users, file, indent=2)

    def _username_exists(self, username):
        """Check if username already exists"""
        users = self._load_users()
        for user in users:
            if user.get("username") == username:
                return True
        return False

    def _phone_exists(self, phone_number):
        """Check if phone number already exists"""
        users = self._load_users()
        for user in users:
            if user.get("phone_number") == phone_number:
                return True
        return False

    def signup(self):
        print("\n=============== SIGNUP ===================")
        
        # Get username with validation
        while True:
            username = input("Enter username: ").strip()
            if not username:
                print("✗ Username cannot be empty!")
                continue
            
            if self._username_exists(username):
                print(f"✗ Username '{username}' already exists! Please choose a different username.")
                continue
            
            break
        
        # Get phone number with validation
        while True:
            phone_number = input("Enter phone number: ").strip()
            if not phone_number:
                print("✗ Phone number cannot be empty!")
                continue
            
            if self._phone_exists(phone_number):
                print(f"✗ Phone number '{phone_number}' already registered! Please use a different phone number.")
                continue
            
            break
        
        password = getpass("Enter password: ")

        users = self._load_users()
        users.append({
            "username": username,
            "password": password,
            "phone_number": phone_number,
        })
        self._save_users(users)

        print("\n✓ Signup successful! You can now login with your credentials.")
        print(f"Username: {username}")
        print(f"Phone Number: {phone_number}\n")

    def login(self):
        print("\n=============== LOGIN ===================")
        username = input("Enter username: ").strip()
        password = getpass("Enter password: ")
        phone_number = input("Enter phone number: ").strip()

        users = self._load_users()
        for user in users:
            if (user.get("username") == username and 
                user.get("password") == password and 
                user.get("phone_number") == phone_number):
                print("\n✓ Login successful!")
                return True

        print("\n✗ Invalid credentials! Username, password, or phone number is incorrect.")
        print("Please try again or signup if you don't have an account.\n")
        return False