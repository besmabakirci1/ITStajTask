#Proxy design pattern
# wrapping functionality around sth ( object creation ) 
# or it uses an additional layer of abstraction or you could also say protection when it comes to creating instances of classes
from abc import ABCMeta, abstractmethod
class IPerson(metaclass = ABCMeta):
    @abstractmethod
    def person_method():
        """ Interface Method """
class Person (IPerson):
    def person_method(self):
        print("I'm a person!")

"""
p1 = Person()
p1.person_method
"""
                
# cuz that's too direct of an instantiation we're gonna use a proxy so middleman 
# you could say to create and handle the person object so we're gonna say:        
class ProxyPerson(IPerson):
    def __init__(self): ## here we're gonna create person instance
        self.person = Person()
    def person_method(self):
            print("Im the proxy functionality!")
            self.person.person_method()

p1 = Person()
p1.person_method()            
p2 = ProxyPerson()
p2.person_method()
