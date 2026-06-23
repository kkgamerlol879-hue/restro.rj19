import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "database")
ADMIN_FOOD_PATH = os.path.join(DATA_DIR, "admin_food.json")
FOOD_PATH = os.path.join(DATA_DIR, "food.json")

class adminfood:
    def load_food(self):
        try:
            with open(ADMIN_FOOD_PATH, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_food(self, data):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(ADMIN_FOOD_PATH, "w") as f:
            json.dump(data, f, indent=4)
        with open(FOOD_PATH, "w") as f:
            json.dump(data, f, indent=4)

    def add_food(self):
        foods = self.load_food()
        food_id = int(input("enter a food id:-"))
        name = input("enter a food name:-")
        price = int(input("enter the price of food you add"))

        foods.append({
            "id": food_id,
            "name": name,
            "price": price
        })
        self.save_food(foods)
        print("food added successfully")

    def delete_food(self):
        foods = self.load_food()
        food_id = int(input("enter food id to delete food :-"))

        for idx, food in enumerate(foods):
            if food["id"] == food_id:
                foods.pop(idx)
                self.save_food(foods)
                print("food deleted successfully")
                return

        print("food not found")

    def edit_food(self):
        foods = self.load_food()
        food_id = int(input("enter food id to edit food :-"))

        for food in foods:
            if food["id"] == food_id:
                food["name"] = input("new name:- ")
                food["price"] = int(input("new price"))
                self.save_food(foods)
                print("food updated successfully")
                return

        print("food not found")

    def show_food(self):
        foods = self.load_food()
        if not foods:
            print("No food items found.")
            return

        for food in foods:
            print(food["id"], food["name"], food["price"])

                            