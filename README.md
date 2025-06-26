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


________________________
1. Magic Methods & Dunder (__dunder__)
Ne?
Python’un sınıf davranışlarını (operatör aşırı yükleme, built-in fonksiyon çağrıları, iterable/yönetici protokolleri vb.) özelleştirmenizi sağlayan özel yöntemler.

Neden?

Kodunuzu Python’un yerleşik tipleriyle aynı sezgisellikle kullanmak için

v1 + v2, print(obj), len(obj), obj() gibi ifadeleri kendi sınıfınıza taşımak için

Nasıl?

python
Copy
Edit
class Vector:
    def __init__(self, x, y):           # Oluşturma
        self.x, self.y = x, y

    def __add__(self, other):           # +
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __repr__(self):                 # repr() / REPL
        return f"Vector({self.x}, {self.y})"

    def __call__(self):                 # obj()
        print("Hello! I was called!")
Gibi metodları tanımlayıp, Python’un “data model” protokollerini takip edersiniz.

2. Tasarım Desenleri (Design Patterns) ve Vector Örneği
Decorator Pattern (OOP):

Amaç: Bir nesnenin davranışını dinamik olarak “etiketlemek” (wrap), alt sınıf oluşturmadan sorumluluk eklemek/çıkarabilmek.

GoF Şablonu: Component ← Decorator ← ConcreteDecorator

Python Karşılığı:

mydecorator(func) → wrapper içindeki ek davranış → func(*args, **kwargs)

Adım adım @mydecorator ile fonksiyonu sararsınız.

Adapter, Strategy, Command, Factory gibi diğer desenleri Vector örneğine uyarlayarak gösterdik:

Adapter: Magic methods (__add__, __repr__, __call__) ile Python operatörlerini sınıfınıza adapte etmek.

Strategy: Farklı toplama algoritmalarını (standard_add, mod_add) add(self, other, strategy=…) ile seçtirmek.

Command: __call__ metoduyla bir nesneyi “komut” gibi kullanmak.

Factory Method: VectorFactory.from_tuple(...), VectorFactory.from_polar(...) gibi statik üreticilerle nesne yaratımı soyutlamak.

3. Python Decorators
Ne?
Bir fonksiyonu başka bir fonksiyonla “sarmak” (wrap) suretiyle giriş/çıkış veya yan etki davranışları ekleyen dil seviyesi kolaylık.

Neden?

Tek Sorumluluk Prensibi: Logging, yetkilendirme, önbellekleme gibi çapraz kesen özellikleri fonksiyondan ayırmak.

Açık/Kapalı Prensibi: Orijinal fonksiyonu değiştirmeden yeni davranış eklemek.

Nasıl?

python
Copy
Edit
def mydecorator(func):
    def wrapper(*args, **kwargs):
        print("Önce bu yazı gelir")
        result = func(*args, **kwargs)
        print("Sonra bu yazı gelir")
        return result
    return wrapper

@mydecorator
def hello(name):
    print(f"Hello, {name}")
Örnekler:

Basic (@mydecorator)

Parametreli (@repeat(3))

Logging (@logged) → print + logfile.txt kaydı

Timing (@timed) → time.time() kullanarak süre ölçümü

Neden *args, **kwargs?
Wrapper’ın orijinal fonksiyonun her tür pozisyonel ve keyword argümanını eksiksiz iletmesi için.

4. Generators
Ne?
yield anahtar kelimesiyle lazy execution sağlayan, ihtiyaç duyulduğunda tek tek değer üreten fonksiyonlar.

Neden?

Bellek Verimliliği: Büyük veya sonsuz dizileri bir kerede değil, gerektiğinde üretmek.

Basitlik: Klasik iterator metotları yerine yield ile kısa ve okunaklı kod.

Nasıl?

python
Copy
Edit
def my_generator(n):
    for i in range(1, n+1):
        yield i**3

gen = my_generator(9_000_000)
print(next(gen))  # 1
print(sys.getsizeof(gen))  # ~112 bayt (sabit)
for cube in gen: print(cube)
sys.getsizeof ile Gösterim:
Generator objesinin çok küçük bir “overhead” tuttuğunu, listeye göre milyarlarca kat bellek tasarrufu sağladığını kanıtlamak için kullanılır.

5. Komut Satırı Argümanları
sys.argv:

Liste halinde tüm komut satırı parametreleri.

sys.argv[0] → betik adı,

sys.argv[1:] → sizin verdiğiniz argümanlar.

Basit Kullanım:

python
Copy
Edit
filename = sys.argv[1]
message  = sys.argv[2]
with open(filename,'w+') as f:
    f.write(message)
Bayraklar (Flags) ile:

Kısa (-f, -m) ve uzun (--filename=, --message=) seçenekleri

getopt.getopt() ile ayrıştırmak:

python
Copy
Edit
import getopt
opts, args = getopt.getopt(
    sys.argv[1:], 
    "f:m:", 
    ["filename=", "message="]
)
for opt, val in opts:
    if opt in ("-f","--filename"): filename = val
    if opt in ("-m","--message"):  message  = val
Neden argparse?
Daha karmaşık bayrak setleri, zorunlu/opsiyonel argümanlar, otomatik yardım (-h/--help) üretmek için argparse modülü tercih edilir.


Encapsulation (Kapsülleme) ve Data Hiding (Veri Gizleme)

Kapsülleme nedir?
Bir sınıfın içindeki verileri ve onları işleyen metotları bir arada tutma prensibidir. Böylece nesne sahibi (caller) sadece “kamuya açık” metotlarla (public API) etkileşime girer, iç yapının detaylarını bilmek zorunda kalmaz.

Veri gizleme (data hiding) nedir?
Sınıf içinde kullandığınız bazı özniteliklerin (attributes) doğrudan dışarıdan okunmasını/yazılmasını engelleme tekniğidir. Python’da bunun en yaygın yolu, öznitelik adının başına çift alt tire (__) koymaktır. Bu, isim mangling (isim çarpıtma) yoluyla dışarıdan erişimi zorlaştırır.