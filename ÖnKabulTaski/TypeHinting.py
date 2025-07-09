# python dynamic bir dildir yani çaşışma zamanıma kadar hangi veri tipiyle uğraştığımızı bilmiyoruz
## bir func varsa onu tanımlayabilirim
# myparameter: int → myfunction’a int gelmeli,
# -> int → dönüş tipi int olacak,
# otherparameter: str → otherfunction ise str bekliyor.
# mypy gibi bir araçla daha çalıştırmadan uyumsuz tipleri bulmanızı sağlar,



def myfunction(myparameter: int) -> int:
    return myparameter + 10

def otherfunction(otherparameter: str):
    print(otherparameter)

otherfunction(myfunction(20))
