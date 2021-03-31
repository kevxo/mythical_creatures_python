class Unicorn:
  def __init__(self, name, color = "white"):
    self.name = name
    self.color = color

  def is_white(self):
    return True if self.color == "white" else False

  def say(self, word):
    return f"**;* {word} **;*"
