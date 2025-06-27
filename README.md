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


