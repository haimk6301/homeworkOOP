class Employee:

    def __init__(self,name, year_of_joining, salary, address):
        self.name = name
        self.year_of_joining = year_of_joining
        self.salary = salary
        self.address = address

    def print_employee_table(self):
        print(f'\t{self.name}    \t{self.year_of_joining}        \t{self.salary}  \t{self.address}')

