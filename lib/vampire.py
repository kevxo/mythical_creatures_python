class Vampire:
  def __init__(self, name, pet = "bat"):
    self.name = name
    self.pet = pet
    self.count = 0

  def is_thirsty(self):
    return True if self.count == 0 else False

  def drink(self):
    self.count += 1
