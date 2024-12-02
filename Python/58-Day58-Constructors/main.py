class Person:

  def __init__(self):
    print("Hey I am a person")
a = Person()

#     self.name = name
#     self.occ = occ

#   def info(self):
#     print(f"{self.name} is a {self.occ}")

# a = Person("Harry", "Developer")
# b = Person("Divya", "HR")
# c = Person(1, 2)
# a.info()
# b.info()
# c.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()


class Details:
  def __init__(self, animal, group):
      self.animal = animal
      self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")

class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()