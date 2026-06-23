import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
taxes_db_path = os.path.join(BASE_DIR, "..", "database", "taxes.json")

from .daily_analytics import daily_analytics

class billing:
    def __init__(self):
        self.taxes = self.load_taxes()
        self.analytics = daily_analytics()
    
    def load_taxes(self):
        """Load tax information from database"""
        try:
            with open(taxes_db_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Taxes database not found!")
            return []
    
    def generate_bill(self, total, takeaway_charges=0):
        """
        Generate comprehensive bill with all taxes, GST with their IDs, and takeaway charges
        """
        # Calculate subtotal with takeaway charges
        bill_total = total + takeaway_charges
        
        print("\n" + "="*55)
        print("                    BILL DETAILS                    ")
        print("="*55)
        print(f"\nSubtotal (Food):                   {total:.2f} Rs")
        
        if takeaway_charges > 0:
            print(f"Takeaway Charges:                  {takeaway_charges:.2f} Rs")
            print(f"Bill Total:                        {bill_total:.2f} Rs")
        
        print("-"*55)
        
        tax_breakdown = {}
        total_tax = 0
        
        # Calculate all taxes with their IDs based on bill total
        for tax in self.taxes:
            tax_id = tax["tax_id"]
            tax_name = tax["tax_name"]
            percentage = tax["percentage"]
            tax_amount = (bill_total * percentage) / 100
            tax_breakdown[tax_id] = {
                "name": tax_name,
                "percentage": percentage,
                "amount": tax_amount
            }
            total_tax += tax_amount
        
        # Display each tax with ID
        print("\nTAX BREAKDOWN:")
        print("-"*55)
        for tax_id, tax_info in tax_breakdown.items():
            print(f"{tax_id} | {tax_info['name']:30} ({tax_info['percentage']}%): {tax_info['amount']:.2f} Rs")
        
        print("-"*55)
        print(f"Total Taxes:                       {total_tax:.2f} Rs")
        final_amount = bill_total + total_tax
        print("="*55)
        print(f"FINAL AMOUNT:                      {final_amount:.2f} Rs")
        print("="*55)
        
        print("\n-----------Payment Options----------------")
        print("1. Cash")
        print("2. Credit/Debit Card")
        print("3. Mobile Payment")
        
        payment_choice = input("Select payment method (1/2/3): ")
        payment_methods = {"1": "Cash", "2": "Credit/Debit Card", "3": "Mobile Payment"}
        payment_method = payment_methods.get(payment_choice, "Not Specified")
        
        print("\n" + "="*55)
        print("    Thank you for dining with us!              ")
        print("="*55 + "\n")
        
        # Record customer visit with bill amount
        self.analytics.record_customer_visit(final_amount, payment_method)
        
        return final_amount
    
    def get_tax_details(self):
        """Get detailed tax information"""
        print("\n" + "="*55)
        print("                    TAX DETAILS                    ")
        print("="*55)
        for tax in self.taxes:
            print(f"ID: {tax['tax_id']} | {tax['tax_name']:30} | {tax['percentage']}%")
        print("="*55 + "\n")
        """Get detailed tax information"""
        print("\n" + "="*55)
        print("                    TAX DETAILS                    ")
        print("="*55)
        for tax in self.taxes:
            print(f"ID: {tax['tax_id']} | {tax['tax_name']:30} | {tax['percentage']}%")
        print("="*55 + "\n")