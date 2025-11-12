# payroll/payslip.py
from datetime import datetime

def generate_payslip(employee, salary_info):
    """Generate and display payslip"""
    print("\n========== PAYSLIP ==========")
    print(f"Employee ID : {employee.emp_id}")
    print(f"Name        : {employee.name}")
    print(f"Base Salary : ₹{employee.base_salary}")
    print(f"Gross Salary: ₹{salary_info['gross']}")
    print(f"Tax Deducted: ₹{salary_info['tax']}")
    print(f"Net Salary  : ₹{salary_info['net']}")
    print(f"Date        : {datetime.now().strftime('%Y-%m-%d')}")
    print("==============================\n")
