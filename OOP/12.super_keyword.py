class Parent:
    def parent_method(self):
        print("This is parent_method in Parent class")

class Child(Parent):
    def parent_method(self):
        print("This is parent_method in Child class")
        super().parent_method() #Access parent_method of parent class

    def child_method(self):
        print("This is child_method")

p = Parent()
p.parent_method()

c = Child()
c.child_method()
c.parent_method()


#Another Example
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

pro = Programmer("AB", "id", "py")
print(pro.name)
print(pro.id)
print(pro.lang)