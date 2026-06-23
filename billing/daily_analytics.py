import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
customers_db_path = os.path.join(BASE_DIR, "..", "database", "daily_customers.json")

class daily_analytics:
    def __init__(self):
        self.db_path = customers_db_path
    
    def record_customer_visit(self, bill_amount, payment_method="Not Specified"):
        """Record a customer visit with bill amount"""
        today_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")
        
        try:
            with open(self.db_path, "r") as file:
                customer_records = json.load(file)
        except FileNotFoundError:
            customer_records = []
        
        # Generate customer ID
        customer_id = len(customer_records) + 1
        
        # Add new customer record
        new_record = {
            "customer_id": customer_id,
            "date": today_date,
            "time": current_time,
            "bill_amount": round(bill_amount, 2),
            "payment_method": payment_method
        }
        customer_records.append(new_record)
        
        with open(self.db_path, "w") as file:
            json.dump(customer_records, file, indent=4)
        
        print(f"✓ Customer visit recorded (ID: {customer_id})")
    
    def get_daily_customers(self, date=None):
        """Get daily customer statistics"""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        try:
            with open(self.db_path, "r") as file:
                customer_records = json.load(file)
        except FileNotFoundError:
            print("No customer records found!")
            return
        
        # Filter records by date
        daily_records = [r for r in customer_records if r["date"] == date]
        
        if not daily_records:
            print(f"\nNo customer visits recorded for {date}")
            return
        
        total_customers = len(daily_records)
        total_revenue = sum(r["bill_amount"] for r in daily_records)
        average_bill = total_revenue / total_customers if total_customers > 0 else 0
        
        print("\n" + "="*80)
        print(f"                    DAILY ANALYTICS - {date}                        ")
        print("="*80)
        print(f"\nTotal Customers:                   {total_customers}")
        print(f"Total Revenue (Bills):             {total_revenue:.2f} Rs")
        print(f"Average Bill per Customer:         {average_bill:.2f} Rs")
        print(f"Highest Bill:                      {max(r['bill_amount'] for r in daily_records):.2f} Rs")
        print(f"Lowest Bill:                       {min(r['bill_amount'] for r in daily_records):.2f} Rs")
        
        # Payment method breakdown
        print("\n" + "-"*80)
        print("PAYMENT METHOD BREAKDOWN:")
        print("-"*80)
        payment_methods = {}
        for record in daily_records:
            method = record["payment_method"]
            if method not in payment_methods:
                payment_methods[method] = 0
            payment_methods[method] += 1
        
        for method, count in payment_methods.items():
            print(f"  {method}: {count} transactions")
        
        print("\n" + "-"*80)
        print("CUSTOMER TRANSACTION DETAILS:")
        print("-"*80)
        print(f"{'Cust ID':<10} {'Time':<12} {'Bill Amount':<15} {'Payment Method':<20}")
        print("-"*80)
        
        for record in daily_records:
            print(f"{record['customer_id']:<10} {record['time']:<12} {record['bill_amount']:<15.2f} {record['payment_method']:<20}")
        
        print("="*80 + "\n")
    
    def get_monthly_summary(self):
        """Get monthly summary"""
        current_month = datetime.now().strftime("%Y-%m")
        
        try:
            with open(self.db_path, "r") as file:
                customer_records = json.load(file)
        except FileNotFoundError:
            print("No customer records found!")
            return
        
        # Filter records by month
        monthly_records = [r for r in customer_records if r["date"].startswith(current_month)]
        
        if not monthly_records:
            print(f"\nNo customer visits recorded for {current_month}")
            return
        
        total_customers = len(monthly_records)
        total_revenue = sum(r["bill_amount"] for r in monthly_records)
        average_bill = total_revenue / total_customers if total_customers > 0 else 0
        
        # Group by date
        dates_dict = {}
        for record in monthly_records:
            date = record["date"]
            if date not in dates_dict:
                dates_dict[date] = 0
            dates_dict[date] += 1
        
        print("\n" + "="*80)
        print(f"                    MONTHLY SUMMARY - {current_month}                      ")
        print("="*80)
        print(f"\nTotal Customers (Month):           {total_customers}")
        print(f"Total Revenue (Month):             {total_revenue:.2f} Rs")
        print(f"Average Bill per Customer:         {average_bill:.2f} Rs")
        print(f"Active Days:                       {len(dates_dict)}")
        print(f"Average Customers per Day:         {total_customers/len(dates_dict):.2f}")
        
        print("\n" + "-"*80)
        print("DAILY BREAKDOWN:")
        print("-"*80)
        print(f"{'Date':<12} {'Customers':<15} {'Total Revenue':<20}")
        print("-"*80)
        
        for date in sorted(dates_dict.keys()):
            daily_revenue = sum(r["bill_amount"] for r in monthly_records if r["date"] == date)
            print(f"{date:<12} {dates_dict[date]:<15} {daily_revenue:<20.2f} Rs")
        
        print("="*80 + "\n")
    
    def view_all_customers(self):
        """View all customer records"""
        try:
            with open(self.db_path, "r") as file:
                customer_records = json.load(file)
        except FileNotFoundError:
            print("No customer records found!")
            return
        
        if not customer_records:
            print("No customer records found!")
            return
        
        print("\n" + "="*80)
        print("                         ALL CUSTOMER RECORDS                           ")
        print("="*80)
        print(f"{'Cust ID':<10} {'Date':<12} {'Time':<12} {'Bill Amount':<15} {'Payment Method':<20}")
        print("-"*80)
        
        for record in customer_records:
            print(f"{record['customer_id']:<10} {record['date']:<12} {record['time']:<12} {record['bill_amount']:<15.2f} {record['payment_method']:<20}")
        
        total_revenue = sum(r["bill_amount"] for r in customer_records)
        print("="*80)
        print(f"Total Records: {len(customer_records)} | Total Revenue: {total_revenue:.2f} Rs")
        print("="*80 + "\n")
