class order_processing:
    def place_order(self, foods):
        
        total = 0
        orders = []
        while True:
            choice = input("Enter the food item you want to order (or 'done' to finish): ")
            if choice in foods:
                orders.append(choice)
                total += foods[choice][1]
                print(f"{choice} added to your order. Current total: {total} Rs")
                
                more = input("Do you want to order more? (yes/no): ")
                if more.lower() != 'yes':
                    break
                
            elif choice.lower() == 'done':
                break
            else:
                print("Invalid choice. Please try again.")
        print("\nYour order:")
        for order in orders:
            print(order, foods[order][1], "Rs")
        print(f"Total amount: {total} Rs")
        return total, orders