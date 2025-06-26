# ITStajTask
1. m3 macbook pro Apple silicon içine sanal makine kurulumu (VirtualBox)
Debian (ARM 64-bit) tercih edildi 
Chatgpt kullanıldı : https://chatgpt.com/share/685aa279-9c50-800e-aba7-1a678d55750b


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

# 1) Decorator fonksiyonunun tanımı (Soyut Decorator)
#    - Parametre: süslenecek (decorate edilecek) fonksiyon
#    - Geriye: fonksiyonu “saran” wrapper fonksiyonu döner
# 
def my_decorator(func):
    """
    Decorator’un “fabula”sı:
      • func: Orijinal fonksiyon objesi
      • return: wrapper içindeki ek davranış + func çağrısı
    """
    def wrapper(*args, **kwargs):
        # ── Buraya eklemek istediğiniz davranışı yazın ──
        print("🛠️  I am decorating your function!")  

        # Orijinal fonksiyonu, aldığı tüm argümanlarla çağır:
        result = func(*args, **kwargs)

        # İsterseniz sonucu da işleyip dönebilirsiniz:
        return result

    # Decorator, wrapper fonksiyonunu döndürür:
    return wrapper


# ───────────────────────────────────────────────────────────
# 2) Decorator’ı uygulama (Syntactic sugar: @my_decorator)
#    - @my_decorator  → hello_world = my_decorator(hello_world)
# ───────────────────────────────────────────────────────────
@my_decorator
def hello_world():
    """
    Orijinal fonksiyon (ConcreteComponent):
      • İçerik: sadece “Hello World!” basıyor
    """
    print("👋 Hello World!")


# ───────────────────────────────────────────────────────────
# 3) Fonksiyonu çağırdığınızda gerçekleşen adımlar:
#    a) hello_world() çağrısı → aslında wrapper() çalışır
#    b) wrapper içindeki print(...) → dekorasyon mesajı
#    c) ardından func(*args, **kwargs) → Hello World!
#    d) wrapper döndürdüğü değeri geri verir
# ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    hello_world()
    # Ekran çıktısı:
    # 🛠️  I am decorating your function!
    # 👋 Hello World!

##############################################################################
# ── Ek Örnek: Parametre Alan Decorator (İmza: @repeat(3)) ─────────────────
##############################################################################

def repeat(times):
    """
    Parametreli decorator:
      • times: fonksiyonun kaç kez çalışacağını söyler
      • return: gerçek decorator fonksiyonu
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"[Run {i+1}/{times}]")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"🎉 Hello, {name}!")

# Eğer direkt çalıştırırsak:
# greet("Besma") şu çıktıyı verir:
# [Run 1/3]
# 🎉 Hello, Besma!
# [Run 2/3]
# 🎉 Hello, Besma!
# [Run 3/3]
# 🎉 Hello, Besma!

##############################################################################
# ── Folder Yapısı ve Ne Var? ────────────────────────────────────────────────
#
# Decorators/                  ← Projenin dekoratörlerle ilgili klasörü
# ├─ decorators.py            ← Bu dosya: dekoratör örnekleri
# └─ README.md                ← Klasörün içinde ne olduğu, nasıl kullanıldığı
#
# README.md içinde (kısa):
#   • my_decorator: temel decorator örneği
#   • repeat: parametreli decorator
#   • Çalıştırmak için: python decorators.py
#
##############################################################################




Yazılım tasarım örüntüleri, yazılım tasarımı sırasında sıkça karşılaşılan, birbirine benzer sorunları çözmek için geliştirilmiş ve işlerliği kanıtlanmış genel çözüm önerileridir. Genel olarak yazılım tasarım örüntüleri programlama dillerinden bağımsız olarak tanımlansalar da, nesneye yönelimli programlama dillerine uygun yazılım tasarım örüntüleri daha çok bilinir. Bu örüntüler, nesneler ve sınıflar arasındaki ilişkileri ve etkileşimleri gösterirler. Programcı bir tasarım örüntüsünü elindeki soruna bakarak özelleştirip kullanabilir.