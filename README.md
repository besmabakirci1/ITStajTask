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




<<<<<<< Updated upstream

=======
🌿 Kapsülleme nedir?
Bir sınıfın içindeki verileri ve onları işleyen metotları bir arada tutma prensibidir. Böylece nesne sahibi (caller) sadece “kamuya açık” metotlarla (public API) etkileşime girer, iç yapının detaylarını bilmek zorunda kalmaz.

🌿 Veri gizleme (data hiding) nedir?
Sınıf içinde kullandığınız bazı özniteliklerin (attributes) doğrudan dışarıdan okunmasını/yazılmasını engelleme tekniğidir. Python’da bunun en yaygın yolu, öznitelik adının başına çift alt tire (__) koymaktır. Bu, isim mangling (isim çarpıtma) yoluyla dışarıdan erişimi zorlaştırır.
------------------------------
🧙‍♀️ Magic (Dunder) Methods Nedir?
Magic methods, Python'da çift alt çizgi (__) ile başlayan ve biten özel metotlardır.
Bu metotlara bazen dunder methods (double underscore = dunder) da denir.

Bu metotlar, Python'un içsel işleyişine yön verir.
Yani, toplama +, çağırma (), yazdırma print(), silme del, uzunluk len() gibi ifadelerin arkasında çalışan metotlardır.
    🎯 Neden Kullanılır?
    Python sınıflarını daha anlamlı, esnek ve kullanışlı hale getirir.
    Operatör aşırı yüklemesi sayesinde +, -, *, ==, <, > gibi ifadeler özelleştirilebilir.
    Kodunuzu dışarıya daha güzel ve okunabilir bir şekilde sunmanızı sağlar.
    Büyük projelerde objeler arası etkileşimi kontrol etmek için vazgeçilmezdir.

🎀 Decorator (Dekoratör) Nedir?
Decorator, Python’da bir fonksiyonun davranışına dışarıdan yeni özellikler eklemek için kullanılan bir yapıdır. Asıl fonksiyonu bozmadan, onu bir "sargı" (wrapper) fonksiyonla çevreleyip, öncesine ya da sonrasına ekstra işlem koymamızı sağlar.

🔧 Teknik Olarak Nasıl Çalışır?
Bir dekoratör fonksiyonu, başka bir fonksiyonu parametre olarak alır.

İçerisinde bir wrapper (sargı) fonksiyon tanımlar.

Bu wrapper fonksiyonda:

Ek kodlar yazılır (örn. loglama, zaman ölçme, izin kontrolü),

Ardından asıl fonksiyon çalıştırılır.

En sonunda, bu wrapper fonksiyonu geri döndürülür.

Kullanımda fonksiyonun üstüne @decorator_ismi yazılır.



⚙️ Generator (Üreteç) Nedir?
Generator, Python’da belleği verimli kullanarak büyük veri yapılarıyla çalışmamıza olanak sağlayan özel bir fonksiyon tipidir. Normal return yerine yield kullanır.

🧠 Nasıl Çalışır?
Generator fonksiyonu çağrıldığında bellekte tüm listeyi oluşturmaz.

yield ifadesine kadar olan kısmı çalıştırır, durur ve değeri döner.

next() fonksiyonu ile bir sonraki yield’e kadar devam eder.

Bu sayede "lazy evaluation" (tembel değerlendirme) yapılır: sadece ihtiyaç olduğunda veri üretilir.


💡 Avantajları:
✅ Bellek tasarrufu sağlar (örneğin: 10 milyon elemanlık liste oluşturmaz).

✅ Sonsuz veri üretilebilir (while True ile).

✅ Daha verimli ve hızlı çalışır.

Python'da argument parsing, komut satırından bir script'e dışarıdan parametre (argüman) vermeyi sağlar. Bu, özellikle sistem programlama ve ağ (network) script'lerinde önemlidir. Python dosyaları genellikle terminalde python script.py şeklinde çalıştırılır; bu yapıya "komut satırı argümanları" eklemek için sys.argv listesi ve getopt modülü kullanılır:

✅ 1. sys.argv ile Temel Argüman Okuma:
sys.argv, komut satırından girilen tüm argümanları içeren bir listedir.

sys.argv[0]: script'in adıdır.

sys.argv[1], sys.argv[2], ...: kullanıcı tarafından girilen argümanlardır.

Örnek:

bash
Copy
Edit
python script.py output.txt "Hello World"
Kodda:

python
Copy
Edit
import sys
filename = sys.argv[1]
message = sys.argv[2]
✅ 2. *args ve **kwargs ile Fonksiyonlarda Esnek Parametre Kullanımı:
*args: sırasız (positional) argümanları alır (tuple).

**kwargs: anahtar-değer çiftlerini alır (dict).

✅ 3. getopt Modülü ile Opsiyonel Argümanlar:
getopt.getopt() fonksiyonu ile -f gibi kısa seçenekler veya --file gibi uzun seçenekler tanımlanabilir.

