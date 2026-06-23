class book_table:
    def book_table(self):
        name = input("Enter your name: ")
        contact = input("Enter your contact number: ")
        date = input("Enter the date for booking (YYYY-MM-DD): ")
        time = input("Enter the time for booking (HH:MM): ")
        guests = input("Enter the number of guests: ")
        table_number = input("Enter the table number you want to book: ")
        
        #for adcvance payment
        account_number = input("Enter your account number for payment: ")
        
        suprise = input("Do you want to add any special requests? (yes/no): ")
        if suprise.lower() == 'yes':
            
            special_request = input("Enter your special request: ")
            print(f"Special request noted: {special_request}")
        
        with open("table_bookings.txt", "a") as file:
            file.write(f"{name},{contact},{date},{time},{guests},{table_number}\n")
        
        print(f"Table booked successfully for {name} on {date} at {time} for {guests} guests. Contact: {contact}")