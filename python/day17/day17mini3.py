import csv

def csv_reader(filename, condition=None):
   
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if condition is None:
                yield row
            else:
                if condition(row):  
                    yield row

for row in csv_reader("employees.csv"):
    print(row)

def salary_filter(row):
    return int(row["Salary"]) > 50000

for row in csv_reader("employees.csv", condition=salary_filter):
    print(row)
