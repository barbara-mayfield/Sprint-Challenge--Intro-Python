# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# PARENT
class Vehicle:
    pass


# CHILD
class GroundVehicle:
    pass


# GRANDCHILD
class Car:
    pass


# GRANDCHILD
class Motorcycle:
    pass


# CHILD
class FlightVehicle:
    pass


# GRANDCHILD
class Starship:
    pass


# GRANDCHILD
class Airplane:
    pass
