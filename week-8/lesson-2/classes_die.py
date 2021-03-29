from random import randrange

class Die:
    sides = None
    value = None

    def set_sides(self, num_of_sides):
        self.sides = num_of_sides

    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def get_result_of_roll(self):
        return self.value
