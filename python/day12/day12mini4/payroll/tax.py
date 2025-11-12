# payroll/tax.py
import math

def calculate_tax(salary):
    """Simple tax calculation based on income brackets"""
    if salary <= 25000:
        tax = 0
    elif salary <= 50000:
        tax = salary * 0.10
    elif salary <= 100000:
        tax = salary * 0.20
    else:
        tax = salary * 0.30

    return math.floor(tax)
