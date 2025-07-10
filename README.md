Selamlar 🌷

* **benim bir başka serüvenim ile karşı karşıyasınız bu benim ilk stajım 04.07.2025 - 30.07.2025 tarihlerinde staj için yaptığım her şeyi dekomente ediyor olacağım...**
* **Apple Silicon Mac kullandığımı unutmayın; bazı kurulum ve adımlar farklı olabilir.**

## 📝 Ön Kabul Görevleri

1. **Geliştirme Ortamı Kurulumu (VirtualBox + Debian ARM64)**

   * **Adım 1:** VirtualBox indirme ve kurulum

     ```bash
     # https://www.virtualbox.org adresinden macOS sürümünü indirip kurun.
     ```

     > **Açıklama:** VirtualBox, Apple Silicon destekli ön sürümleriyle ARM64 tabanlı VM oluşturmanızı sağlar.
   * **Adım 2:** Debian ARM64 ISO hazırlama

     ```bash
     # Debian ARM64 ISO dosyasını https://www.debian.org/ARM64 adresinden indirin.
     ```

     > **Açıklama:** ARM64 dağıtımı, M3 çiple uyumlu çalışır.
   * **Adım 3:** Yeni VM oluşturma ve ayarlar

     | Öğe             | Değer                       |
     | --------------- | --------------------------- |
     | İşletim Sistemi | Debian (Linux / ARM 64-bit) |
     | Bellek (RAM)    | 4 GB veya üstü              |
     | Depolama        | 20 GB VDI                   |
     | Ağ Adaptörü     | NAT                         |

     > **Açıklama:** Bellek ve depolama, derleme süreçleri için yeterli olmalıdır.
   * SSH: `openssh-server` kurup, `ssh kullanıcı@<VM_IP>` ile bağlan

2. **E‑Ticaret Sitesi (Odoo Tabanlı)**

   * **Platform:** Odoo E‑commerce modülü ile hızlı ve ölçeklenebilir geliştirme
   * **Ürün Kataloğu:** Printed Mug, Printed T‑Shirt, Printed Bag (kullanıcı tasarımıyla baskıya hazır)
   * **Sipariş Akışı:**

     1. Kullanıcı tasarım yükler veya seçim yapar
     2. Bizim önerilerimizle onaylanan tasarım baskıya gönderilir
     3. Hazır ürün paketlenip müşteriye kargo ile ulaştırılır
   * **Logo Tasarımı:**

     * Basit, akılda kalıcı logo oluşturma
     * SVG ve PNG formatlarında optimizasyon
   * **Teknik Entegrasyon:**

     * Odoo modülleri: `website_sale`, `website_blog`, `payment_stripe` gibi
     * Git ile sürüm kontrol, CI/CD pipeline (ör. GitHub Actions)

3. **Odoo Addon Geliştirme**

   * `odoo_addons/my_module` dizini oluştur
   * `__manifest__.py`, `models/`, `views/` dosyalarını ekle
   * Sanal ortam, `pip install -r requirements.txt`, `./odoo-bin` ile başlat

