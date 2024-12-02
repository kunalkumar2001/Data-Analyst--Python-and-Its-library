class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nikita"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
# class Details:
#   name = "Rohan"
#   age = 20

# obj1 = Details()
# print(obj1.name)
# print(obj1.age)