#!/usr/bin/python3

class Person(object):
  def __init__(self, name):
    self.name = name

class Employee(Person):
  def __init__(self, name, salary):
    super(Employee, self).__init__(name) #super calls paren.__init__()
    self.salary = salary
  def who_am_i():
    return f"Employee: {self.name}"

class Janitor(Employee):
  def __init__(self):
    super(Janitor, self).__init__('Jaime', 9000)
    pass  #empty block

jane = Person('Jane')
john = Employee('John', 120000)
janitor = Janitor()

print(jane.name)
print(f"{john.name} earns {john.salary}")
print(f"The Janitor is {janitor.name} earns {janitor.salary}")

# the convention is to use CamelCase for classes
#  and lower_case_with_underscores for functions and methods