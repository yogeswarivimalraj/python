# payroll/salary.py
from payroll.tax import calculate_tax

def calculate_net_salary(base_salary, bonus=0):
    """Calculate net salary after tax"""
    gross = base_salary + bonus
    tax = calculate_tax(gross)
    net = gross - tax
    return {"gross": gross, "tax": tax, "net": net}
