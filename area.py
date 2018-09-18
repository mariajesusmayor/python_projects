<<<<<<< HEAD
"""
This program takes an input from the user to calculate the area of a shape
"""
print ("Calculator is starting")
option = input("Enter C for Circle or T for Triangle: ")
if option == "C":
  radius = float(input ("Indicate the radius: "))
  area = 3.14159 * radius ** 2
  print ("The area is: %s" % (area))
elif option == "T":
  base = float(input ("Indicate the base: "))
  height = float(input ("Indicate the height: "))
  area = 0.5 * base * height
  print ("The area is: %s" % (area))
else:
  print ("Invalid option")
print ("Exiting program")
=======
"""
This program takes an input from the user to calculate the area of a shape
"""
print ("Calculator is starting")
option = input("Enter C for Circle or T for Triangle: ")
if option == "C":
  radius = float(input ("Indicate the radius: "))
  area = 3.14159 * radius ** 2
  print ("The area is: %s" % (area))
elif option == "T":
  base = float(input ("Indicate the base: "))
  height = float(input ("Indicate the height: "))
  area = 0.5 * base * height
  print ("The area is: %s" % (area))
else:
  print ("Invalid option")
print ("Exiting program")
>>>>>>> a3c79e1e64543b0d6f078d5527564506ecdfc6db
