
# a Toyota is an INSTANCE of class car

class Car:
  def __init__(self, color, make, model):
      self.color = color #Attributes for color make and model
      self.make = make
      self.model = model
      self.gas = 0

  def get_gas(self):
      self.gas += 10

  def check_gas(self):
      print(self.gas)

#instantiate an object of class Car
car1 = Car('blue', 'hyundai', 'elantra') #Instance
car2 = Car('black', 'subaru', 'outback') #Instance
print(car1.check_gas())
car1.get_gas()
print(f"you have {car1.check_gas()} amount of gas")

print(f"car 1 has a color of {car1.color} and car 2 has a color of {car2.color}")
print(f"car 1 has a make of {car1.make} and car 2 has a make of {car2.make}")


