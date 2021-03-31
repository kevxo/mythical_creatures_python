class Medusa:
  def __init__(self, name,):
    self.name = name
    self.statues = []
    self.count = 0

  def stare(self, person):
    if len(self.statues) == 3:
      self.statues[0].stoned_status = False
      self.statues.pop(0)
      person.stoned_status = True
      self.statues.append(person)
    else:
      person.stoned_status = True
      self.statues.append(person)


class Person:
  def __init__(self, name, stoned_status = False):
    self.name = name
    self.stoned_status = stoned_status

  def is_stoned(self):
    return self.stoned_status

