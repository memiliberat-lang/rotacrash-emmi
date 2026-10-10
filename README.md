# 📍 RotaMaster - Google Maps Akıllı Rota Optimize Edici

Google Haritalar'da çoklu durakları (8-10 durak) en kısa mesafeye göre sıralayan ve tek tıkla telefonunuzdaki Google Maps uygulamasını optimize edilmiş sırayla başlatan mobil web uygulaması.

---

## 🚀 Nasıl Çalıştırılır?

### Yöntem 1: Çift Tıklayarak (En Kolay)
1. Klasördeki **`baslat.bat`** dosyasına çift tıklayın.
2. Açılan siyah pencerede telefonunuzdan girebileceğiniz bağlantı yazacaktır:
   - **`http://192.168.1.170:8080`**
3. Bilgisayarınızda tarayıcı otomatik açılacaktır. İsterseniz sağ üstteki **QR Kod** simgesine tıklayıp telefon kameranızla okutarak anında açabilirsiniz.

---

## 📱 Telefonda Kullanım (Ana Ekrana Ekleme)

Uygulamayı telefonunuzun tarayıcısında açtıktan sonra:
* **iPhone (Safari):** Alttaki **Paylaş** simgesine dokunun > **"Ana Ekrana Ekle"** deyin.
* **Android (Chrome):** Sağ üstteki **üç nokta** menüsüne dokunun > **"Ana Ekrana Ekle"** veya **"Uygulamayı Yükle"** deyin.

Artık ana ekranınızda bağımsız bir mobil uygulama gibi simgesi yer alacaktır.

---

## 🛠️ Özellikler

1. **📍 Konum & Adres Ekleme:**
   - **Mevcut Konumum:** GPS üzerinden bulunduğunuz yeri başlangıç noktası olarak ekler.
   - **Adres Arama:** Yazarken canlı öneri getiren adres arama motoru.
   - **Haritadan Seçme:** Harita üzerindeki herhangi bir yere dokunarak durak belirleme.
   - **Toplu Adres Ekleme:** Elinizdeki liste veya koordinatları tek seferde yapıştırma.
   - **8 Örnek:** Tek tıkla 8 adet örnek durağı yükleyip test etme.

2. **⚡ Akıllı Optimizasyon (TSP - Gezgin Satıcı Problemi Algoritması):**
   - 8-10 durağa kadar olan tüm kombinasyonları milisaniyeler içinde inceleyerek **%100 matematiksel olarak en kısa yolu** bulur.
   - Dairesel tur (başlangıç noktasına geri dön) veya Tek Yön seçenekleri mevcuttur.
   - OSRM yol ağı verileriyle gerçek sürüş mesafesi ve tahmini seyahat süresini hesaplar.

3. **🗺️ Google Maps Entegrasyonu:**
   - Duraklar sıralandıktan sonra **"Google Haritalar'da Başlat"** butonuna bastığınızda, telefonunuzdaki orijinal Google Maps uygulaması durakları bu sırayla açar ve doğrudan navigasyona hazır hale getirir.