"f:m:" şeklinde iki nokta (:) kullanımında, o seçeneğin bir değer beklediği anlamına gelir.

Örnek:

bash
Copy
Edit
python script.py -f output.txt -m "Hello World"
Kod:

python
Copy
Edit
import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["file=", "message="])
for opt, arg in opts:
    if opt in ("-f", "--file"):
        filename = arg
    elif opt in ("-m", "--message"):
        message = arg
💡 Avantajları:
Komut satırından veri girilmesini sağlar.

Script'i daha esnek ve yeniden kullanılabilir kılar.

Varsayılan değerlerle birlikte opsiyonel yapı kurulabilir.


Python'da argument parsing, komut satırından script'e parametre almayı sağlar.

🔹 sys.argv: Komut satırındaki tüm argümanları liste olarak verir.
🔹 getopt: -f, --file gibi opsiyonel ve anahtar-değer şeklinde argümanları yönetir.
🔹 *args, **kwargs: Fonksiyonlara esnek sayıda argüman göndermek için kullanılır.

💡 Amaç: Script'i daha esnek, tekrar kullanılabilir ve dışarıdan veri alabilir hale getirmektir.
🔐 Encapsulation (Kapsülleme) ve Data Hiding (Veri Gizleme)
Python’da __ (çift alt çizgi) ile tanımlanan özellikler private (özel) hale gelir. Dışarıdan doğrudan erişilemez:

python
Copy
Edit
self.__name = name
Bu özel alanlara erişim için getter ve değer atamak için setter yöntemleri kullanılır:

python
Copy
Edit
@property
def Name(self): return self.__name

@Name.setter
def Name(self, value): self.__name = value
Getter/setter yöntemleri sayesinde sınıf içindeki verilere kontrollü erişim sağlanır (örneğin: name == "Bob" ise farklı davran).

⚙️ Static Method (Statik Metot)
@staticmethod ile tanımlanan metotlar, sınıfın herhangi bir örneğine (objesine) bağlı olmadan çalışabilir.

self parametresi almaz.

Sınıf adıyla doğrudan çağrılabilir:

python
Copy
Edit
class Person:
    @staticmethod
    def greet(): print("Hello!")

Person.greet()  # Hello!
💡 Ana Fikir:
Encapsulation, nesnenin iç durumunu gizler ve kontrollü şekilde dışarıya açar.

Static method, sınıf örneğine ihtiyaç duymadan çalışan yardımcı fonksiyonlardır.

Bu yapılar birlikte kullanıldığında, daha güvenli, modüler ve bakımı kolay bir nesne yönelimli yazılım mimarisi oluşturulur.


🧠 Type Hinting (Tür İpuçları) – Python'da Ne ve Neden?
Python dinamik tür tanımlamalı (dynamically typed) bir dildir; yani bir değişkenin türü, çalışma zamanında (runtime) belirlenir. Bu durum esnek olsa da, büyük projelerde hataların erken tespiti ve kodun okunabilirliği açısından sorun oluşturabilir.

👇 Ne Yapılır?
Python 3.5+ ile birlikte gelen type hinting, fonksiyonlara ve değişkenlere tür belirtmemizi sağlar:

python
Copy
Edit
def topla(x: int, y: int) -> int:
    return x + y
Bu kodda:

x ve y değişkenleri int (tam sayı) olmalıdır.

Fonksiyonun dönüş değeri de yine int türündedir.

Ama dikkat! Python bu yazımı çalışma zamanında zorunlu kılmaz. Bu bir not gibidir.

🧪 Peki bu ne işe yarar?
Kodun tür kurallarına uyup uymadığını doğrulamak için mypy gibi bir araç kullanılır:

bash
Copy
Edit
mypy main.py
Bu araç, fonksiyona yanlış türde veri gönderdiğinizde hata verir:

python
Copy
Edit
def greet(name: str) -> str:
    return f"Hello {name}"

greet(42)  # mypy burada uyarı verir: int yerine str bekleniyor
🔁 Return Type (Dönüş Tipi) ve Katmanlı Kullanım
Fonksiyonların sadece parametreleri değil, dönüş tipleri de tip ipucu ile belirtilir.

Böylece bir fonksiyonun başka bir fonksiyona verdiği değerin uyumlu türde olup olmadığı da kontrol edilebilir.

📦 Python 3.9+ Özelliği: Liste Tipleri
Python 3.9'dan itibaren liste gibi koleksiyonlara özel tip belirtebilirsiniz:

python
Copy
Edit
def toplam(liste: list[int]) -> int:
    return sum(liste)
Yani bu fonksiyon sadece int içeren listeler için çalışmalı deriz.

📌 Özetle:
Type hinting, Python kodunu daha okunur ve hatalara karşı daha güvenli hale getirir.

Zorunlu değil, ama mypy gibi araçlarla birlikte kullanıldığında statik tür kontrolü sağlar.

