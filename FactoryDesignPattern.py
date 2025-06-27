## Flyweight ve Factory Pattern 🌸

from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    @abstractmethod 
    def person_method():
        """ Interface method : bir arayüzün temelde ne olduğu sadece bir imza tanımıdır. 
        Bu yüzden fonksiyonlara ve yöntemlere sahip 
            sahip olup ne yaptıklarını söyleyemeyeceğiz 
        

p1 = IPerson()
p1.person_method()          
## TypeError: Can't instantiate abstract class IPerson with abstract methods person_method

"""
class Student(IPerson):
     # its gonna inherit from IPerson interface is going to implement that IPerson interface 
     # and we are going to override this method now if I don't do that if I just say :  

    def __init__(self):
        self.name = "Basic Student Name "

## s1 = Student() 

## we are not going to be able to create an instance of student cuz the student didnt ovveride the abstract method person we need to do that otherwise we can't treat this
## a non abstract class
## so after the constructor we are going to say :

    def person_method(self):
        print("I'm a student")
class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Name "
    def person_method(self):
        print("I am a teacher")    
s1 = Student()
s1.person_method()

t1 = Teacher()
t1.person_method()


## the output will be : I'm a student \n I am a teacher and 
# the factory design pattern builds person objects so we actually want to say class person  

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return .1
    
if __name__ == "__main__":
    choice = input("What type of person do you want to create ? \n")
    person = PersonFactory.build_person(choice)
    person.person_method()
