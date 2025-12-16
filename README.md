# Saat

**Saf Python. Sıfır Bağımlılık. Maksimum Minimalizm.**

Saat, masaüstünüzde havada asılı duran, çerçevesiz ve arka planı tamamen şeffaf olan ultra hafif bir dijital saattir. Harici hiçbir kütüphane (3rd party library) kullanılmadan, sadece Python'ın standart kütüphanesi ile yazılmıştır.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Size](https://img.shields.io/badge/Size-Tiny-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

## 🌟 Özellikler

* **Sıfır "Bloat":** `pip install` gerektirmez. Sadece Python ve `tkinter` (zaten gömülü gelir).
* **Hayalet Modu:** Pencere kenarlığı, başlık çubuğu veya arka plan rengi yoktur. Sadece zamanı görürsünüz.
* **Her Zaman Üstte:** Diğer pencerelerin altında kaybolmaz (`Always on Top`).
* **Sürükle & Bırak:** Pencere çerçevesi olmasa bile saati tutup ekranın istediğiniz yerine taşıyabilirsiniz.
* **Kaynak Dostu:** CPU ve RAM kullanımı yok denecek kadar azdır.

## 🚀 Kurulum ve Çalıştırma

Bu projeyi çalıştırmak için bilgisayarınızda Python'ın yüklü olması yeterlidir.

1.  Repoyu klonlayın veya zip olarak indirin:
    ```bash
    git clone [https://github.com/ibodeth/Saat.git](https://github.com/ibodeth/Saat.git)
    cd Saat
    ```

2.  Scripti çalıştırın:
    ```bash
    python main.py
    ```
    *(Not: Dosya adınız `main.py` değilse uygun şekilde değiştirin)*

## 🎮 Kontroller

Arayüz olmadığı için kontroller mouse hareketlerine entegre edilmiştir:

| Eylem | Sonuç |
| :--- | :--- |
| **Sol Tık + Sürükle** | Saati ekranın herhangi bir yerine taşır. |
| **Sağ Tık** | Uygulamayı anında kapatır. |

## 🛠️ Teknik Detaylar

* **Platform:** Windows (Şeffaflık ayarları Windows pencere yöneticisi için optimize edilmiştir).
* **Kütüphaneler:** `tkinter`, `time`
* **Font:** Consolas (Sisteminizde yoksa varsayılan monospace fonta döner).

## 📝 Lisans

Bu proje [MIT](LICENSE) lisansı altında lisanslanmıştır. İstediğiniz gibi kullanabilir, değiştirebilir ve dağıtabilirsiniz.
