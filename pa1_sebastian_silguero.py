# Team Members: Sebastian Silguero
# Course: CS151, Dr.Rajeev
# Date: September 20th, 2021
# Programming Assignment: 1
# Program Inputs: Length, Width, and Height in Feet; Dimensions of the room that will be painted
# Program Output: Total Area that needs to be painted in Square Feet and the amount of paint and primer needed in gallons.

# User will input the length, width, and height in Feet.

print("Enter the dimensions of the room in feet:")

# l represents length
l = float(input("Length of the Room: "))
# w represents width
w = float(input("Width of the Room: "))
# h represents the height
h = float(input("Height of the Room: "))

# Calculate the area of the wall, ceiling and total area. Total area that needs to be painted.

areaCeiling = l * w
areaWall = w * h
totalArea = areaCeiling + (areaWall * 4)

print("Area that needs to be painted is: " + str(totalArea) + " sq ft.")

# Calculation of how much paint and primer is needed.

totalPaint = totalArea / 350
totalPrimer = totalArea / 200

print("Total amount of paint needed: %.2f" % totalPaint + " gal")
print("Total amount of primer needed: %.2f" % totalPrimer + " gal")

print("Thanks for using my code!")





