
## Decorator Nedir?
### Bir callable (çağrılabilir) Python objesidir ki, orijinal bir fonksiyonu alır, üzerine ek işlemler koyar ve yeni bir fonksiyon döndürür.
### bir fonksiyonu başka bir fonksiyonla “sarmak” (wrap) suretiyle davranışını dinamik olarak değiştirmeye yara
"""
    @decorator_name
    def fonksiyon(...):
        ...
şu ile eşdeğerdir:

    def fonksiyon(...):
    ...
    fonksiyon = decorator_name(fonksiyon)
"""   

"""
def mydecorator(functions):
    def wrapper(*args, **kwargs):
        print("I'm decorating your function!")
        return_value = function(*args, **kwargs)
        return return_value
    return wrapper 
@mydecorator
def hello(person):
    print(f"Hello {person}")
    return f"Hello{person}!"
# instead of writing is as " mydecorator(hello_world)() " in python we use it as @mydecorator /n hello_world()


print (hello("Mike"))

"""

#Practical Example 01 - Logging 
def logged(function):
    def wrapper(*args,** kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname= function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
            return value
        
        return wrapper
    
@logged 
def add(x, y):
    return x + y

print(add(10 , 20))

# Practical Example #2 - Timing
import time 
def timed(function):
    def wrapper(*args,** kwargs): #argüman ve anahtar kelimeler alınır 
        before = time.time() # şuanki zamanı alıp
        value = function(*args,** kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute!")
        return value
    return wrapper

@timed
def myfunction(x):
    result *= 1
    for i in range(1, x):
        result *= i

    return result
myfunction(90000)    