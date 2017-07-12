import random


class Thief:
	sneaky = True

	def __init__(self, name, sneaky=True, **kwargs):
		self.name = name
		self.sneaky = sneaky

		for key, value in kwargs.items():
			setattr(self, key, value)

	def pick_pocket(self):
		if self.sneaky:
			return self.sneaky and bool(random.randint(0, 1))
		else:
			return False

	def hide(self, light_level):
		return self.sneaky and light_level < 10















ted = Thief("Ted", scars = None, favorite_weapon = "knife")

print(ted.scars)
print(ted.favorite_weapon)