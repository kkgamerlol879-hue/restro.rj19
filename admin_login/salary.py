import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
salary_db_path = os.path.join(BASE_DIR, "..", "database", "salary.json")
admin_db_path = os.path.join(BASE_DIR, "..", "database", "admin.json")

class salary_management:
    def __init__(self):
        self.db_path = salary_db_path
        self.admin_db_path = admin_db_path
        # Salary brackets based on experience
        self.base_salary_2_years = 20000
        self.base_salary_5_years = 50000
        self.performance_bonus_percentage = 5  # 5% per performance level
    
    def calculate_base_salary(self, experience_years):
        """Calculate base salary based on experience"""
        if experience_years >= 5:
            return self.base_salary_5_years
        elif experience_years >= 2:
            return self.base_salary_2_years
        else:
            # Less than 2 years - trainee salary
            return 15000
    
    def initialize_salary(self, admin_id, experience_years):
        """Initialize salary record for admin"""
        admin_id_str = str(admin_id)
        try:
            with open(self.db_path, "r") as file:
                salary_records = json.load(file)
        except FileNotFoundError:
            salary_records = []
        
        # Check if salary already exists
        for record in salary_records:
            if str(record.get("admin_id")) == admin_id_str:
                print(f"Salary record already exists for Admin {admin_id_str}")
                return
        
        base_salary = self.calculate_base_salary(experience_years)
        
        new_record = {
            "admin_id": admin_id_str,
            "experience_years": experience_years,
            "base_salary": base_salary,
            "performance_level": 1,
            "performance_bonus": 0,
            "total_salary": base_salary,
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        }
        
        salary_records.append(new_record)
        
        with open(self.db_path, "w") as file:
            json.dump(salary_records, file, indent=4)
        
        print(f"✓ Salary record initialized for Admin {admin_id}")
    
    def get_salary_details(self, admin_id):
        """Get detailed salary information for an admin"""
        try:
            with open(self.db_path, "r") as file:
                salary_records = json.load(file)
        except FileNotFoundError:
            print("No salary records found!")
            return
        
        admin_id_str = str(admin_id)
        for record in salary_records:
            if str(record.get("admin_id")) == admin_id_str:
                print("\n" + "="*70)
                print(f"                    SALARY DETAILS - Admin {admin_id_str}                  ")
                print("="*70)
                print(f"\nExperience Years:                  {record['experience_years']} years")
                print(f"Base Salary:                       {record['base_salary']:.2f} Rs")
                print(f"Performance Level:                 {record['performance_level']}")
                print(f"Performance Bonus ({self.performance_bonus_percentage}% per level): {record['performance_bonus']:.2f} Rs")
                print("-"*70)
                print(f"Total Monthly Salary:              {record['total_salary']:.2f} Rs")
                print("="*70)
                print(f"Created Date:                      {record['created_date']}")
                print(f"Last Updated:                      {record['last_updated']}")
                print("="*70 + "\n")
                return
        
        print(f"No salary record found for Admin {admin_id}")
    
    def update_performance(self, admin_id):
        """Update admin performance and recalculate salary"""
        try:
            with open(self.db_path, "r") as file:
                salary_records = json.load(file)
        except FileNotFoundError:
            print("No salary records found!")
            return
        
        admin_id_str = str(admin_id)
        for record in salary_records:
            if str(record.get("admin_id")) == admin_id_str:
                print("\n" + "="*70)
                print(f"                    PERFORMANCE UPDATE - Admin {admin_id_str}              ")
                print("="*70)
                print(f"\nCurrent Performance Level:         {record['performance_level']}")
                print(f"Current Total Salary:              {record['total_salary']:.2f} Rs")
                print("-"*70)
                
                action = input("\nIncrease performance level? (yes/no): ").lower()
                
                if action == 'yes':
                    new_performance = record['performance_level'] + 1
                    
                    # Calculate new bonus
                    bonus = (record['base_salary'] * new_performance * self.performance_bonus_percentage) / 100
                    new_total = record['base_salary'] + bonus
                    
                    # Update record
                    record['performance_level'] = new_performance
                    record['performance_bonus'] = bonus
                    record['total_salary'] = new_total
                    record['last_updated'] = datetime.now().strftime("%Y-%m-%d")
                    
                    with open(self.db_path, "w") as file:
                        json.dump(salary_records, file, indent=4)
                    
                    print(f"\n✓ Performance updated successfully!")
                    print(f"New Performance Level:             {new_performance}")
                    print(f"New Performance Bonus:             {bonus:.2f} Rs")
                    print(f"New Total Salary:                  {new_total:.2f} Rs")
                    print("="*70 + "\n")
                else:
                    print("\nNo changes made.")
                
                return
        
        print(f"No salary record found for Admin {admin_id}")
    
    def get_salary_summary(self):
        """Get salary summary for all admins"""
        try:
            with open(self.db_path, "r") as file:
                salary_records = json.load(file)
        except FileNotFoundError:
            print("No salary records found!")
            return
        
        if not salary_records:
            print("No salary records found!")
            return
        
        print("\n" + "="*90)
        print("                          SALARY SUMMARY - ALL ADMINS                        ")
        print("="*90)
        print(f"{'Admin ID':<12} {'Experience':<12} {'Base Salary':<15} {'Performance':<14} {'Bonus':<12} {'Total':<15}")
        print("-"*90)
        
        total_payroll = 0
        for record in salary_records:
            print(f"{record['admin_id']:<12} {record['experience_years']} years{'':<5} {record['base_salary']:<15.2f} Level {record['performance_level']:<6} {record['performance_bonus']:<12.2f} {record['total_salary']:<15.2f}")
            total_payroll += record['total_salary']
        
        print("="*90)
        print(f"{'Total Payroll (Monthly):':<72} {total_payroll:.2f} Rs")
        print("="*90 + "\n")
    
    def salary_guide(self):
        """Display salary guide"""
        print("\n" + "="*70)
        print("                      SALARY GUIDE                            ")
        print("="*70)
        print("\nBASE SALARY BRACKETS:")
        print("-"*70)
        print(f"Less than 2 years experience:       {15000:.2f} Rs")
        print(f"2-4 years experience:               {self.base_salary_2_years:.2f} Rs")
        print(f"5+ years experience:                {self.base_salary_5_years:.2f} Rs")
        
        print("\nPERFORMANCE BONUS CALCULATION:")
        print("-"*70)
        print(f"Bonus Rate:                         {self.performance_bonus_percentage}% per performance level")
        print("\nFormula: Performance Bonus = Base Salary × Performance Level × {0}%".format(self.performance_bonus_percentage))
        print("\nTotal Salary = Base Salary + Performance Bonus")
        
        print("\nEXAMPLE CALCULATIONS:")
        print("-"*70)
        print(f"Admin with 5 years experience (Level 1): {self.base_salary_5_years:.2f} + ({self.base_salary_5_years} × 1 × {self.performance_bonus_percentage}%) = {self.base_salary_5_years + (self.base_salary_5_years * 1 * self.performance_bonus_percentage / 100):.2f} Rs")
        print(f"Admin with 5 years experience (Level 2): {self.base_salary_5_years:.2f} + ({self.base_salary_5_years} × 2 × {self.performance_bonus_percentage}%) = {self.base_salary_5_years + (self.base_salary_5_years * 2 * self.performance_bonus_percentage / 100):.2f} Rs")
        print(f"Admin with 5 years experience (Level 3): {self.base_salary_5_years:.2f} + ({self.base_salary_5_years} × 3 × {self.performance_bonus_percentage}%) = {self.base_salary_5_years + (self.base_salary_5_years * 3 * self.performance_bonus_percentage / 100):.2f} Rs")
        print("="*70 + "\n")
