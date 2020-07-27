def sum(a, b):
  return a + b

name = 'Ozz'

class Person(object):
  def __init__(self):
    self.name = 'Ozz'

  def get_name(self):
    return self.name

  @staticmethod
  def parse_person(name):
    person = Person()
    person.name = name
    return person
