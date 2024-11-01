class Employee:
    def __init__(self, name, salary):  
        self.name = name
        self.salary = salary

    def showDetail(self):
        print(f"{self.name}\n{self.salary}")

    @classmethod
    def fromStr(self, str):
        return self(str.split("-")[0], int(str.split("-")[1]))
    
e1 = Employee("empOG", 99999)
Employee.showDetail(e1)

string = "emp2-10000"
e2 = Employee.fromStr(string)
e2.showDetail()
