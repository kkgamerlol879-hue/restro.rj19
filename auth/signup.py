import json
import os
from getpass import getpass

BASE_DIR =os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR,"database.txt","signup.json") 

with open(file_path,"r") as file:
    
    users = json.load(file)
    
class auth:
    def signup():
        username = input("Enter username: ")
        password = input("Enter password: ")
        phone_number = input("enter phone number")
        
        with open("database.txt/signup.json","r") as file:
            users = json.load(file)
        
        print("Signup successful!")
        
       
    