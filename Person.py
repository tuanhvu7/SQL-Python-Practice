class Person(object):    
    
   def __init__(self, first_name, last_name):
       self.first_name = first_name
       self.last_name = last_name

   def printInfo(self):
       print("Name: " + self.first_name + " " + self.last_name + "\n")

   def setFirstName(self, name):
       self.first_name = name

   def setLastName(self, name):
       self.last_name = name

   def setName(self, first_name, last_name):
       self.first_name = first_name
       self.last_name = last_name


   def getFirstName(self):
       return self.first_name

   def getLastName(self):
       return self.last_name



