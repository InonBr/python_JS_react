class Animal:
  def __init__(self, habitst, diet):
    self.habitst = habitst
    self.diet = diet

  def speak(self):
    print(f"I live in the {self.habitst} and my diet is {self.diet}")

# animal_1 = Animal('sea', 'plankton')
# animal_1.speak()


class Lion(Animal):
  def __init__(self, title, pride_size):
    super().__init__('savanna', 'meat')
    self.title = title
    self.pride_size = pride_size

  def roar(self):
    print(f"I am the {self.title} of my pride of {self.pride_size} lions")

scar = Lion('outcast', 15)
scar.roar()
scar.speak()
