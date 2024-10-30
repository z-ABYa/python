# Public 
class Employee():
  def __init__(self):
    self.name = "Harry"


# Private(by convention)(used for name mangling)
class programmer():
  def __init__(self):
    self.__name = "Marry"

b = programmer()
# print(b.__name) Cannot be accessed directly(shows Err)
print(b._programmer__name) #can be accessed indirectly (Name Mangelingna)


# Protected 
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):  # protected method
        return "CodeWithHarry"

obj = Student()
print(obj._name)      
print(obj._funName())