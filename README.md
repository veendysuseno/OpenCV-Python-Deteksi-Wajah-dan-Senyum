# Deteksi Wajah dan Senyum dengan OpenCV

Proyek ini merupakan contoh sederhana penggunaan OpenCV dalam Python untuk mendeteksi wajah dan senyum dari gambar statis. Program membaca file gambar lokal, lalu menandai area wajah dan senyum dengan kotak dan teks pada hasil gambar.

## Fitur

- Deteksi wajah menggunakan Haar Cascade
- Deteksi senyum pada area wajah yang terdeteksi
- Menampilkan hasil deteksi dalam jendela OpenCV
- Menggunakan file cascade yang disimpan di folder proyek

## Struktur Project

```text
.
├── main.py                     # Script utama deteksi wajah dan senyum
├── gambar.jpg                  # Gambar uji yang digunakan
├── haarcascade_frontalface_default.xml
├── haarcascade_smile.xml
└── README.md
```

## Prasyarat

Pastikan Python sudah terinstal di komputer Anda. Selanjutnya, install library OpenCV:

```bash
pip install opencv-python
```

## Cara Menjalankan

1. Buka terminal atau command prompt.
2. Masuk ke folder proyek.
3. Jalankan perintah berikut:

```bash
python main.py
```

Program akan membaca `gambar.jpg`, mendeteksi wajah dan senyum, lalu menampilkan hasil deteksi di jendela baru.

## Penjelasan Singkat

File `main.py` melakukan hal berikut:

- Memuat cascade classifier untuk wajah dan senyum
- Membaca gambar dari folder proyek
- Mengubah gambar ke grayscale
- Mendeteksi wajah dengan `detectMultiScale()`
- Untuk setiap wajah yang terdeteksi, memeriksa area wajah tersebut untuk senyum
- Menggambar kotak dan label `Wajah` serta `Senyum`

## Catatan

- File Haar Cascade (`.xml`) diperlukan agar deteksi dapat berjalan.
- Kualitas deteksi tergantung pada pencahayaan, sudut wajah, dan kualitas gambar.
- Proyek ini cocok untuk pembelajaran dasar pengolahan citra dan deteksi objek dengan OpenCV.

## Lisensi

Proyek ini dibuat untuk tujuan pembelajaran dan dapat dikembangkan lebih lanjut sesuai kebutuhan.
