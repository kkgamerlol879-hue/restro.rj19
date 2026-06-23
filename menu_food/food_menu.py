import json
import os

class menu_food:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.food_file = os.path.join(self.base_dir, "database", "food.json")

    def show_menu(self):
        pass
    
    def show_menu_food(self):
        
        print("food_menu reached")
        return
        foods = json.load(f)
    
            
    def show_menu(self):
        print("1.  add food ")
        print("2.  view. food ")
        print("3.   exit.  ")        
            
        try:
            with open(self.food_file, "r") as f:
                foods_list = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            foods_list = []

        foods = {food["name"]: [food.get("id"), food.get("price")] for food in foods_list}
        if not foods:
            foods = {
                "Veg Spring Rolls": [1, 50],
                "Chicken Spring Rolls": [2, 80],
                "Mutton Spring Rolls": [3, 100],
                "Fish Spring Rolls": [4, 70],
                "Prawn Spring Rolls": [5, 90],
                "Egg Spring Rolls": [6, 40],
                "Paneer Spring Rolls": [7, 60],
                "Mushroom Spring Rolls": [8, 55],
                "Veg Samosa": [9, 20],
                "Chicken Samosa": [10, 30],
                "Mutton Samosa": [11, 40],
                "Fish Samosa": [12, 25],
                "Prawn Samosa": [13, 30],
                "Egg Samosa": [14, 20],
                "Paneer Samosa": [15, 25],
                "Mushroom Samosa": [16, 30],
                "Veg Pakora": [17, 30],
                "Chicken Pakora": [18, 40],
                "Mutton Pakora": [19, 50],
                "Fish Pakora": [20, 35],
                "Prawn Pakora": [21, 45],
                "Egg Pakora": [22, 25],
                "Paneer Pakora": [23, 30],
                "Mushroom Pakora": [24, 35],
                "Veg Cutlet": [25, 40],
                "Chicken Cutlet": [26, 60],
                "Mutton Cutlet": [27, 80],
                "Fish Cutlet": [28, 50],
                "Prawn Cutlet": [29, 70],
                "Egg Cutlet": [30, 30],
                "Paneer Cutlet": [31, 40],
                "Mushroom Cutlet": [32, 45],
            }

        print("\n-------------------Welcome to our restaurant!----------------------")
        for name, data in foods.items():
            print(name, data[1], "rs")
        print("\n--------------------Here is our starter menu:-----------------")
        
        print("\n1. Veg Spring Rolls",50,"Rs")
        print("\n2. Chicken Spring Rolls",80,"Rs")
        print("\n3. Mutton Spring Rolls",100,"Rs")
        print("\n4. Fish Spring Rolls",70,"Rs")
        print("\n5. Prawn Spring Rolls",90,"Rs")
        print("\n6. Egg Spring Rolls",40,"Rs")
        print("\n7. Paneer Spring Rolls",60,"Rs")
        print("\n8. Mushroom Spring Rolls",55,"Rs")
        print("\n9. Veg Samosa",20,"Rs")
        print("\n10. Chicken Samosa",30,"Rs")
        print("\n11. Mutton Samosa",40,"Rs")
        print("\n12. Fish Samosa",25,"Rs")
        print("\n13. Prawn Samosa",30,"Rs")
        print("\n14. Egg Samosa",20,"Rs")
        print("\n15. Paneer Samosa",25,"Rs")
        print("\n16. Mushroom Samosa",30,"Rs")
        print("\n17. Veg Pakora",30,"Rs")
        print("\n18. Chicken Pakora",40,"Rs")
        print("\n19. Mutton Pakora",50,"Rs")
        print("\n20. Fish Pakora",35,"Rs")
        print("\n21. Prawn Pakora",45,"Rs")
        print("\n22. Egg Pakora",25,"Rs")
        print("\n23. Paneer Pakora",30,"Rs")
        print("\n24. Mushroom Pakora",35,"Rs")
        print("\n25. Veg Cutlet",40,"Rs")
        print("\n26. Chicken Cutlet",60,"Rs")
        print("\n27. Mutton Cutlet",80,"Rs")
        print("\n28. Fish Cutlet",50,"Rs")
        return foods
        print("\n29. Prawn Cutlet",70,"Rs")
        print("\n30. Egg Cutlet",30,"Rs")
        print("\n31. Paneer Cutlet",40,"Rs")
        print("\n32. Mushroom Cutlet",45,"Rs")

    def show_menu_food_(self):
        
        
        print("\n------------main_courese_menu------------------")
        
        print("\n33. Veg Biryani",80,120,"Rs")
        print("\n34. Chicken Biryani",110,160,"Rs")
        print("\n35. Mutton Biryani",140,190,"Rs")
        print("\n36. Fish Biryani",90,140,"Rs")
        print("\n37. Prawn Biryani",120,170,"Rs")
        print("\n38. Egg Biryani",50,110,"Rs")
        print("\n39. Paneer Biryani",80,130,"Rs")
        print("\n40. Mushroom Biryani",75,125,"Rs")
        print("\n41. Veg Fried Rice",50,100,"Rs")
        print("\n42. Chicken Fried Rice",100,150,"Rs")
        print("\n43. Mutton Fried Rice",130,180,"Rs")
        print("\n44. Fish Fried Rice",80,130,"Rs")
        print("\n45. Prawn Fried Rice",110,160,"Rs")
        print("\n46. Egg Fried Rice",40,90,"Rs")
        print("\n47. Paneer Fried Rice",70,120,"Rs")
        print("\n48. Mushroom Fried Rice",65,115,"Rs")
        print("\n49. Veg Noodles",40,90,"Rs")
        print("\n50. Chicken Noodles",90,140,"Rs")
        print("\n51. Mutton Noodles",120,170,"Rs")
        print("\n52. Fish Noodles",70,120,"Rs")
        print("\n53. Prawn Noodles",100,150,"Rs")
        print("\n54. Egg Noodles",50,100,"Rs")
        print("\n55. Paneer Noodles",60,110,"Rs")
        print("\n56. Mushroom Noodles",55,105,"Rs")
        print("\n57. Veg Soup",30,80,"Rs")
        print("\n58. Chicken Soup",80,130,"Rs")
        print("\n59. Mutton Soup",110,160,"Rs")
        print("\n60. Fish Soup",60,110,"Rs")
        print("\n61. Prawn Soup",90,140,"Rs")
        print("\n62. Egg Soup",20,70,"Rs")
        print("\n63. Paneer Soup",40,90,"Rs")
        print("\n64. Mushroom Soup",45,85,"Rs")
        
        
        def show_menu_food_cold_drink(self):
            
            print("\n----------cold drink menu------------------")
            
            print("\n65.coke",30,"Rs")
            print("\n66.pepsi",30,"Rs")
            print("\n67.sprite",30,"Rs")
            print("\n68.fanta",30,"Rs")
            print("\n69.mountain dew",30,"Rs")
            print("\n70.7up",30,"Rs")
            print("\n71.mirinda",30,"Rs")
            print("\n72.thums up",30,"Rs")
            print("\n73.limca",30,"Rs")
            print("\n74.maaza",30,"Rs")
            print("\n75.slice",30,"Rs")
            print("\n76.rooh afza",30,"Rs")
            print("\n77.red bull",130,"Rs")
            print("\n78.monster",130,"Rs")
            print("\n79.energy drink",50,"Rs")
            print("\n80. orange juice",30,"Rs")
            print("\n81.water",30,"Rs")
            
            def show_menu_food_dessert(self):
                
                print("\n----------------dessert menu------------------")
                
                print("\n82.ice cream",50,"Rs")
                print("\n83.cake",100,"Rs")
                print("\n84.pastry",80,"Rs")
                print("\n85.brownie",70,"Rs")
                print("\n86.cookie",30,"Rs")
                print("\n87.donut",40,"Rs")
                print("\n88.muffin",60,"Rs")
                print("\n89.cupcake",50,"Rs")
                print("\n90.pudding",90,"Rs")
                print("\n91.custard",80,"Rs")
                print("\n92.kheer",70,"Rs")
                print("\n93.gulab jamun",60,"Rs")
                print("\n94.rasgulla",50,"Rs")
                print("\n95.jalebi",40,"Rs")
                print("\n96.ladoo",30,"Rs")
                print("\n97.barfi",20,"Rs")
                print("\n98.soan papdi",10,"Rs")

                def show_menu_food_beverage(self):

                    print("\n----------------beverage menu------------------")
                    print("\n99.tea",20,"Rs")
                    print("\n100.coffee",30,"Rs")
                    print("\n101.hot chocolate",40,"Rs")
                    print("\n102.milk",25,"Rs")
                    print("\n103.lemonade",30,"Rs")
                    print("\n104.smoothie",50,"Rs")
                    print("\n105.milkshake",60,"Rs")
                    print("\n106.juice",35,"Rs")
                    print("\n107.water",10,"Rs")
                    print("\n108.coke",20,"Rs")
                    
                    
                    def show_menu_food_snack(self):
                        print("\n----------------snack menu------------------")
                        
                        print("\n109.samosa",20,"Rs")
                        print("\n110.kachori",30,"Rs")
                        print("\n111.pakora",40,"Rs")
                        print("\n112.bhajiya",25,"Rs")
                        print("\n113.aloo tikki",30,"Rs")
                        print("\n114.vada pav",50,"Rs")
                        print("\n115.pav bhaji",60,"Rs")
                        print("\n116.dabeli",35,"Rs")
                        print("\n117.misal pav",10,"Rs")
                        print("\n118.vada pav",20,"Rs")
                        print("\n119.dabeli",40,"Rs")
                        print("\n120.misal pav",50,"Rs")

                        def show_menu_food_sandwich(self):
                            
                            print("\n----------------sandwich menu------------------")
                            
                            
                            print("\n121.veg sandwich",50,"Rs")
                            print("\n122.chicken sandwich",80,"Rs")
                            print("\n123.mutton sandwich",100,"Rs")
                            print("\n124.fish sandwich",70,"Rs")
                            print("\n125.prawn sandwich",90,"Rs")
                            print("\n126.egg sandwich",40,"Rs")
                            print("\n127.paneer sandwich",60,"Rs")
                            print("\n128.mushroom sandwich",55,"Rs")
                            

                            def show_menu_food_pizza(self):
                                print("\n----------------pizza menu------------------")
                                
                                
                                
                                print("\n129.veg pizza",100,"Rs")
                                print("\n130.chicken pizza",150,"Rs")
                                print("\n131.mutton pizza",200,"Rs")
                                print("\n132.fish pizza",120,"Rs")
                                print("\n133.prawn pizza",170,"Rs")
                                print("\n134.egg pizza",80,"Rs")
                                print("\n135.paneer pizza",110,"Rs")
                                print("\n136.mushroom pizza",90,"Rs")
                                

                                def show_menu_food_burger(self):
                                    
                                    print("\n----------------burger menu------------------")
                                    
                                    print("\n137.veg burger",50,"Rs")
                                    print("\n138.chicken burger",80,"Rs")
                                    print("\n139.mutton burger",100,"Rs")
                                    print("\n140.fish burger",70,"Rs")
                                    print("\n141.prawn burger",90,"Rs")
                                    print("\n142.egg burger",40,"Rs")
                                    print("\n143.paneer burger",60,"Rs")
                                    print("\n144.mushroom burger",55,"Rs")

                                    def show_menu_food_pasta(self):
                                        
                                        print("\n----------------pasta menu------------------")
                                        
                                        print("\n145.veg pasta",80,"Rs")
                                        print("\n146.chicken pasta",120,"Rs")
                                        print("\n147.mutton pasta",150,"Rs")
                                        print("\n148.fish pasta",100,"Rs")
                                        print("\n149.prawn pasta",130,"Rs")
                                        print("\n150.egg pasta",70,"Rs")
                                        print("\n151.paneer pasta",90,"Rs")
                                        print("\n152.mushroom pasta",85,"Rs")
                                        

                                        def show_menu_food_rice(self):
                                            
                                            
                                            print("\n----------------rice menu------------------")
                                            
                                            print("\n153.veg rice",60,"Rs")
                                            print("\n154.chicken rice",110,"Rs")
                                            print("\n155.mutton rice",140,"Rs")
                                            print("\n156.fish rice",90,"Rs")
                                            print("\n157.prawn rice",120,"Rs")
                                            print("\n158.egg rice",50,"Rs")
                                            print("\n159.paneer rice",80,"Rs")
                                            print("\n160.mushroom rice",75,"Rs")
                                            

                                            print("\n-----------menu----------------")
                                            for key, value in menu_food.items():
                                                print(key, value[0], value[1], "Rs")
                                                return menu_food