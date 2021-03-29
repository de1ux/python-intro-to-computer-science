"""
Build a dice rolling simulation
"""

from classes_die import Die

d1 = Die()

d1.set_sides(6)
d1.roll()

print("Rolling one six-sided die: ", d1.get_result_of_roll())

d1.roll()

d2 = Die()
d2.set_sides(2)
d2.roll()

print("Rolling both dice: ", d1.get_result_of_roll(), d2.get_result_of_roll())