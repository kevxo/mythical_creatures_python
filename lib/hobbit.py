class Hobbit:
  def __init__(self, name, disposition = "homebody"):
    self.name = name
    self.disposition = disposition
    self.age = 0

  def celebrate_birthday(self):
    self.age += 1

  def is_adult(self):
    return True if self.age > 32 else False

  def is_old(self):
    return True if self.age >= 101 else False

  def has_ring(self):
    return True if self.name == "Frodo" else False

  def is_short(self):
    return True
