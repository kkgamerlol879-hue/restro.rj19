import json
import os

class filehandler:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.menu_file = os.path.join(base_dir, "menu.txt")
        self.food_file = os.path.join(base_dir, "database", "food.json")

    def show_menu(self):
        if os.path.exists(self.menu_file):
            with open(self.menu_file, "r") as file:
                menu = file.read()
                print(menu)
                return

        if os.path.exists(self.food_file):
            with open(self.food_file, "r") as file:
                foods = json.load(file)
            print("\n--- Menu ---")
            for food in foods:
                print(food.get("id"), food.get("name"), food.get("price"), "Rs")
            return

        print("No menu file found. Please create 'menu.txt' or add items to 'database/food.json'.")
            
            
            
    def save_order(self, order_details):
        with open("orders.txt", "a") as file:
            file.write(order_details + "\n")
            
            
            
    def save_booking(self, booking_details):
        with open("table_bookings.txt", "a") as file:
            file.write(booking_details + "\n")
            
            
            
    def save_user(self, user_details):
        with open("database.txt", "a") as file:
            file.write(user_details + "\n")
            
            
            
    def read_users(self):
        with open("database.txt", "r") as file:
            users = file.read()
            return users
        
        
    def read_orders(self):
        with open("orders.txt", "r") as file:
            orders = file.read()
            return orders
        
        
        
    def read_bookings(self):
        with open("table_bookings.txt", "r") as file:
            bookings = file.read()
            return bookings
        
        
        
    def read_menu(self):
        with open("menu.txt", "r") as file:
            menu = file.read()
            return menu     
        
        
        
        def save_menu(self, menu_details):
            with open("menu.txt", "a") as file:
                file.write(menu_details + "\n")  
                
                   
                
    