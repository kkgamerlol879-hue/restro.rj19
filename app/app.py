from auth.auth import auth
from menu_food.food_menu import menu_food
from order_processing.order_processing import order_processing
from order_processing.takeaway import takeaway_handler
from billing.billing import billing
from table_booking.table_booking import book_table
from file_handler.file_handler import filehandler
from admin_food.admin_food import adminfood
from admin_login.admin import admin  
from getpass import getpass


def main():
    menu = menu_food()
    order_processing_obj = order_processing()
    takeaway_obj = takeaway_handler()
    billing_obj = billing()
    table_booking = book_table()
    file_handler = filehandler()
    admin_food = adminfood()
    admin_obj = admin()
    auth_service = auth()

    while True:
        print("\n============RESTRO.RJ19============")
        print("1. signup")
        print("2. login")
        print("3. exit")
        print("4. admin")

        choice = input("Enter your choice: ")
        if choice == "1":
            auth_service.signup()

        elif choice == "2":
            if auth_service.login():
                print("------------Welcome to the app------------------!")

                # Ask for table booking first
                book_table_choice = input("\nDo you want to book a table? (yes/no): ").lower()
                if book_table_choice == 'yes':
                    table_booking.book_table()

                # Load food items for ordering and show the menu
                foods = menu.show_menu()
                file_handler.show_menu()

                while True:
                    print("\n============RESTRO.RJ19 MENU============")
                    print("1. View Menu")
                    print("2. Place Order")
                    print("3. Book a Table")
                    print("4. Exit")

                    menu_choice = input("Enter your choice: ")
                    if menu_choice == "1":
                        file_handler.show_menu()
                    elif menu_choice == "2":
                        total, orders = order_processing_obj.place_order(foods)

                        # Check for leftover food and offer takeaway option
                        has_leftover, packaging_fee = takeaway_obj.check_leftover_food(orders, foods)
                        takeaway_charges = 0

                        if has_leftover:
                            takeaway_charges = takeaway_obj.apply_takeaway_charges(total, packaging_fee)
                            takeaway_obj.show_takeaway_summary(packaging_fee, takeaway_charges)

                        book_table_choice = input("\nDo you want to book a table? (yes/no): ").lower()
                        if book_table_choice == 'yes':
                            table_booking.book_table()

                        billing_obj.generate_bill(total, takeaway_charges)
                    elif menu_choice == "3":
                        table_booking.book_table()
                    elif menu_choice == "4":
                        print("Exiting the app...")
                        break
                    else:
                        print("Invalid choice! Please try again.")
            else:
                print("Invalid credentials!")

        elif choice == "3":
            print("Exiting app")
            break
        elif choice == "4":
            if admin_obj.admin_login():
                admin_obj.penal()
            else:
                print("Access denied!")
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
  