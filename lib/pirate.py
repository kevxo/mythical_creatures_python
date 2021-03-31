class Pirate:
  def __init__(self, name, job = "Scallywag"):
    self.name = name
    self.job = job
    self.count = 0
    self.booty = 0

  def is_cursed(self):
    return False if self.count < 3 else True

  def commit_heinous_act(self):
    self.count += 1

  def rob_ship(self):
    self.booty += 100