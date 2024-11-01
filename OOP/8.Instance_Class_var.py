class Employee:
    companyName = "Apple"
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

emp1 = Employee("Harry")
emp2 = Employee("Rohan")

emp1.showDetails()
Employee.showDetails(emp1) #both are same

emp2.raise_amount = 0.3 #Changing Instance Var
emp2.companyName = "Apple India" #Also Changing Instance Var(as this not changes the class var)
emp2.showDetails()

Employee.companyName = "Google" #Changing Class Var
print(Employee.companyName)