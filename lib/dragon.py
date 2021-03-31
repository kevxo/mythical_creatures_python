
class Dragon:
  def __init__(self, name, color, rider):
    self.name = name
    self.color = color
    self.rider = rider
    self.count = 0

  def eat(self):
    self.count += 1

  def is_hungry(self):
    return True if self.count < 3 else False