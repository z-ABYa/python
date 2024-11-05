class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"This is is an obj of class Employee"

    def __repr__(self):
        return f"Employee:('{self.name}')"
    
    def __call__(self):
        print("Object called")


emp = Employee("Abhyshek")
print(emp) #if 'str' is absent it prints 'repr'
print(str(emp)) #same as above
print(repr(emp)) 
emp()
print(len(emp))
