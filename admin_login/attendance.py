import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
attendance_db_path = os.path.join(BASE_DIR, "..", "database", "attendance.json")

class attendance_tracker:
    def __init__(self):
        self.db_path = attendance_db_path
    
    def mark_attendance(self, admin_id):
        """Mark attendance for admin"""
        today_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")
        admin_id_str = str(admin_id)
        
        try:
            with open(self.db_path, "r") as file:
                attendance_records = json.load(file)
        except FileNotFoundError:
            attendance_records = []
        
        # Check if admin already marked attendance today
        for record in attendance_records:
            if str(record.get("admin_id")) == admin_id_str and record["date"] == today_date:
                print(f"✓ Attendance already marked for today at {record['check_in_time']}")
                return
        
        # Add new attendance record
        new_record = {
            "admin_id": admin_id,
            "date": today_date,
            "check_in_time": current_time,
            "status": "Present"
        }
        attendance_records.append(new_record)
        
        with open(self.db_path, "w") as file:
            json.dump(attendance_records, file, indent=4)
        
        print(f"✓ Attendance marked at {current_time}")
    
    def view_attendance(self, admin_id=None):
        """View attendance records"""
        try:
            with open(self.db_path, "r") as file:
                attendance_records = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No attendance records found!")
            return
        
        if not attendance_records:
            print("No attendance records found!")
            return
        
        print("\n" + "="*70)
        print("                      ATTENDANCE RECORDS                          ")
        print("="*70)
        
        if admin_id is not None:
            # Show specific admin attendance
            records = [r for r in attendance_records if str(r.get("admin_id")) == str(admin_id)]
            print(f"\nAttendance for Admin {admin_id}:")
        else:
            # Show all attendance
            records = attendance_records
            print("\nAll Attendance Records:")
        
        if not records:
            print("No records found for this admin!")
            return
        
        print("-"*70)
        print(f"{'Admin ID':<12} {'Date':<12} {'Check-in Time':<15} {'Status':<15}")
        print("-"*70)
        
        for record in records:
            print(f"{record['admin_id']:<12} {record['date']:<12} {record['check_in_time']:<15} {record['status']:<15}")
        
        print("="*70 + "\n")
    
    def get_attendance_summary(self, admin_id):
        """Get attendance summary for specific admin"""
        try:
            with open(self.db_path, "r") as file:
                attendance_records = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No attendance records found!")
            return
        
        admin_records = [r for r in attendance_records if str(r.get("admin_id")) == str(admin_id)]
        total_days = len(admin_records)
        
        print("\n" + "="*50)
        print(f"       Attendance Summary - Admin {admin_id}      ")
        print("="*50)
        print(f"Total Days Present: {total_days}")
        if total_days > 0:
            print(f"Last Check-in: {admin_records[-1]['date']} at {admin_records[-1]['check_in_time']}")
        print("="*50 + "\n")
