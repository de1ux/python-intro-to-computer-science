"""
Exercises 7.7, Programming Exercise 6

The speeding ticket fine policy of Podunksville is $50 plus $5 for each mph
over the speed limit, plus a penalty of $200 for any speed over 90 mph.

Write a function that accepts a speed limit, and a clocked speed and either
prints a message indicating the speed was legal or prints the amount of the
fine, if the speed is illegal.
"""

def is_speeding(speed_limit, speed):
    pass


def find_fine(speed_limit, speed):
    pass


# we can write these as if statements
if is_speeding(20, 20):
    # Let them go the speed limit w/o considering it speeding
    print("The code in is_speeding is wrong!!!")


if find_fine(40, 41) == 55:
    print("the code is correct!")


# or, more succintly as assertions

# when going 10 under, is_speeding should be false
assert is_speeding(20, 10) == False

# when going 10 over, is_speeding should be true
assert is_speeding(20, 30):
