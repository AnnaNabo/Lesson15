#1,2
class Transport:
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage
       
   def pech(self):
     print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")   
    
   def seating_capacity(self, capacity = 50):
       print(f"Вместимость одного автобуса {self.name}: {capacity} пассажиров")
 
class AutobusCl(Transport):
   def proverka(self):
    self.seating_capacity() 
     

AutobusO = AutobusCl("Renault Logan", 180, 12)
AutobusO.pech()
AutobusO.proverka()
