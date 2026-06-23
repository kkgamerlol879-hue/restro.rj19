import json
import os
from getpass import getpass

BASE_DIR =os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR,"database.txt","signup.json") 

with open(file_path,"r") as file:
    
    users = json.load(file)
    
class auth:
    
       
    def login():
        username = input("Enter username: ")
        password = getpass("Enter password: ")
        phone_number = input("enter phone")
         
        with open("database.txt/signup.json","r") as file:
            users = json.load(file)

        for user in users:
            if user["username"] == username and user["password"] == password:
                print("login successfuly")
                return True
        print("invelid member sorry try after signup:-")
        return False