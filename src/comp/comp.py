# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# --------------------------------------------------------------------
# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

# Understand
#   List comprehension syntax: [ <expression> for <element> in <iterable> if <condition> ]
#   We need to iterate through the list and return a list of Humans who's name starts with a D
#   How do you parse a class object in a list using a list comprehension? h.name, h.age in humans
#   print(type(humans[0]))


# Plan
#   for human in humans:
#       if human.name[0] == "D":
#           print(f"{human.name}")

# Execute
print("Starts with D:")
a = [human.name for human in humans if human.name[0] == "D"]
print(a)

# Reflect

# --------------------------------------------------------------------
# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

# Understand
#   Using a list comprehension print a list of everyone's names that end in "e".
#   Need to get the end of the person's name using []

# Plan
#   for human in humans:
#       if human.name[-1:] == "e":
#           print(human.name)

# Execute
print("Ends with e:")
b = [human.name for human in humans if human.name[-1:] == "e"]
print(b)

# Reflect

# --------------------------------------------------------------------
# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

# Understand
#   List comprehension will create a list of names
#   whose name's first letter is between C and G


# Plan

# for human in humans:
#    if "C" <= human.name[0] <= "G":
#        print(human.name)

# Execute
print("Starts between C and G, inclusive:")
c = [human.name for human in humans if "C" <= human.name[0] <= "G"]
print(c)

# Reflect
#   Instead of using the "C" <= .... <= "G" it would be much cleaner to
#   use in Range(), need to study up on how to do that with strings

# --------------------------------------------------------------------
# Write a list comprehension that creates a list of all the ages plus 10.

# Understand
#   Return list comprehension of all Human's ages + 10

# Plan

# for human in humans:
#    result = human.age + 10
#    print(result)

# Execute
print("Ages plus 10:")
d = [human.age + 10 for human in humans]
print(d)

# Reflect

# --------------------------------------------------------------------
# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.

# Understand
#   List comprehension that creates a list of strings
#   name joined to age with a hyphen "-"

# Plan

# can only concatenate str (not "int") to str
# so we change age (int) to a str

# for human in humans:
#    result = human.name + "-" + str(human.age)
#    print(result)

# Execute
print("Name hyphen age:")
e = [human.name + "-" + str(human.age) for human in humans]
print(e)

# Reflect

# --------------------------------------------------------------------
# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.

# Understand
# List comprehension creates a list of tuples (), containing name and age
# for everyone between the ages of 27 and 32


# Plan

# for human in humans:
#    if human.age in range(27, 32):
#        result = (human.name, human.age)
#        print(result)

# Execute
print("Names and ages between 27 and 32:")
f = [(human.name, human.age) for human in humans if human.age in range(27, 33)]
print(f)

# Reflect

# --------------------------------------------------------------------
# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.

# Understand
#   Create a list comp of new Humans like old list,
#   except ALL NAMES UPPERCASE & age + 5

# Plan
# for human in humans:
#    result = Human(human.name.upper(), human.age + 5)
#    print(result)

# Execute
print("All names uppercase:")
g = [Human(human.name.upper(), human.age + 5) for human in humans]
print(g)

# Reflect

# --------------------------------------------------------------------
# Write a list comprehension that contains the square root of all the ages.

# Understand
# List comp of all the ages squared
# sqrt() function is an inbuilt function in Python programming language that
# returns the square root of any number.

# Plan
# Import math
# for human in humans:
#    result = math.sqrt(human.age)
#    print(result)

# Execute
print("Square root of ages:")
h = [math.sqrt(human.age) for human in humans]
print(h)

# Reflect
