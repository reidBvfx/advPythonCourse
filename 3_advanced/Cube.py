# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""

from abc import ABC, abstractmethod

class Object():
   def __init__(self, name):
      self.name = name
      self.translateV = [0, 0, 0]
      self.rotateV = [0, 0, 0]
      self.scaleV = [1, 1, 1]

   def translate(self, x, y, z):
      self.translateV = [x, y, z]
      print(f"{self.name}'s translation is now ({self.translateV[0]}, {self.translateV[1]}, {self.translateV[2]})")

   def rotate(self, x, y, z):
      self.rotateV = [x, y, z]
      print(f"{self.name}'s rotation is now ({self.rotateV[0]}, {self.rotateV[1]}, {self.rotateV[2]})")

   def scale(self, x, y, z):
      self.scaleV = [x, y, z]
      print(f"{self.name}'s scale is now ({self.scaleV[0]}, {self.scaleV[1]}, {self.scaleV[2]})")

   def print_status(self):
      print("{:<15} {:<5} ".format(f"{self.__class__.__name__} name: ", f"{self.name}"))
      print("-" * len(f"Cube name: {self.name}"))
      print("{:<15} {:<5} ".format("Translation: ", f"{self.translateV}"))
      print("{:<15} {:<5} ".format("Rotation: ", f"{self.rotateV}"))
      print("{:<15} {:<5} ".format("Scale: ", f"{self.scaleV}"))
      print("{:<15} {:<5} ".format("Color: ", f"{self.colorV}"))
      print()

   def update_transform(self, ttype, value):
      x = value[0]
      y = value[1]
      z = value[2]
      match ttype:
         case "translate":
            self.translate(x, y, z)
         case "rotate":
            self.rotate(x, y, z)
         case "scale":
            self.scale(x, y, z)

class Cube(Object, ABC):
   def __init__(self, name):
      super().__init__(name)
      self.colorV = [0, 0, 0]

   """this could be an @abstracemethod is Cube had a child class"""
   def color(self, R, G, B):
      self.colorV = [R, G, B]
      print(f"{self.name}'s color is now ({self.colorV[0]}, {self.colorV[1]}, {self.colorV[2]})")

   

c1 = Cube("cube1")  
c2 = Cube("cube2")   
c3 = Cube("cube3")

c1.update_transform("translate", [12, 15, 18])  
c1.print_status()

c2.rotate(50, 200, 140)
c2.print_status()

c3.color(255, 255, 255)
c3.print_status()