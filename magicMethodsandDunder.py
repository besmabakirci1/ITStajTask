#advanced Python Tutorial 0.1
# https://docs.python.org/3/tutorial/classes.html


class Vector:
    """
    2D vektör sınıfı:
    - x ve y bileşenlerini saklar,
    - toplama operatörünü destekler.
    """

    def __init__(self, x, y):
        """
        Yapıcı (constructor) metod:
        Bir Vector nesnesi yaratılırken x ve y değerlerini atanır.
        """
        self.x = x
        self.y = y

    def __add__(self, other):
       
        return Vector(self.x + other.x, self.y + other.y)
        """
        + ( sum ), / ( divisin ) , - (subtraction) operatörlerini kullanmak için:
        v1 + v2 ifadesi burada tanımlı:
        - other: toplamak istediğimiz diğer Vector nesnesi.
        - Yeni bir Vector döndürülür, bileşenleri toplanmış olarak.
        yoksa v3 = v1 + v2 dediğimizde error verecektir. 
    
        """

        v1 = Vector(10,20)
        v2 = Vector(50,60)
        v3 = v1 + v2 
        print(v3.x)
        print(v3.y)

        """
        print(v3.y) dediğimizde değerini 
        print(v3) dediğimizde sınıf vektörünün bir nesnesi olduğunu söyleyen bir mesaj alınır. 
        bu durumda vektörü bir diziye dönüştürebilirim ve böylelikle ne olacağını söyler ya da temsil yöntemini değiştirebiliriz 




        """
    def __repr__(self):
        """
        Nesneyi yazdırırken okunaklı bir gösterim sağlar
        (örneğin print(v3) dediğimizde Vector(60, 80) yazsın).
        """
        return f"Vector({self.x}, {self.y})"
