from admin_food.admin_food import adminfood
from .attendance import attendance_tracker
from billing.daily_analytics import daily_analytics
from .salary import salary_management
import json
import os
from getpass import getpass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
admin_db_path = os.path.join(BASE_DIR, "..", "database", "admin.json")

class admin:
    def __init__(self):
        self.admin_food = adminfood()
        self.attendance = attendance_tracker()
        self.analytics = daily_analytics()
        self.salary_management = salary_management()
        self.current_admin_id = None
        self.current_experience_year = None

    def admin_login(self):
        """
        Admin login function with password, mobile number, batch number, and experience year
        """
        print("\n=============== Admin Login ===================")
        admin_id = input("Enter admin ID: ").strip()
        password = getpass("Enter password: ").strip()
        mobile_number = input("Enter mobile number: ").strip()
        batch_number = input("Enter batch number: ").strip()
        experience_year = input("Enter experience year: ").strip()

        try:
            with open(admin_db_path, "r") as file:
                admins = json.load(file)
        except FileNotFoundError:
            print("Admin database not found!")
            return False

        for admin_data in admins:
            if (str(admin_data["admin_id"]) == admin_id and 
                admin_data["password"] == password and 
                admin_data["mobile_number"] == mobile_number and 
                admin_data["batch_number"] == batch_number and 
                str(admin_data["experience_year"]) == experience_year):
                print(f"\n✓ Login successful! Welcome Admin {admin_id}")
                self.current_admin_id = admin_id
                self.current_experience_year = int(admin_data["experience_year"])
                # Initialize salary if not exists
                self.salary_management.initialize_salary(self.current_admin_id, self.current_experience_year)
                return True

        print("\n✗ Invalid credentials! Login failed.")
        return False

    def penal(self):
        """
        Admin panel - accessible only after successful login
        """
        while True:
            
            print("\n=============== Admin Panel ===================")
            
            print("1. Add food")
            print("2. Delete food")
            print("3. Edit food ")
            print("4. Show food")
            print("5. Mark Attendance")
            print("6. View My Attendance")
            print("7. Daily Customer Analytics")
            print("8. Monthly Summary")
            print("9. View All Customers")
            print("10. View My Salary")
            print("11. Update Performance")
            print("12. View Salary Guide")
            print("13. View All Salaries")
            print("14. Logout")
            
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.admin_food.add_food()
                
            elif choice == "2":  
                self.admin_food.delete_food()  
                
            elif choice == "3":
                self.admin_food.edit_food()
                
            elif choice == "4":
                self.admin_food.show_food()
            
            elif choice == "5":
                self.attendance.mark_attendance(self.current_admin_id)
            
            elif choice == "6":
                self.attendance.view_attendance(self.current_admin_id)
                self.attendance.get_attendance_summary(self.current_admin_id)
            
            elif choice == "7":
                self.analytics.get_daily_customers()
            
            elif choice == "8":
                self.analytics.get_monthly_summary()
            
            elif choice == "9":
                self.analytics.view_all_customers()
            
            elif choice == "10":
                self.salary_management.get_salary_details(self.current_admin_id)
            
            elif choice == "11":
                self.salary_management.update_performance(self.current_admin_id)
            
            elif choice == "12":
                self.salary_management.salary_guide()
            
            elif choice == "13":
                self.salary_management.get_salary_summary()
                
            elif choice == "14":
                print("Logging out...")
                break
            else:
                print("Invalid choice! Please try again.")
                       