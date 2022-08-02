from datetime import datetime


class Employee:

    def __init__(self, fname:str,lname:str,salary:float):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def get_name(self):
        return f"{self.fname} {self.lname}"

    def get_salary(self):
        return self.salary
    
    def get_salary_after_tax(self,tax:float):
        return (self.salary - self.salary*tax)
