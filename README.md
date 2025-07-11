Selamlar 🌷

* **benim bir başka serüvenim ile karşı karşıyasınız bu benim ilk stajım 04.07.2025 - 30.07.2025 tarihlerinde staj için yaptığım her şeyi dokümante ediyor olacağım...**
* **Apple Silicon Mac kullandığımı bilginize sunmak isterim çünkü bazı kurulum ve adımlar farklı olabilir.**

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

   * Kaynak: [Python & Design Patterns Playlist](https://www.youtube.com/playlist?list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc) 🎧
   * Amaç: Magic Methods, Decorator, Generator, OOP, Design Patterns öğren

---

##  1. Hafta :

* **Understanding Neural Network and Backpropagation Algorithm**

  * *(English)*

    1. [The Perceptron Explained](https://youtu.be/i1G7PXZMnSc?si=45-LrjEc2QzKhU2W)
    2. [But what is a neural network? | Deep learning chapter 1](https://youtu.be/aircAruvnKk?si=xkoGPEReRLA_UZ56)
    3. [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://youtu.be/IHZwWFHWa-w?si=ilfRwZx-0I8Fniu8)
    4. [Backpropagation, intuitively | Deep Learning Chapter 3](https://youtu.be/Ilg3gGewQ5U?si=uBw90JvWbqI09VZD)
  * *(Turkish)*

    1. [Neural Network 1 : Eğitime ve Kavramlara Giriş](https://youtu.be/B5MmXmMMuvI?si=JZ4Yfmc_MdsxPyhU)
    2. [Neural Network 2: Perceptron Kavramı ve Öğrenme](https://youtu.be/5Lo_HUDtxtw?si=DuZ1y9W11aRfIvrd)
    3. [Neural Network 3: Çok Katmanlı Yapay Sinir Ağları](https://youtu.be/qrmaixHBrzU?si=sXHsC0A5XaXsJZId)

* **Download Ollama and choosing model upon the RAM criteria**

  1. [Learn Ollama in 15 Minutes - Run LLM Models Locally for FREE](https://youtu.be/UtSSMs6ObqY?si=xF7yTc1MQEP1tGZh)
  2. [Design Your Own Ollama Model Now!](https://youtu.be/bXf2Cxf3Wk0?si=kwTZ9U8uJjZ1VqZE)

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

### 2.0 Magic Methods (Dunder Metotlar)

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

### 3.0 Decorator’lar

Fonksiyonların girişine/çıkışına dinamik davranış eklemeye yarar.

#### 3.1 Temel Decorator

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

#### 3.2 Parametreli Decorator

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

#### 4.0 Tasarım Desenleri (Design Patterns)

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

#### 5.0 ⚙️ Generator’lar

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

#### 6.0 Komut Satırı Argümanları

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

#### 7.0 Kapsülleme & Veri Gizleme

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

#### 8.0 Type Hinting

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

### 9.0 Detaylı Tasarım Desenleri

#### 9.1 Factory Pattern

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

# 🌐 Neural Network and Backpropagation Algorithm 🤖🧠


## 1. Nöron Nedir? ⚙️
- **Tanım:** Sayı tutan birimdir ve her nöron 0–1 arası bir aktivasyon değeri taşır.  
- **Giriş katmanı:** 784 nöron (28×28 piksellik her piksel için bir nöron)

## 2. Aktivasyon Nedir? 🌟
- **Tanım:** Pikselin gri ton değeridir (0 = siyah, 1 = beyaz).  
- **Anlamı:** Yüksek aktivasyon = o nöron “parlak” (aktiftir)

## 3. Problemin Tanımı 🧐
28×28 piksellik düşük çözünürlüklü el yazısı rakam görüntülerini (örneğin “3”) bilgisayarla otomatik tanımanın ne kadar zor olduğunu vurguluyor.  
> **İnsan Beyni–Bilgisayar Karşılaştırması:** İnsan görsel korteksi bu görevi zorlanmadan çözer; bilgisayarda ise “komik derecede” karmaşık hale gelir.

## 4. Öğrenme (Learning) Kavramı 🚀
Soyut bir şeyi somutlaştırmak sonucu gerçekleşir.  
**Amaç:** On binlerce parametrenin “doğru” değerlerini otomatik ve hızlı bir şekilde bulmak.


## 5. Soyutlama Düzeyleri 🏗️
- **Giriş Katmanı (Input Layer):** Ham pikseller. 784 nöron.  
- **Gizli Katmanlar (Hidden Layers):** Kenar, köşe, döngü gibi alt-bileşenler.  
  - Örnekte iki gizli katman, her biri 16 nöron.  
- **Çıkış Katmanı (Output Layer):** Bileşen kombinasyonlarından rakam tanıması. 10 nöron (0–9).  

> **Genel Amaç:** Aynı yapı, farklı görüntü ve ses tanıma görevlerine de uyarlanabilir.

## 6. İleri Besleme Mekanizması 🔄
- Her gizli katmandaki nöron, önceki katmandaki tüm nöronların aktivasyonlarıyla “bağlantılıdır”.  
- **Ağırlık (weight):** Sinyallerin gücünü belirler.  
- **Bias:** Nöronun “ne zaman” aktif olacağını kontrol eden eşik ayarı.  

> Eğitim aşamasında bias ve weight parametreleri gradient descent ile otomatik olarak ayarlanır.

## 7. Parametre Hesabı 📊
- Her katman atlaması için *önceki katmandaki nöron sayısı* × *sonraki katmandaki nöron sayısı* kadar bağlantı (weight).  
- **Aktivasyon fonksiyonu:** Toplam sonucu 0–1 aralığına sıkıştırmak (sigmoid veya ReLU).  
- **Toplam parametre sayısı:** weight sayısı + bias sayısı.  

| Geçiş                          | Önceki katman | Sonraki katman | Ağırlık Matrisi Boyutu | Ağırlık sayısı   | Bias sayısı | Parametre | Bias vektörü boyutu | Ara Toplam |
| ------------------------------ | ------------- | -------------- | ---------------------- | ---------------- | ----------- | --------- | ------------------- | ---------- |
| Giriş → 1. Gizli katman        | 784 nöron     | 16 nöron       | (16, 784)              | 784 × 16 = 12 544 | 16          | 12 560    | (16, 1)             | 12 560     |
| 1. Gizli katman → 2. Gizli katman | 16 nöron  | 16 nöron       | (16, 16)               | 16 × 16 = 256     | 16          | 272       | (16, 1)             | 272        |
| 2. Gizli katman → Çıkış        | 16 nöron      | 10 nöron       | (10, 16)               | 16 × 10 = 160     | 10          | 170       | (10, 1)             | 170        |
| **Genel Toplam**               |               |                |                        | **12 960**        | **42**      | **13 002**|                     | **13 002** |


## 8. Backpropagation’ın Amacı 🎯
- **Amaç:** Hangi ağırlık, hatayı ne kadar etkiliyor?  
- **Hedef:** Modelin tahmin hatasını (maliyeti) en aza indirmek.  
> **Özet:** Tahmin → Hata → Gradyan → Güncelleme


## 9. Adım Adım İşleyiş 🚶‍♀️
| Adım | Ne Yapıyoruz?                                                                                 |
| ---- | --------------------------------------------------------------------------------------------- |
| 1    | **Tahmin (Forward Pass):** Girdiyi ağdan geçirip çıktı değerini hesaplıyoruz.                  |
| 2    | **Hata Hesaplama (Loss):** Tahmin ile gerçek etiket arasındaki farkı ölçüyoruz (örn. kare fark). |
| 3    | **Geri Yayılım (Backprop):** Hatanın her ağırlığa ne kadar etki ettiğini belirliyoruz.         |
| 4    | **Ağırlık Güncelleme:** Ağırlıkları, hatayı azaltacak yönde küçük adımlarla güncelliyoruz.      |

## 10. Basit Örnek Görseliyle 🖼️
- **Girdi:** `[x₁, x₂]`  
- **Ağırlıklar:** `[w₁, w₂]`, **Bias:** `b`  
- **Hesap:** `z = w₁·x₁ + w₂·x₂ + b` → `a = sigmoid(z)`  
- **Hata:** `(a − y)²` (`y` = gerçek etiket)  
- **Geri Yayılım:** Hangi `w₁` veya `w₂` değişirse hata ne kadar değişir?  
- **Güncelleme:** `w ← w − η·(etki)` (`η` = öğrenme hızı)

## 11. Döngüyü Tekrarlama 🔁
Her veri noktası veya mini-batch için:  
1. Tahmin  
2. Hata Hesaplama  
3. Geri Yayılım  
4. Ağırlık Güncelleme  

> Bu dört adım tekrarlanarak ağ “öğrenir” ve tahmin doğruluğu artar.

---

## 📚 Ek Kaynaklar
- **Ian Goodfellow, Yoshua Bengio & Aaron Courville** – *Deep Learning* (MIT Press, 2016)  
  Resmî web sitesi ve PDF: https://www.deeplearningbook.org/  
- **Michael Nielsen** – *Neural Networks and Deep Learning* (online kitap, 2015)  
  Etkileşimli alıştırmalar: https://neuralnetworksanddeeplearning.com/  
- **Stanford CS231n** – *Convolutional Neural Networks for Visual Recognition*  
  Ders notları: http://cs231n.stanford.edu/  
  Video dersleri: https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv  


----

## 🌐 Fundamental of Network:
[Kullanılan Kitap Linki 📘](https://drive.google.com/file/d/1RzrRfISQd7i8XpL0zkMRHvKRFqIOs7df/view?usp=drive_link)  
and My Notes :

### 🧱 **OSI MODEL**
**P**LEASE **D**O **N**OT **T**HROW THE **S**OUSAGE **P**İZZA **A**WAY  

<details>
<summary> as Table</summary>

<br>

| Katman No | Katman Adı      | Açıklama                                                                 | Örnek Donanım / Protokoller         |
|-----------|------------------|--------------------------------------------------------------------------|-------------------------------------|
| 1️⃣        | **Physical**     | Bit seviyesinde iletim; elektriksel ve fiziksel özellikler               | 🧱 Hub, Kablo, Voltaj, Bit           |
| 2️⃣        | **Data Link**    | Frame oluşturma, MAC adresleme ve hata denetimi                         | 🧠 Switch, MAC, Ethernet             |
| 3️⃣        | **Network**      | IP adresleme, yönlendirme ve paketleme                                  | 🧭 Router, IP, ICMP                  |
| 4️⃣        | **Transport**    | Uçtan uca iletişim, veri aktarım kontrolü                               | 📡 TCP, UDP, Port Numaraları         |
| 5️⃣        | **Session**      | Oturum açma ve senkronizasyon                                           | 🗂️ Oturum Yönetimi, RPC, NetBIOS     |
| 6️⃣        | **Presentation** | Verinin sunumu, şifreleme, biçim dönüşümleri                            | 🔐 JPEG, MP3, SSL/TLS, ASCII         |
| 7️⃣        | **Application**  | Kullanıcının doğrudan etkileştiği katman                               | 🌍 HTTP, FTP, SMTP, GitHub API       |

</details>

📦 1->3 : Media Layer  💻 4->7 : Host Layer  
1. **Physical** ⚡️: bits, hub  
2. **Data Link** 🔗: switcher, frames, MAC address  
3. **Network** 🌍: router, packages, IP address  
4. **Transport** 🚚:
   - **TCP** 🔵:
     - ✅ %100 all bits delivered  
     - 📥 make sure if it's received  
     - 🤝 3 way handshake : SYN ➝ SYN-ACK ➝ ACK
     
   - **UDP** 🔴:
     - 📞 phone call  
     - ⏱️ real time  
     - ❓ not sure if all bits received  
5. **Session** 🗂️:
   - 🧠 Logical Parts  
   - 🔁 Synchronization and send to ports  
6. **Presentation** 🎭:
   - 🔐 connect the data to decrypt or encrypt (if it's needed)  
   - 🧬 syntax layer  
7. **Application** 🧑‍💻:
   - 🧾 End the user layer  
   - 🔚 Deal with last protocol  
---



Curriculum (Each lecture ~25 mins)
Module 0: Introduction & Environment Setup
• Lesson 0.1 — Welcome to the LLM Revolution
• Course goals, what we will build
• Why learn LLMs from scratch?
• Open-source vs closed-source models (GPT-4 vs LLaMA 3)
• Lesson 0.2 - Core Concepts: Autoregression, Transformers, Pretraining vs Fine-tuning
• Lesson 0.3 - Setting Up Your Deep Learning Environment
• Python, PyTorch, datasets, tiktoken, transformers
• GPU on Colab / Kaggle
Module 1: Data - The Fuel for LLMs
• Lesson 1.1 - Understanding Text & The Role of Tokenization
• Words, subwords, characters
• BPE explained
• Lesson 1.2 — Practical Tokenization with tiktoken
• Encoding/decoding tokens
• Vocabulary size, special tokens


https://github.com/pyenv/pyenv?tab=readme-ov-file#homebrew-in-macos : 
MacOS
Details
The options from the Linux section above also work but Homebrew is recommended for basic usage.

Homebrew in macOS
Update homebrew and install pyenv:

brew update
brew install pyenv
If you want to install (and update to) the latest development head of Pyenv rather than the latest release, instead run:

brew install pyenv --head
Then follow the rest of the post-installation steps, starting with Set up your shell environment for Pyenv.

OPTIONAL. To fix brew doctor's warning ""config" scripts exist outside your system or Homebrew directories"

If you're going to build Homebrew formulae from source that link against Python like Tkinter or NumPy (This is only generally the case if you are a developer of such a formula, or if you have an EOL version of MacOS for which prebuilt bottles are no longer provided and you are using such a formula).

To avoid them accidentally linking against a Pyenv-provided Python, add the following line into your interactive shell's configuration:

Bash/Zsh:

alias brew='env PATH="${PATH//$(pyenv root)\/shims:/}" brew'
Fish:

alias brew="env PATH=(string replace (pyenv root)/shims '' \"\$PATH\") brew"





