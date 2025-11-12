# payroll/employee.py

class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def __str__(self):
        return f"{self.emp_id} - {self.name} (${self.base_salary})"
