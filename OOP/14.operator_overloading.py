class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, vec): #Overloading of '+' operator
        return Vector(self.i + vec.i, self.j + vec.j, self.k + vec.k) # returns/calls the Vector class itself
    
vec = Vector(1,2,3)
print(vec)

vec2 = Vector(2,3,4)
print(vec2)
print(vec + vec2)
print(type(vec + vec2))
