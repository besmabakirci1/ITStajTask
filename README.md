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
   * SSH : `openssh-server` kurup, `ssh kullanıcı@<VM_IP>` ile bağlan
   * link :[https://chatgpt.com/share/685aa279-9c50-800e-aba7-1a678d55750b]
   * link : [https://chatgpt.com/c/686d5030-8cc4-800e-ae51-028f25d8afb6]

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
---

<details> 
  
**<summary> Design Pattern and Python: </summary>**

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

</details>

<details> 
  **<summary> 🛠️ Odoo on Debian (Manual Kurulum)</summary>**
  
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
</details>
<details> **<summary> 🔑 SSH & VS Code Remote </summary>**

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

</details>


# 🌐 Neural Network and Backpropagation Algorithm 🤖🧠
![Biyolojik ve Yapay Nöron](https://github.com/user-attachments/assets/17b7f50a-632a-480e-9968-2de823137be0)
- <caption><b>Şekil 1.</b> Sol: İnsan beynindeki biyolojik nöron yapısı. Sağ: Benzer işlevleri taklit eden yapay sinir ağı mimarisi.</caption>

![Biyolojik ve Yapay Nöron](https://github.com/user-attachments/assets/8bf57052-03b2-46e5-9918-24f403e1ac0b)
- <caption><b>Şekil 2.</b> (a) Biyolojik nöronun yapısı, (b) Yapay nöronun matematiksel modeli, (c) Çok katmanlı yapay sinir ağı.</caption>

### 1. Nöron Nedir? ⚙️
- **Tanım:** Sayı tutan birimdir ve her nöron 0–1 arası bir aktivasyon değeri taşır.  
- **Giriş katmanı:** 784 nöron (28×28 piksellik her piksel için bir nöron)

### 2. Aktivasyon Nedir? 🌟
- **Tanım:** Pikselin gri ton değeridir (0 = siyah, 1 = beyaz).  
- **Anlamı:** Yüksek aktivasyon = o nöron “parlak” (aktiftir)

### 3. Problemin Tanımı 🧐
28×28 piksellik düşük çözünürlüklü el yazısı rakam görüntülerini (örneğin “3”) bilgisayarla otomatik tanımanın ne kadar zor olduğunu vurguluyor.  
> **İnsan Beyni–Bilgisayar Karşılaştırması:** İnsan görsel korteksi bu görevi zorlanmadan çözer; bilgisayarda ise “komik derecede” karmaşık hale gelir.

### 4. Öğrenme (Learning) Kavramı 🚀
Soyut bir şeyi somutlaştırmak sonucu gerçekleşir.  
**Amaç:** On binlerce parametrenin “doğru” değerlerini otomatik ve hızlı bir şekilde bulmak.


### 5. Soyutlama Düzeyleri 🏗️
- **Giriş Katmanı (Input Layer):** Ham pikseller. 784 nöron.  
- **Gizli Katmanlar (Hidden Layers):** Kenar, köşe, döngü gibi alt-bileşenler.  
  - Örnekte iki gizli katman, her biri 16 nöron.  
- **Çıkış Katmanı (Output Layer):** Bileşen kombinasyonlarından rakam tanıması. 10 nöron (0–9).  

> **Genel Amaç:** Aynı yapı, farklı görüntü ve ses tanıma görevlerine de uyarlanabilir.

### 6. İleri Besleme Mekanizması 🔄
- Her gizli katmandaki nöron, önceki katmandaki tüm nöronların aktivasyonlarıyla “bağlantılıdır”.  
- **Ağırlık (weight):** Sinyallerin gücünü belirler.  
- **Bias:** Nöronun “ne zaman” aktif olacağını kontrol eden eşik ayarı.  

> Eğitim aşamasında bias ve weight parametreleri gradient descent ile otomatik olarak ayarlanır.

### 7. Parametre Hesabı 📊
- Her katman atlaması için *önceki katmandaki nöron sayısı* × *sonraki katmandaki nöron sayısı* kadar bağlantı (weight).  
- **Aktivasyon fonksiyonu:** Toplam sonucu 0–1 aralığına sıkıştırmak (sigmoid veya ReLU).  
- **Toplam parametre sayısı:** weight sayısı + bias sayısı.  

| Geçiş                          | Önceki katman | Sonraki katman | Ağırlık Matrisi Boyutu | Ağırlık sayısı   | Bias sayısı | Parametre | Bias vektörü boyutu | Ara Toplam |
| ------------------------------ | ------------- | -------------- | ---------------------- | ---------------- | ----------- | --------- | ------------------- | ---------- |
| Giriş → 1. Gizli katman        | 784 nöron     | 16 nöron       | (16, 784)              | 784 × 16 = 12 544 | 16          | 12 560    | (16, 1)             | 12 560     |
| 1. Gizli katman → 2. Gizli katman | 16 nöron  | 16 nöron       | (16, 16)               | 16 × 16 = 256     | 16          | 272       | (16, 1)             | 272        |
| 2. Gizli katman → Çıkış        | 16 nöron      | 10 nöron       | (10, 16)               | 16 × 10 = 160     | 10          | 170       | (10, 1)             | 170        |
| **Genel Toplam**               |               |                |                        | **12 960**        | **42**      | **13 002**|                     | **13 002** |


### 8. Backpropagation’ın Amacı 🎯
- **Amaç:** Hangi ağırlık, hatayı ne kadar etkiliyor?  
- **Hedef:** Modelin tahmin hatasını (maliyeti) en aza indirmek.  
> **Özet:** Tahmin → Hata → Gradyan → Güncelleme

![Gradient Descent](https://github.com/user-attachments/assets/fc6ecc38-c3a6-4a49-ae62-0e28e6e3a4bf)
<caption><b>Şekil 1.</b> Gradyan yönünde (türev işareti boyunca) küçük adımlarla ağırlıkların güncellenmesi ve maliyetin (cost) en aza indirilmesi.</caption>

### 9. Adım Adım İşleyiş 🚶‍♀️
| Adım | Ne Yapıyoruz?                                                                                 |
| ---- | --------------------------------------------------------------------------------------------- |
| 1    | **Tahmin (Forward Pass):** Girdiyi ağdan geçirip çıktı değerini hesaplıyoruz.                  |
| 2    | **Hata Hesaplama (Loss):** Tahmin ile gerçek etiket arasındaki farkı ölçüyoruz (örn. kare fark). |
| 3    | **Geri Yayılım (Backprop):** Hatanın her ağırlığa ne kadar etki ettiğini belirliyoruz.         |
| 4    | **Ağırlık Güncelleme:** Ağırlıkları, hatayı azaltacak yönde küçük adımlarla güncelliyoruz.      |

### 10. Basit Örnek Görseliyle 🖼️
- **Girdi:** `[x₁, x₂]`  
- **Ağırlıklar:** `[w₁, w₂]`, **Bias:** `b`  
- **Hesap:** `z = w₁·x₁ + w₂·x₂ + b` → `a = sigmoid(z)`  
- **Hata:** `(a − y)²` (`y` = gerçek etiket)  
- **Geri Yayılım:** Hangi `w₁` veya `w₂` değişirse hata ne kadar değişir?  
- **Güncelleme:** `w ← w − η·(etki)` (`η` = öğrenme hızı)

### 11. Döngüyü Tekrarlama 🔁
Her veri noktası veya mini-batch için:  
1. Tahmin  
2. Hata Hesaplama  
3. Geri Yayılım  
4. Ağırlık Güncelleme  

> Bu dört adım tekrarlanarak ağ “öğrenir” ve tahmin doğruluğu artar.


![Loss Landscape](https://github.com/user-attachments/assets/444665a0-637e-4487-b34c-ff7d31048697)
<caption><b>Şekil 2.</b> Çok boyutlu kayıp yüzeyinde (loss landscape) optimizasyonun izlediği yol; yerel minimumlar, eyer noktaları ve zor bölgeler.</caption>



#### 📚 Ek Kaynaklar
- **Ian Goodfellow, Yoshua Bengio & Aaron Courville** – *Deep Learning* (MIT Press, 2016)  
  Resmî web sitesi ve PDF: https://www.deeplearningbook.org/  
- **Michael Nielsen** – *Neural Networks and Deep Learning* (online kitap, 2015)  
  Etkileşimli alıştırmalar: https://neuralnetworksanddeeplearning.com/  
- **Stanford CS231n** – *Convolutional Neural Networks for Visual Recognition*  
  Ders notları: http://cs231n.stanford.edu/  
  Video dersleri: https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv  


## 🌐 Fundamental of Network:

### [The Book That We Used 📘](https://drive.google.com/file/d/1RzrRfISQd7i8XpL0zkMRHvKRFqIOs7df/view?usp=drive_link)  & My Notes :

### 🧱 **OSI MODEL**
**P**LEASE **D**O **N**OT **T**HROW THE **S**OUSAGE **P**İZZA **A**WAY  

<details>
**<summary> as Table</summary> **

| Katman No | Katman Adı      | Açıklama                                                                 | Örnek Donanım / Protokoller         |
|-----------|------------------|--------------------------------------------------------------------------|-------------------------------------|
| 1️⃣        | **Physical**     | Bit seviyesinde iletim; elektriksel ve fiziksel özellikler               | 🧱 Hub, Kablo, Voltaj, Bit           |
| 2️⃣        | **Data Link**    | Frame oluşturma, MAC adresleme ve hata denetimi                         | 🧠 Switch, MAC, Ethernet             |
| 3️⃣        | **Network**      | IP adresleme, yönlendirme ve paketleme                                  | 🧭 Router, IP, ICMP                  |
| 4️⃣        | **Transport**    | Uçtan uca iletişim, veri aktarım kontrolü                               | 📡 TCP, UDP, Port Numaraları         |
| 5️⃣        | **Session**      | Oturum açma ve senkronizasyon                                           | 🗂️ Oturum Yönetimi, RPC, NetBIOS     |
| 6️⃣        | **Presentation** | Verinin sunumu, şifreleme, biçim dönüşümleri                            | 🔐 JPEG, MP3, SSL/TLS, ASCII         |
| 7️⃣        | **Application**  | Kullanıcının doğrudan etkileştiği katman                                | 🌍 HTTP, FTP, SMTP, GitHub API       |

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

### İnternet Gerçekte Nasıl Çalışır?

[Video](https://www.youtube.com/watch?v=GIvU5pDrT1o) 

İnternete bağlanmak, istemci (client) cihazdan başlayan ve uçtan uca bir ağ altyapısını tetikleyen, çok katmanlı bir iletişim sürecidir. Kullanıcı bir istekte bulunduğunda (örneğin YouTube'da bir videoya tıklamak), bu istek IP paketlerine bölünerek DNS sunucusu üzerinden hedef sunucunun IP adresi çözülür ve rotalanır. Veriler, genellikle yüksek performanslı SSD’lerle donatılmış, redundant sistemlere sahip veri merkezlerinde saklanır. Bu veriler, dünya genelini saran denizaltı fiber optik kablolar üzerinden, ışık sinyalleri şeklinde minimum gecikmeyle iletilir. Fiber hatlardan çıkan optik sinyaller, modemlerde elektriksel sinyale dönüştürülerek WiFi veya baz istasyonları üzerinden son kullanıcıya ulaşır. IP yönlendirme, paket sıralaması ve hata kontrolü ise TCP/IP başta olmak üzere çeşitli ağ protokolleri tarafından sağlanır. Her veri paketi, hedefe farklı yollardan ulaşabilir ve istemci tarafında yeniden birleştirilerek içerik oluşturulur. Bu sistem, ICANN gibi küresel otoriteler tarafından yönetilen bir adresleme ve protokol standardizasyonu ile işler; yani bir video akışı, aslında ışık hızında hareket eden binlerce paketin, onlarca protokol ve altyapı katmanıyla senkronize şekilde taşınmasıdır.


---

### 🚀 Customize LLM 

Curriculum :
- Module 0: Introduction & Environment Setup
  * Lesson 0.1 — Welcome to the LLM Revolution
  *  Course goals, what we will build
  * Why learn LLMs from scratch?
  * Open-source vs closed-source models (GPT-4 vs LLaMA 3)
  * Lesson 0.2 - Core Concepts: Autoregression, Transformers, Pretraining vs Fine-tuning
  * Lesson 0.3 - Setting Up Your Deep Learning Environment
  * Python, PyTorch, datasets, tiktoken, transformers
  * GPU on Colab / Kaggle
- Module 1: Data - The Fuel for LLMs
  *  Lesson 1.1 - Understanding Text & The Role of Tokenization
  *  Words, subwords, characters
  *  BPE explained
  *  Lesson 1.2 — Practical Tokenization with tiktoken
  *  Encoding/decoding tokens
  *  Vocabulary size, special tokens

````markdown

# 🚀 macOS İçin Pyenv Kurulumu

> **Öneri:** Homebrew, macOS’ta pyenv’in temel kullanımını kolaylaştırır.

## 🛠️ 1. Homebrew Güncelleme ve Pyenv Kurulumu

```bash
# Homebrew’ü günceller
brew update

# Pyenv’i yükler
brew install pyenv
````

##### 🔭 2. Geliştirme Başına (Development Head) Pyenv Kurulumu *(Opsiyonel)*

```bash
# En son geliştirme sürümünü kurar
brew install pyenv --head
```

##### 🔧 3. Kabuk Ortamını Ayarlama

```bash
# Aşağıdaki satırları ~/.bashrc veya ~/.zshrc dosyanıza ekleyin
if command -v pyenv 1>/dev/null 2>&1; then
  # login shell için
  eval "$(pyenv init --path)"
  # interactive shell için
  eval "$(pyenv init -)"
fi
```


##### 🛡️ 4. `brew doctor` Uyarısını Giderme *(Opsiyonel)*

> Bazı formüller Python’a link ederken yanlışlıkla pyenv tarafından sağlanan sürümü kullanırsa uyarı alırsınız.

* **Bash/Zsh için:**

```
      alias brew='env PATH="${PATH//$(pyenv root)\/shims:/}" brew'
```

* **Fish için:**

  ```
      alias brew="env PATH=(string replace (pyenv root)/shims '' \"$PATH\") brew"
  ```

> **Kaynak:**
> [pyenv · GitHub – Homebrew in macOS](https://github.com/pyenv/pyenv?tab=readme-ov-file#homebrew-in-macos)

---

## Macte Ollama, Cpu ve Gpu arasındaki bağlantıyı anlamak : 
> Apple Silicon (M1/M2/M3) üzerinde NVIDIA’ya özgü nvtop veya top -o gpu gibi araçlar çalışmadığı için GPU kullanımını CLI’dan izlemek için :
#### 1. GUI: Activity Monitor – GPU History

1. **Activity Monitor**’ü açın (`Finder` → `Applications` → `Utilities` → **Activity Monitor**).
2. Menüden **Window** → **GPU History** seçeneğini seçin.
3. Burada entegre GPU’nuzun anlık yükünü grafiksel olarak görebilirsiniz.

> Açıklama: En hızlı ve en dolaysız yöntemdir; root izni veya ekstra kurulum gerekmez.

#### 2. CLI: `powermetrics` ile Tek Seferlik Anlık Ölçüm

Terminal’den aşağıdaki komut, 0.5 saniyelik bir örnekleme ile GPU “active residency” (yani GPU’nun ne oranda meşgul olduğuna) dair tek seferlik bir anlık görüntü çıkarır:

```sudo powermetrics --samplers gpu_power -i500 -n1 \ | grep "GPU active residency"```

> Açıklama adım adım:
> 
> - `sudo`: root izni, çünkü `powermetrics` sistem seviyesinde çalışır.
> - `-samplers gpu_power`: yalnızca GPU güç kullanım istatistiklerini toplar.
> - `i500`: 500 ms (0.5 s) örnekleme aralığı.
> - `n1`: tek örnek alıp komuttan çıkar.
> - `grep "GPU active residency"`: yalnızca yüzde değeri içeren satırı filtreler. ([Stack Overflow](https://stackoverflow.com/questions/63881791/macos-get-gpu-history-usage-from-terminal?utm_source=chatgpt.com), [OS X Daily](https://osxdaily.com/2024/07/05/how-to-see-individual-core-cpu-usage-on-mac-with-powermetrics/?utm_source=chatgpt.com))


#### 3. CLI: `asitop` ile Canlı Terminal Arayüzü

`asitop`, `powermetrics`’i arka planda kullanarak renkli, sürekli güncellenen bir terminal arayüzü sunar.

##### 1. **PATH** sorununuzu çözmek için (eğer hâlâ `command not found` alıyorsanız):
    
 ```
    echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
 ```
    
##### 2. Ardından çalıştırın:
    
  ```
    sudo asitop
   ```
    

> Açıklama:
> - `asitop`, CPU (“E-cluster”/“P-cluster”), GPU (entegre), ANE (Apple Neural Engine) ve bellek kullanımını ayrı sütunlarda gösterir.
> - Sürekli güncelleme ve grafiksel çubuklar sayesinde takip etmesi kolaydır. ([GitHub](https://github.com/tlkh/asitop?utm_source=chatgpt.com))


### Terminale **top -o cpu** yazarak CPU hareketlerini görebilirsiniz.



NOT : YUKARIYA nöroloji sinaps fln fotoğrafı eklenmeli .. murat hocanın dediğini hatırla ..

---





## 📚 LLM’in Temel Unsurları

1. **Veri Kümesinin Hacmi**  
   - Modelin “öğreneceği” örnek sayısı; genellikle milyarlarca token.  
2. **Transformer Mimarisi**  
   - Modelin katman yapısı, dikkat (attention) mekanizmaları, besleme (feed‑forward) blokları.

---

## 📚 Transformer Mimarisi

Transformer, tüm cümleye aynı anda bakar ve kelimeler arasındaki bağları “attention” ile öğrenir.  
Daha detaylı bilgi biçin lütfen makaleyi inceleyin:  
[Vaswani et al., “Attention is All You Need”](https://github.com/user-attachments/files/21395756/NIPS-2017-attention-is-all-you-need-Paper.pdf)

![Transformer Şeması](https://github.com/user-attachments/assets/2df429b7-930b-407b-942e-33574005f8db)

---

## Temel Bileşenler

- **Tokenizasyon**  
  Ham metni, anlamlı parçalara ayırma işlemi.  
- **Embedding**  
  Token’ları vektörlere (sayı dizilerine) dönüştürme.  
- **Positional Encoding**  
  Token’ların pozisyon bilgilerini modele ekleme.  
- **Attention (Dikkat)**  
  Hangi token’ın hangi token’la ne kadar ilişkili olduğunu hesaplama.  
- **Katman (Layer)**  
  Bilgiyi derinleştiren, sırayla uygulanan bloklar.  
- **Feed‑Forward**  
  Her katmanda bilinçli öğrenmeyi pekiştiren tam bağlı (dense) ağ bloğu.  

—
<img width="2385" height="1179" alt="image" src="https://github.com/user-attachments/assets/4b88b1fc-542d-4769-9bb0-f5ac0b810163" />

## 💡 Tokenizasyon Nedir?
“Token is an integer that represents a character, or a short segment of characters…”
Ham metni, modelin “anlayabileceği” küçük parçalara (token) bölme işlemidir.  
Örnek:  
> “Merhaba dünya” → `[“Merhaba”, “dünya”]` veya `[“Mer”, “haba”, “dün”, “ya”]`

### Tipleri

#### 1. Word-Level Tokenization (Kelime Düzeyi)

```python
def word_level_tokenize(text):
    # Metni boşluklardan bölerek kelime dizisi döner
    return text.split()

print(word_level_tokenize("Merhaba dünya, bugün nasılsın?"))
# → ['Merhaba', 'dünya,', 'bugün', 'nasılsın?']
```

Açıklama:
Boşlukları ayırır.
Noktalama işaretleri ayrı token olarak kalabilir.
Basit ama nadir kelimelerde sözlük dışı (OOV) sorunu yaşanır.
2. Character-Level Tokenization (Karakter Düzeyi)
def character_level_tokenize(text):
    # Metni karakter bazlı listeye dönüştürür
    return list(text)

print(character_level_tokenize("Merhaba"))
# → ['M', 'e', 'r', 'h', 'a', 'b', 'a']

Açıklama:
Her harfi ayrı token olarak işler.
OOV sorunu yoktur ama sıralı anlam çıkarımı zorlaşır.
3. Subword Tokenization (Alt-Parça Düzeyi)
Kelimeyi, hem anlamlı hem de sık görülen parçalara böler.
Örnek: “bilinmeyen” → [“▁bil”, “in”, “me”, “yen”]
Avantaj:
Daha önce görülmemiş kelimelerle karşılaşıldığında parçalar üzerinden genel anlam tahmini yapılabilir.

Subword Tokenizasyon Algoritmaları
Byte‑Pair Encoding (BPE) : Dil bilgisini göz ardı eder, sadece istatistiksel tekrar sıklığına dayanır.  
    Kullanıldığı Modeller: GPT‑2, GPT‑3 vb.
    Adımlar:
-      Tüm kelimeleri harf harf ayırın.
-      En sık tekrar eden harf çiftini bulun.
-      Bu çifti birleştirin, yeni token ekleyin.
Tekrar ederek istenen sözlük boyutuna ulaşın.

Örnek: Hugging Face GPT‑2 Tokenizer
from transformers import GPT2Tokenizer

# GPT-2 önceden eğitilmiş tokenizasyon kütüphanesini yükler
```
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

text = "bilinmeyen kelime"
tokens = tokenizer.tokenize(text)
ids = tokenizer.convert_tokens_to_ids(tokens)

print("Tokens:", tokens)
print("IDs:", ids)
```
Açıklama:
tokenize() metni alt‑parçalara böler.
convert_tokens_to_ids() her bir token’a sayısal ID atar.
Bu sayede model, nümerik verilerle işlem yapabilir.

---

## Context Length Altında Padding

Bir dil modeli eğitimi sırasında girilen dizi, modelin `context_length` parametresinden (örn. 512 token) kısa ise:

- **Çözüm**: Dizinin sonuna özel `<PAD>` token’ları eklenir.  
- **Neden?**: Modelin sabit uzunlukta giriş beklemesi nedeniyle; aynı boyda tensörler oluşturulur.  

*Bir dil modeli eğitimi sırasında girilen dizinin context length’ten kısa olduğu durumlarda ne yapılır?*

      - Dizinin sonuna padding tokenlari eklenir.


## MNIST Data Set

- **Kaynak**: [Kaggle – MNIST Handwritten Digits Classification][1]  
- **Özellik**: 60.000 eğitim, 10.000 test örneği; 28×28 gri tonlamalı el yazısı rakam görüntüleri.




--

## Tokenizasyon Nedir?

Tokenizasyon, modelin anlayabileceği **tamsayısal** temsillere dönüştürmek için ham metni daha küçük parçalara (token’lara) ayırma işlemidir.  
Transformer tabanlı modeller metni doğrudan anlamaz; sayı ile işlem yaparlar. Bu yüzden:

> “Token is an integer that represents a character, or a short segment of characters…”  
> — Tokenizer modülünün tanımı

Örnek:
"Merhaba dünya" → ["Merhaba", "dünya"] veya ["Mer", "haba", "dü", "nya"]
---

## Tokenizasyon Türleri

### Word-Level Tokenization (Kelime Düzeyi)

```python
def word_level_tokenize(text):
    return text.split()

print(word_level_tokenize("Merhaba dünya, bugün nasılsın?"))
```
# Çıktı: ['Merhaba', 'dünya,', 'bugün', 'nasılsın?']
Ne yapar? Metni boşluk karakterinden bölerek kelimeleri çıkarır.
Nasıl çalıştırılır? Python 3 yüklü bir ortamda bu fonksiyonu içeren dosyayı çalıştırabilirsiniz.
Character-Level Tokenization (Karakter Düzeyi)
```python
def character_level_tokenize(text):
    return list(text)

print(character_level_tokenize("ABC"))
```
# Çıktı: ['A', 'B', 'C']
Ne yapar? Her karakteri ayrı bir token olarak işler.
Ne zaman tercih edilir? Dilin çok ince detaylarına girmek gerektiğinde; ancak eğitim maliyeti artar.
Subword Tokenization (Alt Parça Düzeyi)
Kelime ve karakter düzeyleri arasında bir denge sağlar.
Örnek: "bilinmeyen"
→ ["▁bil", "in", "me", "yen"]

Avantajı: Nadir kelimelerde bile parçalar tanınır; “unk” token sayısı azalır.

Subword Tokenizasyon Algoritmaları
Byte-Pair Encoding (BPE)
from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

text  = "bilinmeyen kelime"
tokens = tokenizer.tokenize(text)
ids    = tokenizer.convert_tokens_to_ids(tokens)

print("Tokens:", tokens)
print("IDs:", ids)
Ne yapar?
Karakterleri ayırır,
En sık görülen çiftleri birleştirir,
Yeni token’lar oluşturur.
Nasıl kullanılır? transformers kütüphanesini pip ile yükleyip (pip install transformers) bu kodu çalıştırın.
WordPiece
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

text  = "bilinmeyen kelime"
tokens = tokenizer.tokenize(text)
ids    = tokenizer.convert_tokens_to_ids(tokens)

print("Tokens:", tokens)
print("IDs:", ids)
Farkı: BPE yerine olasılığa dayalı seçim yapar.
Adımlar:
Karakterleri ayırır,
Parçaların birlikte görülme olasılıklarını hesaplar,
En yüksek olasılıklı birleşimleri gerçekleştirir.
SentencePiece
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google/mt5-small")

text  = "bilinmeyen kelime"
tokens = tokenizer.tokenize(text)
ids    = tokenizer.convert_tokens_to_ids(tokens)

print("Tokens:", tokens)
print("IDs:", ids)
Özellikleri:
Ön işlem yapmadan, bütün metni bir dize gibi ele alır.
Boşlukları özel karakter (_) ile temsil eder.
Kullanım alanı: Çok dilli veya morfolojik olarak zengin dillerde.

### Token ID’leri ve Vocabulary Nedir?
Token → ID dönüşümü: Model sayılarla çalışır.
Her modelin bir vocabulary dosyası (sözlüğü) vardır.
Token’lar eğitim ve çıkarım aşamasında bu ID’ler üzerinden işlenir.

### 💡 Tokenizer ve Detokenizer Nedir?
Tokenizer: Metni token’lara bölüp ID’lere çevirir.
Detokenizer: Model çıktısı ID’leri tekrar metne dönüştürür.
Akış:
Metin
  └─ Tokenizer → [token1, token2, …]
      └─ Numeralizasyon → [id1, id2, …]
          └─ Model çalışır
              └─ Detokenizer ile [id1, …] → [token1, …]
                  └─ Metni tekrar oluşturur

### Neden Tokenizasyon Bu Kadar Önemli?
Modelin kapasitesi, nadiren görülen kelimeleri tanıma ve genel başarımı büyük ölçüde buna bağlıdır.
Türkçe gibi eklemeli dillerde subword tokenizasyonu kritik avantaj sağlar.





## yapay zeka eğitebilmemiz için etiketli verilere ihtiyaç duyarız (Supervised Learning)
Supervised Learning, yapay zekanın geçmişteki etiketli verilerden öğrenerek gelecekteki veriler için doğru tahminler yapabilmesini sağlayan bir makine öğrenmesi yöntemidir.




Rotary Positional Encoding'in (RoPE), daha eski konum kodlama yöntemlerine göre en temel avantajı kelimelerin birbirlerine olan göreceli konumlarini ve mesafelerini de kodlayabilmesi.
RoPE fonksiyonunda, kelime vektörlerini "döndürmek" (rotate) için sin cos fonksiyon çifti kullanılmıştır.



bağlam içinde bulunduğumuz yerde kurduğumuz cümledir veya içinde geçtiği yer göre kazandığı anlam 






-----
n8n self hosted :
- starter kit  https://github.com/n8n-io/self-hosted-ai-starter-kit
- ollama -llm
öğren.

https://www.youtube.com/watch?v=huaCsAs02xY n8n hk. somut bir örnek teşkil ettiğini düşünüyorum. 

----

n8n Starter Kit ve Ollama LLM entegrasyonu için en kapsamlı kaynaklar:

## n8n AI Starter Kit Kaynakları

**Resmi Kaynaklar:**
- **GitHub Repository:** n8n-io/self-hosted-ai-starter-kit - Açık kaynak template
- **Resmi Dokümantasyon:** n8n.io/hosting/starter-kits/ai-starter-kit/
- **Hızlı Başlangıç:** n8n.io/try-it-out/quickstart/
- **AI Workflow Tutorial:** n8n.io/advanced-ai/intro-tutorial/
- **Learning Path:** n8n.io/learning-path/
- **Advanced AI Docs:** n8n.io/advanced-ai/

**Video ve Pratik Kaynaklar:**
- **Starter Kit Tutorial Video:** community.n8n.io/t/self-hosted-ai-starter-kit-tutorial/62465
- **Pratik Örnek (Medium):** A practical n8n workflow example from A to Z

## Ollama + n8n Entegrasyon Kaynakları

**Resmi Dokümantasyon:**
- **Ollama Model Node:** n8n.io/integrations/builtin/cluster-nodes/.../lmollama/
- **Ollama Credentials:** n8n.io/integrations/builtin/credentials/ollama/
- **Common Issues:** Ollama Model node troubleshooting

**Kapsamlı Rehberler:**
- **Hostinger Tutorial:** n8n-ollama integration detaylı rehber
- **Docker Guide:** n8n with Ollama LLM Locally Using Docker
- **Medium Tutorial:** n8n ve Ollama pipeline kurulumu
- **Advanced Integration:** Aleksandar Haber'in kapsamlı rehberi

**Hazır Workflow Şablonları:**
- **Chat Template:** Chat with local LLMs using n8n and Ollama
- **AI Agent Template:** Weather ve Wikipedia agent örneği

## Önerilen Öğrenme Sırası:

1. **Temel n8n:** n8n quickstart ve learning path'i tamamlayın
2. **AI Starter Kit:** GitHub repo'yu klonlayıp kurulum yapın
3. **Ollama Kurulum:** Yerel Ollama instance'ını çalıştırın
4. **Entegrasyon:** Docker rehberini takip ederek bağlantı kurun
5. **Pratik:** Hazır workflow şablonlarını test edin
6. **Gelişmiş:** Kendi AI agent'larınızı geliştirin







```bash
brew install --cask docker
```

Kurulum bittikten sonra:

1. **Docker Desktop'u başlatın:**
```bash
open /Applications/Docker.app
```

2. **Docker'ın çalıştığını kontrol edin:**
```bash
docker --version
```

3. **Ardından n8n kurulumuna devam edin:**

```bash
# Ollama'yı arka planda çalıştır
ollama serve &

# .env dosyasını kontrol et
cat .env

# Docker Compose'u başlat
docker compose up
```
Kurulum bittikten sonra http://localhost:5678 adresinden n8n'e erişebileceksiniz.



Docker kurduktan sonra:

Ollama'yı arka planda başlatın:

bashollama serve &

.env dosyasını kontrol edin:

bashcat .env
OLLAMA_HOST=host.docker.internal:11434 satırının olduğundan emin olun.

Docker Compose'u çalıştırın:

bashdocker compose up

Llama3.2 kurun (opsiyonel ama önerilen):

bashollama pull llama3.2