4. **Python & Tasarım Desenleri**

   * Kaynak: [Python & Design Patterns Playlist](https://www.youtube.com/playlist?list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc)
   * Amaç: Magic Methods, Decorator, Generator, OOP, Design Patterns öğren

---

##  1. Hafta :

* **Understanding Neural Network and Backpropagation Algorithm**

  * *(English)*

    1. [https://youtu.be/i1G7PXZMnSc?si=45-LrjEc2QzKhU2W](https://youtu.be/i1G7PXZMnSc?si=45-LrjEc2QzKhU2W)
    2. [https://youtu.be/aircAruvnKk?si=xkoGPEReRLA\_UZ56](https://youtu.be/aircAruvnKk?si=xkoGPEReRLA_UZ56)
    3. [https://youtu.be/IHZwWFHWa-w?si=ilfRwZx-0I8Fniu8](https://youtu.be/IHZwWFHWa-w?si=ilfRwZx-0I8Fniu8)
    4. [https://youtu.be/Ilg3gGewQ5U?si=uBw90JvWbqI09VZD](https://youtu.be/Ilg3gGewQ5U?si=uBw90JvWbqI09VZD)
  * *(Turkish)*

    1. [https://youtu.be/B5MmXmMMuvI?si=JZ4Yfmc\_MdsxPyhU](https://youtu.be/B5MmXmMMuvI?si=JZ4Yfmc_MdsxPyhU)
    2. [https://youtu.be/5Lo\_HUDtxtw?si=DuZ1y9W11aRfIvrd](https://youtu.be/5Lo_HUDtxtw?si=DuZ1y9W11aRfIvrd)
    3. [https://youtu.be/qrmaixHBrzU?si=sXHsC0A5XaXsJZId](https://youtu.be/qrmaixHBrzU?si=sXHsC0A5XaXsJZId)

* **Download Ollama and choosing model upon the RAM criteria**

  1. [https://youtu.be/UtSSMs6ObqY?si=xF7yTc1MQEP1tGZh](https://youtu.be/UtSSMs6ObqY?si=xF7yTc1MQEP1tGZh)
  2. [https://youtu.be/bXf2Cxf3Wk0?si=kwTZ9U8uJjZ1VqZE](https://youtu.be/bXf2Cxf3Wk0?si=kwTZ9U8uJjZ1VqZE)

  ```
  bash
  ```

  CopyEdit

  `ollama run deepseek-r1:8b`

* **Searching about LLM libraries & learning how to customize LLM especially by using Ollama**

  1. [https://github.com/malibayram/llm-from-scratch](https://github.com/malibayram/llm-from-scratch)
  2. [https://www.udemy.com/course/sifirdan-llm-gelistirme-kendi-dil-modelini-olustur/?couponCode=LOCLZDOFFPTRCTRL](https://www.udemy.com/course/sifirdan-llm-gelistirme-kendi-dil-modelini-olustur/?couponCode=LOCLZDOFFPTRCTRL)

* **Downloaded model:**

  `https://ollama.com/library/deepseek-r1 ollama run deepseek-r1:8b`

* **Additional libraries mentioned by the instructor:**

  * [ModelScope](https://github.com/modelscope/modelscope)

  * [Unsloth](https://github.com/unslothai/unsloth) ( JAX tabanlı dataset loader ) 

  * [Hugging Face](https://huggingface.co/) (Transformers)

* Ollama CLI:

  ```bash
  ollama pull deepseek-r1:8b
  ollama run deepseek-r1:8b --context 2048
  ollama fine-tune deepseek-r1:8b --dataset ./data/my_prompts.jsonl --output custom-deepseek
  ```

## 🐍 Python Kavramları (2.0–9.0) (2.0–9.0) Python Kavramları (2.0–9.0)

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
> 2. `__add__` – `v1 + v2` işlemi çağrıldığında devreye girer, yeni `Vector` nesnesi üretir.
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

## 5.0 ⚙️ Generator’lar

Bellek kullanımını minimuma indirerek "lazy evaluation" sağlar. Normal `return` yerine `yield` kullanır.

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
> * `next()` ile bir sonraki `yield`'e kadar ilerler, tembel değerlendirme yapılır.

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

---

## 🛠️ Odoo on Debian (Manual Kurulum)

**Detaylı Adımlar:**

1. Sistem Güncelleme ve Bağımlılıklar

```bash
sudo apt update && sudo apt upgrade -y
sudo timedatectl set-timezone Europe/Istanbul
sudo apt install git python3.10 python3.10-venv python3-pip build-essential wget libpq-dev libxml2-dev libxslt1-dev libjpeg-dev libblas-dev libatlas-base-dev -y
```

2. Odoo Kullanıcısı & PostgreSQL

```bash
sudo useradd -r -s /bin/bash -m -d /opt/odoo odoo
sudo -u postgres createuser --createdb --username postgres odoo
```

3. Kaynak Kodunun İndirilmesi

```bash
sudo -u odoo git clone --depth 1 --branch 16.0 https://github.com/odoo/odoo.git /opt/odoo/odoo
```

4. Python Sanal Ortamı & Gereksinimler

```bash
sudo -u odoo python3.10 -m venv /opt/odoo/venv
source /opt/odoo/venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r /opt/odoo/odoo/requirements.txt
deactivate
```

5. Konfigürasyon Dosyası (/etc/odoo.conf)

```ini
[options]
db_user = odoo
db_password = odoo
addons_path = /opt/odoo/odoo/addons
admin_passwd = YourStrongAdminPassword
xmlrpc_port = 8069
logfile = /var/log/odoo/odoo.log
```

```bash
sudo chown odoo: /etc/odoo.conf
sudo chmod 640 /etc/odoo.conf
```

6. Log & Veri Klasörleri

```bash
sudo mkdir -p /var/log/odoo /var/lib/odoo
sudo chown -R odoo: /var/log/odoo /var/lib/odoo
```

7. Systemd Servis

```ini
[Unit]
Description=Odoo16 Service
After=network.target postgresql.service

[Service]
Type=simple
User=odoo
Group=odoo
ExecStart=/opt/odoo/venv/bin/python3 /opt/odoo/odoo/odoo-bin -c /etc/odoo.conf
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

```bash
sudo tee /etc/systemd/system/odoo.service > /dev/null <<EOF
[Unit]
Description=Odoo16 Service
After=network.target postgresql.service

[Service]
Type=simple
User=odoo
Group=odoo
ExecStart=/opt/odoo/venv/bin/python3 /opt/odoo/odoo/odoo-bin -c /etc/odoo.conf
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable odoo.service
sudo systemctl start odoo.service
```

8. Güvenlik Duvarı

```bash
sudo ufw allow 8069/tcp
```

---

## 🔑 SSH & VS Code Remote

**Detaylı Adımlar:**

1. Debian VM Üzerinde SSH Sunucusu

```bash
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable --now ssh
```

2. SSH Anahtar Çifti Oluşturma (macOS)

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ''
```

3. Anahtarın VM’e Kopyalanması

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub odoo@<VM_IP>
```

4. SSH Konfigürasyonu (macOS \~/.ssh/config)

```ini
Host debian-odoo
  HostName <VM_IP>
  User odoo
  IdentityFile ~/.ssh/id_ed25519
  ServerAliveInterval 60
  ControlMaster auto
  ControlPath ~/.ssh/cm-%r@%h:%p
```

5. Bağlantıyı Test Etme

```bash
ssh debian-odoo -v
```

6. Port Yönlendirme (Tunnel)

```bash
ssh -L 8069:localhost:8069 debian-odoo
```

7. VS Code Remote - SSH

8. VS Code eklentisini yükle: Remote - SSH

9. F1 > Remote-SSH: Add New SSH Host > debian-odoo

10. Remote Explorer’dan debian-odoo’ya bağlan

11. /opt/odoo dizinini aç

12. Ek İpuçları

* Agent Forwarding: ForwardAgent yes
* Multiplexing: ControlPersist 600

---

## 🔄 Backpropagation Detaylı İncelemesi

### 1. Ön Hazırlık: Sinir Ağı Nasıl Çalışır?

* **Nöron:** Basit bir hesap birimi; girdileri ağırlıklarla çarpar, toplar ve bir aktivasyon fonksiyonundan geçirir.
* **Katmanlar:** Giriş, gizli ve çıkış katmanları. Her katman bilgiyi bir sonraki katmana aktarır.

### 2. Backpropagation’ın Amacı

* Ağırlıkları nasıl ayarlayacağımızı bulmak: Hangi ağırlık, hatayı ne kadar etkiliyor?
* Amaç: Modelin tahmin hatasını (maliyeti) en aza indirmek.

### 3. Adım Adım İşleyiş

| Adım                       | Ne Yapıyoruz?                                                         |
| -------------------------- | --------------------------------------------------------------------- |
| 1. Tahmin (Forward Pass)   | Girdiyi ağdan geçirip çıktı değerini hesaplıyoruz.                    |
| 2. Hata Hesaplama (Loss)   | Tahmin ile gerçek etiket arasındaki farkı ölçüyoruz (örn. kare fark). |
| 3. Geri Yayılım (Backprop) | Hatanın her ağırlığa ne kadar etki ettiğini belirliyoruz.             |
| 4. Ağırlık Güncelleme      | Ağırlıkları, hatayı azaltacak yönde küçük adımlarla güncelliyoruz.    |

### 4. Basit Örnek Görseliyle

1. **Girdi:** \[x₁, x₂]
2. **Ağırlıklar:** \[w₁, w₂], **Bias:** b
3. **Hesap:** z = w₁·x₁ + w₂·x₂ + b → **Aktivasyon:** a = sigmoid(z)
4. **Hata:** (a − y)² (y gerçek etiket)
5. **Geri Yayılım:** Hangi w₁ veya w₂ değişirse hata ne kadar değişir? Bu etkiyi hesapla.
6. **Güncelle:** w ← w − η·(etki) (η = öğrenme hızı)

### 5. Döngüyü Tekrarlama

Her veri noktası veya mini-batch için:

1. Tahmin
2. Hata Hesaplama
3. Geri Yayılım
4. Ağırlık Güncelleme

Bu dört adım tekrarlanarak ağ ‘öğrenir’ ve tahmin doğruluğu artar.

---

