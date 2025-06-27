# ITStajTask
1. m3 macbook pro Apple silicon içine sanal makine kurulumu (VirtualBox)
Debian (ARM 64-bit) tercih edildi 
Chatgpt kullanıldı : https://chatgpt.com/share/685aa279-9c50-800e-aba7-1a678d55750b


🔮 Magic Methods (sihirli metodlar)

🧩 Tasarım Desenleri (Design Patterns)

🌀 Generator’lar (lazy execution)

🛠️ Komut Satırı Argümanları (sys.argv, argparse)

🛡️ Kapsülleme & Veri Gizleme

1️⃣ Vector Sınıfı 🐍

2 boyutlu vektörler oluşturun, toplayın ve okunabilir çıktı alın.

class Vector:
    def __init__(self, x, y):
        """Başlatıcı: x ve y koordinatlarını atar."""
        self.x, self.y = x, y

    def __add__(self, other):
        """`+` operatörünü aşırı yükler: bileşenleri toplayıp yeni Vector döndürür."""
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        """`print(v)` okunuşunu `Vector(x, y)` şeklinde düzenler."""
        return f"Vector({self.x}, {self.y})"

Kullanım Örneği:

v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2
print(v3)  # 👉 Vector(60, 80)

Açıklama:

__init__: Nesne oluştururken bileşenleri (x, y) tanımlar.

__add__: v1 + v2 ifadesini mümkün kılar.

__repr__: Konsolda temiz, anlaşılır bir çıktı sağlar.

2️⃣ Python Decorator’ları 🎉

Fonksiyonların giriş/çıkışlarına dinamik davranış ekleyin.

🔹 a) Temel Decorator

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("🛠️ Fonksiyon dekoratöründen önce bu mesaj gelir!")
        result = func(*args, **kwargs)
        print("✅ Fonksiyon tamamlandı.")
        return result
    return wrapper

@my_decorator
def hello_world():
    print("👋 Hello World!")

Adımlar:

@my_decorator ile orijinal hello_world fonksiyonu wrapper ile sarılır.

Tek Sorumluluk Prensibi: Logging, yetkilendirme, önbellekleme gibi çapraz kesen özellikleri fonksiyondan ayırmak.

Açık/Kapalı Prensibi: Orijinal fonksiyonu değiştirmeden yeni davranış eklemektir.
hello_world() çalıştığında önce dekoratör mesajları, sonra fonksiyon çalışır.

🔹 b) Parametreli Decorator

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"🔃 Çalıştırma {i+1}/{times}")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"🎉 Merhaba, {name}!")

Not: greet("Besma") 3 kez çağrılır.


3️⃣ Magic Methods & Tasarım Desenleri 🧩

Magic Methods: __call__, __len__, __iter__ gibi yerleşik protokolleri özelleştirir.

Decorator Pattern: Yeni sorumlulukları alt sınıf oluşturmadan ekler.

Adapter, Strategy, Command, Factory: Kodunuzu esnek ve genişletilebilir kılar.

4️⃣ Generator’lar 🌀

def cubes(n):
    for i in range(1, n+1):
        yield i**3

yield: Her seferinde bir değer üretir, bellek kullanımı minimum.

5️⃣ Komut Satırı Argümanları 🛠️

sys.argv: Tüm parametreleri listeler (sys.argv[0] betik adı).

argparse: Zorunlu/opcional seçenekler, otomatik -h yardım mesajı.

6️⃣ Kapsülleme & Veri Gizleme 🛡️

Kapsülleme: Verileri (attributes) ve işlemleri (methods) bir arada tutar.

Veri Gizleme: __private öznitelikler ile dış erişimi kısıtlar (name mangling).





