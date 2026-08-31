# Exercise 1.4 — Algorithm Audit: Flywheel Calculation
#
# Read the complete exercise description in Lecture_1.ipynb.
#
# Correct the Python errors and the engineering/algorithm errors.

mass = float(input("Enter flywheel mass [kg]: "))
diameter_mm = float(input("Enter flywheel diameter [mm]: "))
speed_rpm = float(input("Enter rotational speed [rpm]: "))

radius = diameter_mm / 2
omega = speed_rpm * 60
I = mass × radius**2
energy = I * (omega**2]

print("Energy =", energy, "J")
