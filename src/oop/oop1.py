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
class GroundVehicle(Vehicle):
    pass


# GRANDCHILD
class Car(GroundVehicle):
    pass


# GRANDCHILD
class Motorcycle(GroundVehicle):
    pass


# CHILD
class FlightVehicle(Vehicle):
    pass


# GRANDCHILD
class Starship(FlightVehicle):
    pass


# GRANDCHILD
class Airplane(FlightVehicle):
    pass
