#Myscript.py 
#python3 myscipt.py -o text.txt DEBUG -c

#some func. can have arcs keyword and arguments  this is how you essentailly have a variable amount of parameters of named parameters and just positional parameters so I can go ahead and say print 


"""

def myfunction(*args , **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(args[4])

myfunction('hey', True, 19, 'wow', KEYONE = "TEST", KEYTWO = 7)    

"""
# ← kwargs’da KEYONE yoksa KeyError
##“Decorator yazarken wrapper fonksiyonu mutlaka *args, **kwargs almalı ve bunları orijinal fonksiyona eksiksiz iletmeli; aksi hâlde bazı keyword argümanlar kaybolur veya eksik oldukları için hata fırlatılır.”
_______________________________

 
# sys.argv bir liste (list).
#0.elemanı: çalıştırdığınız Python betiğinin adı (main.py).

#1.elemanı: komut satırından ilk parametre

#2.elemanı: komut satırından ikinci parametre

# … ve bu şekilde devam eder.

# argüman vektörü ve burda geçirilen bireysel argümanları ele almak için indeksler kullanabiliriz 
## indeks o her zaman dosya adının kendisi veya betik adı veya program adıdır.
#  Bu durumda main.py olur ve sonra bir iki üç ve benzeri konumsal argümanlardır, 
# bu yüzden burada bir test çalıştıralım ve 

"""
import sys
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
"""

### sys.argv → komut satırından girilen değerleri yakalamak için

### sys.argv[0] → betiğin kendisi

### sys.argv[1:] → sizin girdiğiniz gerçek parametreler

### Yorum satırındaki “Usage:” → nasıl çalıştırmanız gerektiğini açıklamak için konur

### Eğer işin içine -p, -h gibi bayraklar (flags) giriyorsa, basit argv[1]/argv[2] yetmez; 
# ya manuel parse ya argparse kullanmalısınız.

_______________________________

import sys
import getopt
filename = "test.txt"
message = "Hello"

opts, args = getopt.getopt(sys.argv[1:], "f:m:" , ['filename', 'message'])

for opt , arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open (filename, 'w+') as f :
    f.write(message)            