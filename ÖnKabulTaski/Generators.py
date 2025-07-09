#Generators ne işe yaradığı ve nasıl kullanıldığı anlatıldı ve tanım verilmedi. 
## seq 1 to 9,000,000
## take the cube power of each number number in the seq

import sys

for x in range (1, 9000000):
    print( x**3)
## but the range func. is limited cuz its have spesific start point and end  
# what we can do if we dont have range func.?
## - we build our generators , and they have sth called "lazy execution " 
# as a instance from haskell [2..90] got then  a numbers from 2 to 90 but we dont get it as collection 
# we get them when we need it so this is the structor that produces whenever we need when we need it .
# for returning we use yield keyword, every time we get the next element so you   

def mygenerator(x):
    for x in range(n):
        yield x ** 3
values = mygenerator(9000000)   

"""
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
"""

"""
for x in values:
    print(x)
    #sys.getsizeof(...) ile bellekte tamponlanan veri yerine nesnenin kendisinin boyutunu ölçmek için kütüphane import edecek ve bu kullanılmaycak olup direkt basmasını isteyeceğiz 
    
"""

print(sys.getsizeof(values))


_____________________________________

# generator ile yapabileceğimi bir şey daha sırdan koleksiyonlarla yapamayıp 
## sonsuz diziler yaratabiliriz örneğin def capstock 
## burada parametremiz yok çünkü sınırımız yok 



def infinite_seq ():
    result = 1 
    while True:
         yield result
         result *= 5

values = infinite_seq()
"""print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))"""

for x in values:
    print(x)

# yield anahtar kelimesi var olduğu için durur çünkü bir sonraki değerin talebini bekler     