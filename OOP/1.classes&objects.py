class Person: # This is a templet and can be used again for diff "persons".
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation} and has ${self.networth}.")


a = Person()
b = Person()
c = Person()# All info -> Default

a.name = "Shubham"
a.occupation = "Accountant" #Networth -> Default

b.name = "Nitika"
b.occupation = "HR"
b.networth = 17

# print(a.name, a.occupation)
a.info()
b.info()
c.info()