Büyük projelerde, takım çalışmasında ve IDE desteğinde büyük avantaj sağlar.

Python yine de esnekliğini korur; yanlış tür verilse bile çalıştırır (mypy kullanmazsanız).

Dilerseniz bu konuyla ilgili örnekler, uygulamalar veya quiz şeklinde tekrar sorularla daha da pekiştirebiliriz 🌟




🌸 Factory Pattern ve Flyweight Pattern,
yazılım geliştirmede kodun esnekliğini ve performansını artırmak için kullanılan iki önemli tasarım desenidir. Factory Pattern, bir nesne oluşturma işlemini merkezi bir "fabrika" sınıfına devrederek, hangi sınıfın örneği gerektiğini dış dünyadan gizler ve böylece yeni nesne türleri eklemeyi kolaylaştırır; örneğin bir PersonFactory sınıfı, gelen isteğe göre Student ya da Teacher nesnesi oluşturabilir. Bu desen, kodun genişletilebilirliğini ve bakımı kolaylaştırır. Öte yandan, Flyweight Pattern, bellekte çok sayıda benzer nesne gerektiğinde kullanılır ve ortak özellikleri paylaşarak gereksiz kopyaların önüne geçer. Böylece performans ve bellek kullanımı optimize edilir. Özellikle grafik uygulamaları ve oyun motorlarında sıkça tercih edilir. Her iki desen de yazılımda tek sorumluluk ilkesi, açık-kapalı prensibi ve kaynak verimliliği gibi nesne yönelimli programlamanın temel ilkelerine hizmet eder.

🏭 Factory Design Pattern Nedir?
Factory Design Pattern, nesne yönelimli programlamada kullanılan bir tasarım desenidir ve amacı, nesne yaratımını merkezi ve dinamik hale getirmektir. Bu desenle, kodlama aşamasında hangi alt sınıftan (örneğin Student, Teacher) nesne oluşturacağımıza karar vermek yerine, bunu çalışma zamanında (runtime) dinamik olarak belirleriz. Bu da kodun modülerliğini artırır, sorumlulukların ayrımını (separation of concerns) sağlar ve özellikle büyük projelerde sınıflar arası bağımlılığı azaltır. Python’da bunu, IPerson gibi bir arayüz (interface) tanımlayıp, bu arayüzü uygulayan (implements) Student ve Teacher gibi sınıflarla ve bu sınıfları üretecek bir PersonFactory sınıfıyla gerçekleştiriyoruz. PersonFactory.build_person("Student") çağrısı örneğin bir Student nesnesi oluşturur. Böylece, nesne üretimi tek bir yerden kontrol edilir ve sistemin genişletilebilirliği artar.

🌸 Proxy Design Pattern,
 bir nesneye doğrudan erişim yerine, onun önüne bir “vekil” (proxy) yerleştirerek erişimi kontrol etmek, gizlemek, ya da ek işlevler eklemek için kullanılır. Bu desende asıl iş yapan sınıf (Person), IPerson adlı bir arayüzü (interface) uygular. Ancak bu sınıfın doğrudan örneklenmesini engellemek veya sarmalamak istediğimizde, devreye ProxyPerson sınıfı girer. ProxyPerson, aynı arayüzü uygular ve içeride bir Person nesnesi oluşturur. person_method fonksiyonu çağrıldığında önce kendi mesajını verir, sonra gerçek Person nesnesine yönlendirerek işi devreder. Böylece nesne oluşturma ve erişim sürecine bir ara katman (middleman) eklenmiş olur. Bu yapı özellikle güvenlik, erişim kontrolü, önbellekleme (caching), loglama gibi işlemler için kullanılır. Kısacası proxy, nesneye ulaşmadan önce araya girerek "kontrollü kapı bekçiliği" yapar.

 🎯 Singleton Design Pattern Nedir?
Amaç: Bir sınıftan (class) sadece tek bir örnek (instance) oluşturulmasını garanti altına almak.
Böylece, sistemde birden fazla kişi bu sınıfa erişmeye çalışsa bile, her zaman aynı nesne (örnek) döner.


🌸 Composite Design Pattern,
 nesneleri ağaç yapısı şeklinde düzenlemeye ve bu yapılar üzerinde aynı işlemleri gerçekleştirmeye olanak tanıyan bir tasarım desenidir. Bu desende, hem "bileşen" (yaprak sınıf) hem de "bileşik" (alt bileşenleri olan sınıf) aynı arayüzü (interface) uygular. Bu sayede tüm yapıya homojen bir şekilde işlem yapılabilir.
    Örneğin:
    🧩 Bir "Yönetim Departmanı", içinde "Muhasebe" ve "Yazılım" departmanlarını barındırır ve toplam çalışan sayısını bu şekilde hesaplar. Bu yapı, karmaşık organizasyonel sistemlerin veya ağaç benzeri yapıların modellenmesinde son derece kullanışlıdır.
>>>>>>> Stashed changes
