class takeaway_handler:
    def __init__(self):
        self.packaging_fee = 5  # Flat packaging fee in Rs
        self.takeaway_tax_percentage = 1.5  # Takeaway packaging tax percentage
    
    def check_leftover_food(self, orders, foods):
        """
        Check if customer has leftover food and offer takeaway option
        Returns: (has_leftover, takeaway_amount) tuple
        """
        if not orders:
            return False, 0
        
        print("\n" + "="*60)
        print("                    LEFTOVER FOOD CHECK                    ")
        print("="*60)
        print("\nYou ordered the following items:")
        print("-"*60)
        for order in orders:
            print(f"  • {order}: {foods[order][1]} Rs")
        print("-"*60)
        
        leftover = input("\nDo you have leftover food? (yes/no): ").lower()
        
        if leftover == 'yes':
            print("\n" + "="*60)
            print("                    TAKEAWAY OPTION                         ")
            print("="*60)
            
            takeaway = input("\nWould you like to take the leftover food home? (yes/no): ").lower()
            
            if takeaway == 'yes':
                print("\n✓ Takeaway option selected!")
                print(f"Packaging Fee: {self.packaging_fee} Rs")
                print(f"Takeaway Packaging Tax (1.5%): Will be calculated on final amount")
                return True, self.packaging_fee
            else:
                print("\n✗ Leftover food will not be packed.")
                return False, 0
        else:
            print("\n✓ Food completely consumed. Thank you!")
            return False, 0
    
    def apply_takeaway_charges(self, subtotal, packaging_fee=0):
        """
        Apply takeaway charges to the bill
        Returns: additional_charges (packaging fee + packaging tax)
        """
        if packaging_fee == 0:
            return 0
        
        # Calculate packaging tax on subtotal + existing packaging fee
        packaging_tax = ((subtotal + packaging_fee) * self.takeaway_tax_percentage) / 100
        total_additional = packaging_fee + packaging_tax
        
        return total_additional
    
    def show_takeaway_summary(self, packaging_fee, additional_charges):
        """Display takeaway charges summary"""
        if packaging_fee == 0:
            return
        
        print("\n" + "="*60)
        print("                    TAKEAWAY CHARGES                      ")
        print("="*60)
        print(f"Packaging Fee:                     {packaging_fee:.2f} Rs")
        print(f"Packaging Tax (1.5%):              {additional_charges - packaging_fee:.2f} Rs")
        print(f"Total Takeaway Charges:            {additional_charges:.2f} Rs")
        print("="*60 + "\n")
