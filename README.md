**Selamlar 🌷**

Bu README, birinci adım olarak MacBook Pro M3 (Apple Silicon) üzerinde sanal makine kurulumu ve ardından Python'da ileri seviye kavramları öğrenme akışını kronolojik sırayla sunar. Her bölümde ilgili kod bloklarının ne işe yaradığını, nasıl çalıştığını aşamalı olarak açıklayan notlar yer almaktadır.

---

## İçindekiler

| Bölüm | Konu                                              |
| :---: | :------------------------------------------------ |
|  1.0  | Sanal Makine Kurulumu (VirtualBox + Debian ARM64) |
|  2.0  | Magic Methods (Dunder Metotlar)                   |
|  3.0  | Decorator’lar                                     |
|  4.0  | Tasarım Desenleri (Design Patterns)               |
|  5.0  | Generator’lar                                     |
|  6.0  | Komut Satırı Argümanları                          |
|  7.0  | Kapsülleme & Veri Gizleme                         |
|  8.0  | Type Hinting                                      |
|  9.0  | Detaylı Tasarım Desenleri                         |

---

## 1.0 Geliştirme Ortamı Kurulumu

**Adım 1:** VirtualBox indirme ve kurulum

```bash
# https://www.virtualbox.org adresinden macOS sürümünü indirip kurun.
```

> **Açıklama:** VirtualBox, Apple Silicon destekli ön sürümleriyle ARM64 tabanlı VM oluşturmanızı sağlar.

**Adım 2:** Debian ARM64 ISO hazırlama

```bash
# Debian ARM64 ISO dosyasını https://www.debian.org/ARM64 adresinden indirin.
```

> **Açıklama:** ARM64 dağıtımı, M3 çiple uyumlu çalışır.

**Adım 3:** Yeni VM oluşturma ve ayarlar

| Öğe             | Değer                       |
| --------------- | --------------------------- |
| İşletim Sistemi | Debian (Linux / ARM 64-bit) |
| Bellek (RAM)    | 4 GB veya üstü              |
| Depolama        | 20 GB VDI                   |
| Ağ Adaptörü     | NAT veya Bridge             |

> **Açıklama:** Bellek ve depolama, derleme süreçleri için yeterli olmalıdır.

---

## 2.0 Magic Methods (Dunder Metotlar)

Python sınıflarının özel davranışlarını tanımlayan çift alt çizgiyle başlayan metotlardır.

```python
class Vector:
    def __init__(self, x, y):
        """Nesne oluşturulurken x ve y bileşenlerini atar."""
        self.x, self.y = x, y

    def __add__(self, other):
        """`+` operatörünü özelleştirir: bileşenleri toplayıp yeni Vector döndürür."""
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        """`print(v)` ifadesini `Vector(x, y)` formatında gösterir."""
        return f"Vector({self.x}, {self.y})"
```

> **Açıklama Aşamaları:**
>
> 1. `__init__` – Başlatıcı yapıcı metod, x ve y değerlerini nesneye kaydeder.
> 2. `__add__` – v1 + v2 işlemi çağrıldığında devreye girer, yeni Vector nesnesi üretir.
> 3. `__repr__` – Konsolda temiz ve okunabilir çıktı sağlar.

---

## 3.0 Decorator’lar

Fonksiyonların girişine/çıkışına dinamik davranış eklemeye yarar.

### 3.1 Temel Decorator

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("🛠️ Öncesi mesaj")
        result = func(*args, **kwargs)
        print("✅ Sonrası mesaj")
        return result
    return wrapper

@my_decorator
def hello_world():
    print("👋 Hello World!")

hello_world()
```

> **Açıklama:**
>
> 1. `@my_decorator` ile `hello_world` fonksiyonu `wrapper` ile sarılır.
> 2. `wrapper` çalışırken önce ek işlem, sonra orijinal fonksiyon, en son ek işlem yapılır.

### 3.2 Parametreli Decorator

```python
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

