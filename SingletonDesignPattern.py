from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def get_data():
        """implement in child class """
class PersonSingleton(IPerson):
    __instance = None
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    def __init__(self, name , age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else :

            self.name = name 
            self.age = age
            PersonSingleton.__instance = self
    @staticmethod            
    def get_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age : {PersonSingleton.__instance.age}")

p = PersonSingleton("Mike", 30)
print(p)
p.print_data()

p2 = PersonSingleton.get_instance()
print(p2)
p.print_data()

