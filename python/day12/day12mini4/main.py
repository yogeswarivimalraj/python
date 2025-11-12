# main.py
from payroll.employee import Employee
from payroll.salary import calculate_net_salary
from payroll.payslip import generate_payslip

def main():
    emp = Employee(101, "Yogeswari", 50000)
    salary_info = calculate_net_salary(emp.base_salary, bonus=5000)
    generate_payslip(emp, salary_info)

if __name__ == "__main__":
    main()