greet("Besma")
```

> **Açıklama:**
>
> * `repeat(3)` ile decorator fonksiyonuna parametre verilir.
> * `wrapper` içinde `func` belirtilen kez çağrılır.

---

## 4.0 Tasarım Desenleri (Design Patterns)

Kodun modülerliğini ve genişletilebilirliğini artıran tekrarlanabilir çözümlerdir.

| Desen Adı | Amaç                                                  |
| --------- | ----------------------------------------------------- |
| Factory   | Nesne oluşturmayı merkezi hale getirir                |
| Proxy     | Asıl nesneye erişimi kontrol eder                     |
| Singleton | Tekil örnek sağlar                                    |
| Composite | Ağaç yapısındaki nesneleri homojen işlemlerle yönetir |
| Flyweight | Bellek optimizasyonu yapar                            |

> **Not:** Örnek uygulamalar 9.0 bölümünde detaylı işlenmiştir.

---

## 5.0 ⚙️Generator’lar

Bellek kullanımını minimuma indirerek "lazy evaluation" sağlar. Normal return yerine yield kullanır.

```python
def cubes(n):
    for i in range(1, n+1):
        yield i**3

for val in cubes(5):
    print(val)  # 1, 8, 27, 64, 125
```

> **Açıklama:**
>
> * `yield` ile değerler tek tek üretilir.

> * Tüm liste bellekte tutulmaz.

> *  in detail : Generator fonksiyonu çağrıldığında bellekte tüm listeyi oluşturmaz. yield ifadesine kadar olan kısmı çalıştırır, durur ve değeri döner. next() fonksiyonu ile bir sonraki yield’e kadar devam eder. Bu sayede "lazy evaluation" (tembel değerlendirme) yapılır: sadece ihtiyaç olduğunda veri üretilir.
---

## 6.0 Komut Satırı Argümanları

`sys.argv` ve `argparse` ile script’lere dışarıdan parametre ekler.

```python
import sys, argparse

parser = argparse.ArgumentParser(description="CLI Örneği")
parser.add_argument("-n", "--name", required=True, help="İsim girin")
args = parser.parse_args()
print(f"Merhaba {args.name}!")
```

> **Açıklama:**
>
> 1. `ArgumentParser` ile parametreler tanımlanır.
> 2. `-h` yardımı otomatik oluşturulur.
> 3. `args.name` ile değere erişilir.

---

## 7.0 Kapsülleme & Veri Gizleme

Sınıf içi verileri korur ve dış erişimi kontrol eder.

```python
class Person:
    def __init__(self, name):
        self.__name = name  # private attribute

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("İsim en az 2 karakter olmalı.")
        self.__name = value
```

> **Açıklama:**
>
> * `__name` ile doğrudan erişim engellenir.
> * `@property` ve `@setter` ile kontrollü erişim sağlanır.

---

## 8.0 Type Hinting

Kod okunabilirliğini ve statik analiz desteğini artırır.

```python
from typing import List

def toplam(liste: List[int]) -> int:
    return sum(liste)

print(toplam([1, 2, 3]))
```

> **Açıklama:**
>
> * `List[int]` ve `-> int` bildirimi not niteliğindedir.
> * `mypy` gibi araçlarla hatalar önceden yakalanabilir.

---

## 9.0 Detaylı Tasarım Desenleri

### 9.1 Factory Pattern

```python
class IPerson:
    def get_role(self): pass
class Student(IPerson):
    def get_role(self): return "Student"
class Teacher(IPerson):
    def get_role(self): return "Teacher"
class PersonFactory:
    @staticmethod
    def build(person_type):
        if person_type == "Student": return Student()
        if person_type == "Teacher": return Teacher()
        raise ValueError("Geçersiz tip")
```

> **Açıklama:**
>
> * `PersonFactory.build()` ile nesne türü runtime'da belirlenir.

### 9.2 Proxy Pattern

```python
class RealService:
    def request(self): print("Gerçek hizmet çağrıldı")
class ProxyService:
    def __init__(self): self._service = RealService()
    def request(self):
        print("Erişim kontrolü yapılıyor")
        self._service.request()
