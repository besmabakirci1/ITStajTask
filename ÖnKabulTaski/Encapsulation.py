# Encapsulation and data hiding 

class Person:
    def __init__(self, name, age, gender):
          self.__name = name 
          self.__age = age 
          self.__gender = gender

          # its basic constructor so everything here is private
          # p1 = Person(...)          
          # p1.__name = ""  
          ## but these doesnt work in python cuz this attributes set as private by " .__ "
          ## so we can create properties did allow to access those values to read and write through this property
          ## through getter and setters essentialy we do sth like fonc. 
          # in .py we dont have method overloading so we cant specify usually like method called name with self and another method called name with self and value this is doesnt work 



@property
def Name(self):
     return self.__name

@Name.setter
def Name(self, value):
    self.__name = value

@staticmethod
def mymethod():
     print("Hello World!")
         

p1 = Person("Mike", 20, 'm')
print(p1.Name) 




  