```

> **Açıklama:**
>
> * Proxy, gerçek hizmete erişmeden önce veya sonra ek işlemler yapar.

### 9.3 Singleton Pattern

```python
class SingletonMeta(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Database(metaclass=SingletonMeta):
    pass
```

> **Açıklama:**
>
> * `SingletonMeta` ile sınıftan tek örnek oluşturulur.

### 9.4 Composite Pattern

```python
class Component:
    def operation(self): pass
class Leaf(Component):
    def operation(self): print("Leaf işlemi")
class Composite(Component):
    def __init__(self): self._children = []
    def add(self, comp): self._children.append(comp)
    def operation(self):
        for child in self._children:
            child.operation()
```

> **Açıklama:** Ağaç yapısındaki tüm bileşenlere homojen işlem uygulanır.

### 9.5 Flyweight Pattern

```python
class FlyweightFactory:
    _pool = {}
    @classmethod
    def get(cls, key):
        if key not in cls._pool:
            cls._pool[key] = object()
        return cls._pool[key]
```

> **Açıklama:** Ortak nesneler havuzdan tekrar kullanılır, bellek tasarrufu sağlanır.

---


Odoo for debian "manually"

### make sure that sudo works
su
apt-get update
apt-get upgrade
apt install sudo
nano /etc/sudoers
###################
# make sure to write your username instead of "user"
user ALL=(ALL:ALL) ALL
exit

### Installing the required packages
sudo apt install make gcc curl python3-virtualenv autoconf automake build-essential python3-dev libssl-dev libpq-dev libldap2-dev libffi-dev libxslt1-dev libxml2-dev libblas-dev libatlas-base-dev zlib1g-dev libjpeg-dev postgresql libsasl2-dev

### configure postgres, create a role in username 
sudo su -l postgres
psql
################### 
#make sure to write your username instead of "user"
CREATE role user with login createdb;
\q
exit

### download python and odoo
wget https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tgz
wget http://nightly.odoo.com/16.0/nightly/tgz/odoo_16.0.latest.tar.gz

### install python and configure it 
tar -zxvf Python-3.10.13.tgz
cd Python-3.10.13
./configure --with-openssl=/usr/
sudo make install
python3.10 -m pip install --upgrade pip setuptools

### extract odoo files and create virtual envierment
tar -zxvf odoo_16.0.latest.tar.gz
mv odoo-16.0* ./odoo-16
cd odoo-16
virtualenv -p python3.10 env16
source env16/bin/activate 

### install odoo's requirement and create odoo-bin
pip install --upgrade pip setuptools
pip install -r requirements
cp setup/odoo ./odoo-bin
chmod u+x odoo-bin
./odoo-bin 


----

Ssh Bağlantısı yapmak sanal makine ve local host arasında :

systemctl status ssh

- macOS’te SSH durumunu nasıl kontrol ederiz?
sudo systemsetup -getremotelogin
🔹 Remote Login: On → SSH aktif
🔹 Remote Login: Off → SSH kapalı

- SSH’yi açmak:
sudo systemsetup -setremotelogin on


- SSH aktif mi port dinliyor mu?
sudo lsof -iTCP -sTCP:LISTEN -n -P | grep sshd

- IP adresinizi öğrenmek için:
ipconfig getifaddr en0
( inet 10.x.x.x gibi bir adres arayın. )

- SSH Servisinin Durumunu Terminalden Kontrol Edelim
sudo launchctl list | grep ssh
( Eğer çıktı yoksa SSH arka planda çalışmıyor olabilir. )

- SSH Servisini Terminalden Manuel Başlat (Yalnızca geçici çözüm)
sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist
(Bu komut macOS’te yerleşik olan SSH servis tanımını yükler ve başlatır.)

- Debian VM’de terminalden IP’yi öğrenmek için:
ip a

Test için:
Eğer başka bir cihaz yoksa kendi MacBook’unuzda ikinci bir terminal açarak ssh localhost komutuyla bağlantı test edebilirsiniz:

ssh basmabakirci@localhost
-
Attached to: NAT to Bridged Adapter 
 - ping **.**.*.***
Eğer yanıt alamazsanız, ağ bağlantısı yok demektir.

vs code ta bağlanmak sanal makineye cihazın kendisinden 
vs code aç sol en altta mavi bir >< diye bir buton var open the remote window kısmından connect to host kısmı var onunla bağlanıyoruz:

---
07.08.2025 and 08.08.2025:
- understanding backpropagation algorithm
- Cognitive phycology
- electric electronic engineering
- nourology

https://www.youtube.com/watch?v=B5MmXmMMuvI&t=13s
https://youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&si=tqCmhAkeq9aXqMhm
http://neuralnetworksanddeeplearning.com/chap1.html

---

1. **Rastgele Başla**

   * Ağırlıklar ve bias’lar (yaklaşık 13 000 sayı) rastgele seçilir.
   * Henüz hiçbir fikri yoktur; tahminleri “çorap içinde rakam” gibi karışık olur.

2. **Tahmin Yap (Forward Pass)**

   * 28×28 piksellik resmi alır, her pikseli 0–1 arasına dönüştürür.
   * Bu değerler giriş katmanındaki 784 nöronu “yak” (aktivasyon = pikselin parlaklığı).
   * Katman katman ilerle, her nöron kendine gelen aktivasyonları ağırlıklarıyla çarp, topla, bias ekle, sıkıştırıcı fonksiyondan geçir (sigmoid/ReLU).
   * Son katmanda 10 sayı elde et; en büyük olanı “tahmin” olarak seç.

3. **Hata Ölç (Maliyet Fonksiyonu)**

   * Tahmin ile gerçek etiket arasındaki farkı kare al, her çıkış nöronu için topla, tüm örneklerin ortalamasını al → bu senin “maliyetin” (error).
   * Büyük hata = kötü; küçük hata = iyi.

4. **Nasıl Daha İyi Olacağını Bul (Gradyan Hesabı)**

   * Hangi ağırlığı biraz artırsak ya da azaltırsak “hata” ne kadar değişir, ona bak.
   * Bunu, her parametrenin maliyeti ne kadar “hissedeceğini” (türevi) hesaplayarak yapıyoruz.
   * Basit benzetme: En dik iniş yönünü bulmak için tepeyi tararız.

5. **Ağırlıkları Güncelle (Gradient Descent)**

   * Her bir ağırlığı, “maliyeti en çok düşüren” yönde ve küçük bir adımla değiştir:

     $$
       w \;\gets\; w \;-\;\eta\;\frac{\partial C}{\partial w}
     $$
   * Burada $\eta$ (eta), adım büyüklüğü yani “öğrenme hızı”.

6. **Tekrar Et**

   * Yeni ağırlıklarla tekrar “Tahmin Yap → Hata Ölç → Güncelle” döngüsünü yüzlerce, binlerce kez uygula.
   * Her adımda hata azalır, ağ “öğrenir” ve rakamları doğru tahmin etmeye başlar.

7. **Mini-Batch İyileştirmesi**

   * Tüm eğitimi her seferinde binlerce resme bakarak yapmak yavaş;
   * Onun yerine küçük rastgele gruplar (“mini-batch”) kullan, böylece her adım daha hızlı hesaplanır.

---

**Özetleyelim:**

* Sinir ağı önce “tamamen bilgisiz” başlar.
* Resimleri bir katmandan diğerine iletip tahmin eder.
* Tahminin ne kadar kötü olduğunu ölçer.
* Hangi yönde değişirse hatanın azalacağını (gradyanı) hesaplar.
* Ağırlıkları küçük adımlarla o yöne kaydırır.
* Döngüyü tekrar tekrar çalıştırarak ağı eğitir ve doğruluğunu artırır.

Bu basit döngü—**Tahmin → Hata → Gradyan → Güncelleme**—sayesinde sinir ağı “öğrenir.”


## 1. Maliyet (Cost) Hesabı

*(İlk görüntü: çıktı farklarının kareleri)*

1. Ağımızın **10 çıkış nöronu** var; her biri 0–1 arası bir değer üretiyor.
2. Diyelim gerçek sayı “4”, dolayısıyla doğru cevap vektörü (one-hot) şöyle:

   ```
   [0,0,0,0,1,0,0,0,0,0]
   ```
3. Ağın verdiği çıktı örneğin:

   ```
   [0.28, 0.32, 0.32, 0.95, 0.83, 1.00, 0.63, 0.44, 0.14, 0.69]
   ```
4. Her bileşen için:

   $$
     (\text{çıktı}_k - \text{hedef}_k)^2
   $$

   *örneğin (0.83−1.00)², (1.00−0.00)², vs.*
5. Bütün bu kareleri **topluyoruz** → bu tek resim için “maliyet”.
6. Eğitim verisindeki tüm fotoğrafların malietlerini **ortalıyoruz** → ağın genel malieti.

---

## 2. Bir Nöronun Aktivasyonu

*(İkinci görüntü: 0.2 = σ(w·a + b))*

Her nöron üç şey yapar:

1. **Ağırlıklı Toplam**

   $$
     z = w_0\,a_0 + w_1\,a_1 + \dots + w_n\,a_n + b
   $$

   * $a_i$: bir önceki katmandaki i’inci nöronun aktivasyonu
   * $w_i$: o nörondan gelen bağlantının ağırlığı
   * $b$: bias (ekstra sabit sayı)

2. **Aktivasyon Fonksiyonu**

   $$
     a = \sigma(z)
     \quad\text{(sigmoid fonksiyonu: 0–1 arası sıkıştırır)}
   $$

3. **“Nasıl Artırırım?”**

   * Bias’ı ($b$) biraz artırırsam $z$ büyür → $a$ artar
   * Özellikle büyük $a_i$ ile çarpılan $w_i$’yi artırırsam daha etkili olur
   * (Ancak gerçek eğitimde direkt $a_i$ değiştiremeyiz, sadece $w,b$ güncelleriz.)

---

## 3. Vektör/Matriks İfadesi (Vectorization)

*(Üçüncü görüntü: W·a = ?)*

Tek bir nöron yerine **tüm katmanı** bir kerede hesaplamak için:

1. **Aktivasyon vektörü** $a^{(0)}$:

   $$
     \begin{bmatrix}a_0 \\ a_1 \\ \vdots \\ a_n\end{bmatrix}
     \quad(\text{örneğin }784\times1)
   $$

2. **Ağırlık matrisi** $W$:

   $$
     W = 
     \begin{bmatrix}
       w_{0,0} & w_{0,1} & \dots & w_{0,n} \\
       w_{1,0} & w_{1,1} & \dots & w_{1,n} \\
       \vdots & \vdots & \ddots & \vdots \\
       w_{m,0} & w_{m,1} & \dots & w_{m,n}
     \end{bmatrix}
     \quad(m\times n)
   $$

3. **Bias vektörü** $b$:

   $$
     \begin{bmatrix}b_0\\b_1\\\vdots\\b_m\end{bmatrix}
   $$

4. **Tek adımda hesaplama**

   $$
     z^{(1)} = W\,a^{(0)} + b,
     \quad
     a^{(1)} = \sigma\bigl(z^{(1)}\bigr)
   $$

   * Böylece tüm sonraki katmanın $m$ nöronu için aktivasyonları bir defada bulmuş olursunuz.

---

**Kısa Özet**

1. **Maliyet:** Çıktı ile hedef arasındaki farkların karelerini topla, ortala.
2. **Nöron:** Önce ağırlıklı toplam, sonra sigmoid ile sıkıştır → aktivasyon.
3. **Vektör/Matriks:** Bireysel toplama gerek kalmadan “W·a + b” formülüyle tüm katmanı hızlıca hesapla.


## Ağırlığa Göre Maliyeti Hesaplamak

* **Soru:** Bir ağırlık $w$ – ki bu, örneğin son katmandaki tek bir bağlantının gücü olsun – ne kadar değiştirilirse, maliyet fonksiyonu $C$ ne kadar değişir?
* Bunu matematiksel olarak

  $$
    \frac{\partial C}{\partial w}
  $$

  ifadesiyle sorarız: “$w$’yi 0.01 artırırsam $C$ ne kadar değişir?”

---

## 2. Zincir Kuralı (Chain Rule) Nasıl Uygulanır?

Diyelim tek bir yol var:

$$
  w \;\longrightarrow\; z \;\longrightarrow\; a \;\longrightarrow\; C
$$

* **$z$:**   $z = w\cdot a_{\text{önceki}} + b$ (ağırlıklı toplam + bias)
* **$a$:**   $a = \sigma(z)$ (sigmoid veya ReLU ile sıkıştırma)
* **$C$:**   $(a - y)^2$ (hedef $y$ ile arasındaki kare fark)

Bu üç aşamayı, küçük bir $w$ değişikliğinin maliyete nasıl yansıdığını bulmak için zincir kuralıyla çarparız:

$$
  \frac{\partial C}{\partial w}
  =
  \underbrace{\frac{\partial C}{\partial a}}_{\displaystyle\text{1) }2(a - y)}\;\times\;
  \underbrace{\frac{\partial a}{\partial z}}_{\displaystyle\text{2) }\sigma'(z)}\;\times\;
  \underbrace{\frac{\partial z}{\partial w}}_{\displaystyle\text{3) }a_{\text{önceki}}}
$$

1. **$\partial C/\partial a = 2(a - y)$:**

   * Ne kadar “yanlış” olduğumuzu (a ile y farkı) gösterir.
2. **$\partial a/\partial z = \sigma'(z)$:**

   * Sigmoid’in eğimi – $z$’deki küçük değişikliğin $a$’yı ne kadar değiştirdiği.
3. **$\partial z/\partial w = a_{\text{önceki}}$:**

   * Ağırlığı ne kadar artırırsak artırın, bu bağlantının etkinliği önceki aktivasyona (girdi sinyaline) bağlıdır.

---

## 3. Bias için Türev

* Bias $b$ için “3) adım” şöyle değişir:
  $\displaystyle \frac{\partial z}{\partial b} = 1$
* Yani

  $$
    \frac{\partial C}{\partial b}
    =
    \frac{\partial C}{\partial a}\;\times\;\frac{\partial a}{\partial z}\;\times\;1
  $$

---

## 4. Daha Büyük Ağlarda Ne Değişir?

* Gerçek bir ağda her katmanda onlarca nöron var, ama formül **aynı** kalır. Tek fark:

  * Bir önceki katmandaki her nöronun değişimi, **tüm** sonraki katmandaki nöronlara ayrı ayrı “zincir kuralı”yla yansıtılır ve **toplanır**.
* Bunun sonucu, her bir ağırlık için “o ağırlığın tüm yollar üzerinden maliyete etkisi” hesaplanmış olur.

---

## 5. Neden Önemli?

* Bu kısım, **backpropagation**’ın kalbi:

  * Maliyet fonksiyonunun en hızlı düştüğü yöne (negatif gradyana) adım atmamızı sağlar.
  * Böylelikle ağırlıkları en “etkili” şekilde güncelleriz.

---

### Özet Adımlar

1. **Forward Pass:** Hesapla $z$, sonra $a$, sonra $C$.
2. **Zincir Kuralı:**
   $\partial C/\partial w = (\partial C/\partial a)\times(\partial a/\partial z)\times(\partial z/\partial w)$.
3. **Tüm Ağırlıkları Güncelle:**

   $$
     w \gets w \;-\;\eta\;\frac{\partial C}{\partial w}
   $$

   ($\eta$ = öğrenme hızı)

Böylece **matematiksel olarak** backpropagation’ı “öğrenmiş” olursunuz – sonraki adım, bu formülleri kodunuza taşıyıp denemek!






